from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

class WebScraping():

    def __init__(self, url, consulta, arquivo):
        # Alocando argumentos
        self.url = url
        self.consulta = consulta
        self.nome_arquivo = arquivo

        # Inicializando objetos
        self.site = None
        self.navegador = None
        self.registros = None
        self.dados_cnpj = []

        # Expecifica configurações de inicialização do navegador -- Selenium
        self.options = Options()
        self.options.add_argument('window-size=maximized')  # Dimensões da janela aberta
        self.options.add_experimental_option("detach", True) # Manter o Chrome aberto
        ## self.options.add_argument('--headless')  # Realiza a rotina sem abrir o navegador

        print('Web Scraping inicializado!')

    def get_url(self):
        # Indicando a automação do Chrome 
        self.navegador = webdriver.Chrome(options=self.options)
        self.navegador.get(self.url)

        sleep(3)

    def navegacao(self):
        # Indentificando e executando os elementos de navegação
        pesquisa_codigo = self.navegador.find_element(By.XPATH, 
            "//*[@id='__layout']/div/div[2]/section/div[2]/div[2]/section/div/div/div/div/div[1]/input")
        pesquisa_codigo.click()
        sleep(1)
        pesquisa_codigo.send_keys(self.consulta)
        sleep(1)
        dropdown = self.navegador.find_element(By.XPATH, 
            "//*[@id='__layout']/div/div[2]/section/div[2]/div[2]/section/div/div/div/div/div[2]/div/a")
        dropdown.click()
        sleep(2)
        botao_pesquisa = self.navegador.find_element(By.XPATH, 
            "//*[@id='__layout']/div/div[2]/section/div[6]/div/div[1]/button[1]")
        sleep(2)
        botao_pesquisa.click()

        sleep(5)
        
    def integracao_bs(self):
        # Início da integração do BeautifulSoup
        self.site = BeautifulSoup(self.navegador.page_source, 'html.parser')

    def identifica_box(self):
        # Identificação do atributo raiz do registro
        self.registros = self.site.findAll('div', class_='box')

    def raspagem_dados(self):     
        # Automação da busca dos registros 
        for registro in self.registros:
            registro_numero = registro.find('strong').get_text()
            registro_nome = registro.find('strong').findNext('strong').contents[0]
            registro_status = registro.find('small').get_text()
            registro_endereco = registro.find('small').findNext('small').contents[0][2:]
            
            print('Número:', registro_numero)
            print('Nome:', registro_nome)
            print('Status:', registro_status)
            print('Endereço:', registro_endereco)

            # Utilizado para quebra de linhas
            print()

            # Criação do DataFrame
            self.dados_cnpj.append([registro_numero,
                                    registro_nome,
                                    registro_status,
                                    registro_endereco])

    def prox_pag(self):
        try:
            next_button = self.navegador.find_element(By.XPATH, 
                            "//*[@id='__layout']/div/div[2]/section/div[10]/div/nav/a[2]")
            botao_vazio = next_button.get_property('disabled')
            if botao_vazio is True:
                print('Raspagem encerrada com sucesso!')
                return False
            sleep(2)
            next_button.click()
            print('Seguindo para a próxima página:')
            return True
        except Exception as e:
            print(e)

    def criar_tabela(self):
        dados = pd.DataFrame(self.dados_cnpj, columns = ['Número',
                                                        'Nome',
                                                        'Status',
                                                        'Endereço'])
        dados.to_excel(self.nome_arquivo, index = False)

if __name__=='__main__':
    casa_dos_dados = WebScraping(url='https://casadosdados.com.br/solucao/cnpj/pesquisa-avancada', 
                            consulta='6204000', arquivo='dados_cnpj.xlsx')
    # Execução sequencial de todas as fases do Web Scraping:
    #   1. Pesquisar pelo URL do site Casa dos Dados
    casa_dos_dados.get_url()
    print('get_url executado com sucesso')
    #   2. Buscar pelo botão de pesquisa
    casa_dos_dados.navegacao()
    print('navegacao executada com sucesso')
    
    ### Laço de Paginação
    botao_prox_pag = True
    while botao_prox_pag is True: 
        #   3. Interpretar o HTML da página
        casa_dos_dados.integracao_bs()
        print('integracao_bs executado com sucesso')
        #   4. Indentica a raiz do registro
        casa_dos_dados.identifica_box() 
        print('identifica_box executado com sucesso:')
         #  5. Listar registros da página atual
        casa_dos_dados.raspagem_dados()
        print('raspagem de dados executada com sucesso:')
        sleep(2)
        #   6. Seguir para próxima página
        botao_prox_pag = casa_dos_dados.prox_pag()
        sleep(3)
            
    #   7. Criar tabela com dataframe   
    casa_dos_dados.criar_tabela()
    print('criar_tabela executado com sucesso:')
    print('Web Scraping conclúido!')