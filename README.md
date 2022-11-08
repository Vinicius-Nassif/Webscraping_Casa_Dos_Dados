# Projeto Web Scraping

## 1. Introdução

​		Web Scraping, ou raspagem de dados, é uma modalidade de mineração que admite a extração de dados de sites da web convertendo em informação estruturada para análise futura. Geralmente, essa técnica é realizada por meio de um software que simula uma navegação humana nos sites desejados, extraindo informações específicas. 

​		Nesse projeto, o Python foi adotado como linguagem de programação para instrumentalizar o serviço de um freelancer responsável que deveria ir até o site Casa dos Dados (https://casadosdados.com.br/solucao/cnpj/pesquisa-avancada), realizar a varredura de todos os registros com código de atividade empresarial de consultoria em tecnologia da informação (cod: 6204000)  para obter as seguintes informações:

- Número do CNPJ;

- Nome;

- Status; e

- Endereço.

  ​ Após a obtenção das informações de todos os anúncios, esses dados serão inseridos e armazenados em uma planilha do Excel (.xlsx), bem como no MySQL. 

  ​	O intuito dessa atividade irá expor mais intensivamente a automação web, loops, variáveis, manipulações de arquivos, divisão de tarefas em módulos, tratamento de exceções e criação de um banco de dados no MySQL, conforme será demonstrado a seguir.


## 2. Módulos

Módulo é um arquivo contendo funções em *Python* para serem usados em outros programas da mesma linguagem. 

Para instrumentalizar essa atividade de maneira organizada, foi realizada em dois módulos de código *Python*:

- webscraping.py; e
- data_to_mysql.py.

Cada um será responsável por etapas do processo e serão abordados no decorrer desse trabalho. 



## 3. webscraping.py

### 3.1 Bibliotecas

​		O projeto teve início no primeiro módulo com a importação das bibliotecas e funções utilizadas na elaboração do código em Python:

![1](https://user-images.githubusercontent.com/111388699/200622568-e37ec6b4-efc4-489a-8b78-4dd13e3ae36e.png)

​		Primeiramente, ocorreu a importação da R*equests*, que é uma biblioteca HTTP para a linguagem de programação e tem como funcionalidade tornar as solicitações HTTP mais simples e mais fáceis de usar. 

​		Na sequência, a biblioteca *BeautifulSoup*, tem como funcionalidade a extração de dados de arquivos HTML e XML, funciona também como interpretador (parser). Já a biblioteca *Selenium* é uma ferramenta empregada para automatização de testes de sistemas que permite ao usuário reproduzi-los em passo acelerado no ambiente real da aplicação, em função da sua integração direta com o navegador.

​		Da biblioteca *time*, foi importado o método *sleep* com o objetivo de suspender a execução pelo número de segundos informado em seu parâmetro. Por último, foi importada a biblioteca *Pandas* como a sigla “pd”, com o objetivo de manipulação e análise de dados.



### 3.2 Código

#### def __init__(self, url, consulta, arquivo):

​		O código teve início com a denominação de uma classe chamada *WebScraping():* e sua primeira função foi a __init__():, como podemos ver a seguir:

![2](https://user-images.githubusercontent.com/111388699/200622653-6d76201f-6bc7-4e65-a2a7-753376941e8f.png)

​		O método *__init__():* é um método especial para que o *Python* execute automaticamente sempre que criarmos uma nova instância baseada na classe WebScraping(): foi definido para ter quatro parâmetros: o *self, url*, consulta e arquivo.

​		Logo abaixo, iniciou-se os atributos *self.site*, *self.navegador* e *self.registros* como vazios com o objetivo de receberem seus valores no desenvolvimento do código. O objeto *self.dados_cnpj* foi criado como uma lista vazia a ser preenchida futuramente com um *dataframe*. 

​		Já o *self.options* recebeu o método *Options()*, nativo da biblioteca *Selenium*, que por sua vez recebeu as configurações de inicialização do navegador, sendo a linha 24 para especificar as dimensões da janela do navegador a ser aberta e, na linha 26, para que seja toda rotina realizada sem ser fechada, porém, foi deixada comentada. 

​		Na sequência, com o objetivo de demonstrar que a inicialização de todo método *__init__():* ocorreu com êxito, na linha 28 foi definido para exibir uma mensagem pelo método *print(‘WebScraping inicializado’)*. 



#### def get_url(self):

​		Essa função indica a automação do navegador Google Chrome.

![3](https://user-images.githubusercontent.com/111388699/200622783-da075270-1434-4e80-978c-c54ec119b82f.png)

​		A automação iniciou-se por meio do *self.navegador* recebendo *o webdriver* do *Selenium*, com as opções atribuídas no método *__init__*. A função do *webdriver* é manipular o navegador nativamente, como um usuário faria, por meio de automação, seja localmente ou em uma máquina remota usando o servidor *Selenium*.

​		Na sequência, trazendo o método *self.navegador.get(self.url)* com a biblioteca *Requests*, realizando a solicitação HTTP para a linguagem de programação. 

​		O método *sleep* recebeu como parâmetro 3 segundos para aguardar antes de seguir para o próximo método, evitando erros no processo  e evitando a detecção da automação web enquanto ocorre a abertura do navegador e a solicitação do HTTP. 



#### def navegacao(self):

Essa função identifica e executa os elementos de navegação do site casa dos dados. 

![4](https://user-images.githubusercontent.com/111388699/200622893-dda7c404-20ad-4d93-83c8-9a56a45d8817.png)

​		A imagem demonstra que foi criada a variável *pesquisa_codigo* e ela recebeu o *self.navegador* com o método *find_element* (pertencente à biblioteca do *Selenium*) para encontrar o elemento pelo *xpath* alocando os atributos entre parênteses após inspeção da estrutura HTML do site. 

​		Encontrado o elemento, a variável *pesquisa_codigo* recebe o comando de clicar por meio do método *click()*, ficando o espaço apto para receber o número do código desejado por meio do método *send_keys(self.consulta)* (imagem a seguir).

​		Assim, surge uma caixa preditiva com a opção digitada e para dar continuidade a navegação ocorre a nomeação de uma variável como *dropdown* e ela recebe o *self.navegador*  com o método *find_element* para encontrar o elemento pelo *xpath*.

​		Na linha 49, foi definida a variável *botao_pesquisa* recebendo o *self.navegador*  com o método *find_element* para encontrar o elemento pelo *xpath* e, na linha 52, essa variável recebeu o método *click()*, enviando a pesquisa desejada.

​		Os métodos *sleep* intercalados receberam como parâmetros segundos variados para aguardar seguir para as próximas etapas, evitando erros na execução e a detecção da automação, permitindo também a visualização dos passos.

![5](https://user-images.githubusercontent.com/111388699/200622983-b6d4b9a0-555b-4095-b47c-e3caae88b050.png)



#### def integracao_bs(self):

​		Essa função indica o início da integração com a biblioteca *BeautifulSoup*. 

![6](https://user-images.githubusercontent.com/111388699/200623093-b042da3f-355d-455f-9edf-612f8ca0ab5c.png)

​		A variável *self.site* recebeu o método *BeautifulSoup*, tendo como parâmetros o *self.navegador.page_source* e o *html.parser*. Aqui ocorre a preparação para identificação do conteúdo a ser extraído e interpretação do conteúdo HTML. 



#### def identifica_box(self):

​		Essa função identifica o atributo raiz dos registros.

![7](https://user-images.githubusercontent.com/111388699/200623188-aba72313-9acf-409c-bb53-ddc4153eeb1b.png)

​		Já com a biblioteca *BeutifulSoup* integrada com o *Selenium*, a variável *self.hospedagens* recebeu a variável *self.site* com o método *findAll*, com os parâmetros inspecionados da estrutura HTML: div e o atributo de classe a partir da interpretação do conteúdo HTML.

​		Esses parâmetros foram observados como padrões na estrutura raiz dos anúncios de cada registro. Portanto, a função foi orientada para identificar o bloco raiz de todos os registros da estrutura HTML de cada página a ser percorrida durante a execução do *Web Scraping*. A imagem a seguir ilustra a inspeção desse elemento:

![8](https://user-images.githubusercontent.com/111388699/200623328-a5bfd29b-9169-48d8-b3cf-1322f8958114.png)



#### def raspagem_dados(self):

​		Essa função é responsável pela automação da raspagem de dados de cada de detalhe desejado no registro. 

![9](https://user-images.githubusercontent.com/111388699/200623401-b60d178a-db15-4747-855b-9dcb98d6654d.png)

​		Para que a raspagem ocorresse da forma desejada, a função foi introduzida por um laço de repetição *for*. Para cada registro dentro da variável *self.registros*, seria extraída o número, o nome, o status e o endereço.

​		Cada variável recebeu o registro com o método *find* e entre os parênteses os parâmetros encontrados na inspeção da estrutura HTML. 

​		Para as variáveis *registro_numero* e *registro_status*  foi chamado o método *get_text()* com o objetivo de trazer as informações limpas, sem trechos das estruturas HTML. 

​		As variáveis *registro_nome* e *registro_endereco*, além do método *find()*, receberam também o método findNext(), para que fosse encontrado na estrutura HTML o próximo tópico semelhante na sequência, seguido de *.content[0]*  para a extração somente do respectivo texto. Ainda na variável *registro_endereço* foi utilizado uma operação de fatiamento de strings (slicing) "*[2:]*" com o objetivo de extrair apenas a parte útil do dado desejado. 

​		Após definida a estrutura da extração de dados de cada variável, o método *print()* foi chamado, para cada uma delas, de forma que ficasse organizado no terminal do interpretador, sendo que foi utilizado um "*print()*" vazio para realizar uma quebra de linha entre as informações extraídas. 

![10](https://user-images.githubusercontent.com/111388699/200623472-b7d398c2-c511-4a01-aff3-4a23aa47c801.png)

​		Encerrando o laço *for*, foi criado um *dataframe* na variável *self.dados_cnpj* com o método *append*, que serviu para anexar as informações extraídas em cada campo especificado.



#### def prox_pag(self):

​		Essa função é responsável em encontrar e executar a paginação do website.

![11](https://user-images.githubusercontent.com/111388699/200623549-b574b755-50b6-40a4-a89d-1f4121d92fc5.png)

​		É iniciada com a orientação *try*, ou seja, que o *Python* realize a tentativa recebendo a variável *next_button* com a variável *self.navegador* com o método *find_element* pelos parâmetros do HTML. Esse elemento é para identificar o botão de próxima página (“setinha”) que se encontra no próprio site, como se o usuário estivesse visualizando onde clicar desejando a paginação.

![12](https://user-images.githubusercontent.com/111388699/200623646-5a4f954f-f432-4d69-b846-cfcfb19c0f98.png)

​		Na sequência, a variável *botao_vazio* recebeu o *next_button* com o método *get_property(‘disabled’)* para identificar caso o botão de paginação tenha em sua propriedade que está desabilitado, com o intuito de encerrar a paginação e evitar erros. 

​		Assim, ao se iniciar a condicional *if botao_vazio is True*:, deve o *Python* encerrar a raspagem de dados, dando o retorno *False* para o laço de paginação *While* criado na execução (será explicado ao longo desse documento), ou seja, se o botão estiver com a propriedade de desabilitado, ele não poderá mais ser clicado para passar a página e indicará que é a última página a ser raspada, encerrando o laço. 

​		Enquanto o *next_button* permanecer sendo encontrado com a propriedade habilitada, será aguardado 2 segundos pelo método *sleep()* e, então clicado, retornando o valor de *True* para o laço de paginação citado no parágrafo anterior, prosseguindo para raspagem de dados da página seguinte. 

​		Ao ser finalizada a orientação *try:*, é indicado o *except Exception as e:* para que seja colocado em um método *print()* a exceção que ocorreu no código.



#### def criar_tabela(self):

​		Essa função é responsável pela criação da planilha no Excel. 

![13](https://user-images.githubusercontent.com/111388699/200623682-ae7e8cc6-2de5-4cfd-bfe4-c7c97920ce0e.png)

​		A variável dados recebeu o Pandas com a sigla pd e o método *DataFrame*, atribuindo à *self.dados_cnpj* as colunas ‘Número’, ‘Nome’,‘Status’ e ‘Endereço’. 

​		Cada uma dessas colunas receberá o dataframe com os dados correspondentes que foram raspados do site casa dos dados. 

​		Por fim, a variável dados, que detém todo o *dataframe*, foi colocada com o método *to_excel* com os parâmetros *self.nome_arquivo* e *index=False*, indicando a criação da planilha. 



#### Execução - if __name__== '__main__':

Podemos usar um bloco **if __name__ ==** ''**__main__**'' para permitir ou evitar que partes do código sejam executadas ao importar os módulos. Quando o interpretador do *Python* lê um arquivo, a variável **__name__** é definida como **__main__**, se o módulo está sendo executado, ou como o nome do módulo se ele for importado.

![14](https://user-images.githubusercontent.com/111388699/200623756-30a94487-a5c6-4bfb-ae54-40d754e856fa.png)

​		Tem o objetivo de orquestrar a execução sequencial de todas as fases do web scraping, como um índice representativo e intuitivo, com o chamado de todos os métodos já explicados e trazendo também mensagens de êxito nas conclusões de cada etapa pelo método *print()*. 

​		Foi criada a variável casa_dos_dados recebendo a classe WebScraping, dando como parâmetros a url='https://casadosdados.com.br/solucao/cnpj/pesquisa-avancada’, a consulta=’6204000’ e o arquivo=’dados_cnpj.xlsx’. Lembrando que esses parâmetros estavam sendo preparados desde a *def __init__():*.

​		Nesse momento, é necessário chamar a atenção aos passos das linhas 119 a 133 que abordam a criação do laço de paginação empregado.

​		O laço teve início com a criação da variável *botao_prox_pag* e a ela foi atribuído o valor *True*. Na linha subsequente, essa variável foi alocada em um laço *while* atribuindo o funcionamento das etapas indentadas (linhas 119 a 133) enquanto o *botao_prox_pag* permaneça com o valor de verdadeiro (*True*). Assim, a variável *botao_prox_pag* foi atribuída a função *self.prox_pag():*. 

​		A análise de valor como verdadeiro ou falso foi feita pela função *self.prox_pag()*:,encerrando o laço while, prosseguindo para criação da tabela e conclusão da execução do código.



### 3.3 dados_cnpj.xlsx

​		Vejamos como ficou parte da planilha após receber o *dataframe* criado:

![15](https://user-images.githubusercontent.com/111388699/200623820-5a4631c5-2f72-4b03-abe5-dc6892769853.png)



## 4. data_to_mysql.py

### 4.1 Bibliotecas

​		O segundo módulo teve início com a importação das seguintes bilbiotecas

![16](https://user-images.githubusercontent.com/111388699/200623900-313458b4-8815-4a8a-bf8d-c056386a3b4c.png)

​		O MySQL é um sistema de gerenciamento de dados estruturados relacionais e como o *Python* não tem acesso nativo à banco de dados MySQL, foi necessário importar a biblioteca *mysql.connector*, crianco um script de conexão.

​		Na sequência, a biblioteca *xlrd*, tem como funcionalidade de recuperar ou fazer leitura de informações constantes em uma planilha. Já a biblioteca *os* é uma ferramenta empregada para obter funcionalidades dependentes do sistema operacional.



### 4.2 Código

#### def __init__(self, host, schema):

​		O código teve início com a denominação de uma classe chamada *Excel_to_Mysql():* e sua primeira função foi a __init__():, como podemos ver a seguir:

![17](https://user-images.githubusercontent.com/111388699/200624046-da5659bb-3994-4399-92a7-1073f2bd11c6.png)

​		O método *__init__* foi definido para ter três parâmetros: o *self*, *host e schema*.

​		Logo abaixo, iniciam-se os objetos *self.conn* e *self.cur*  como vazios com o objetivo de receberem seus valores no desenvolvimento do código. As variáveis *self.my_db_user* e *self.my_db_password* receberam, por meio da biblioteca *os* e do método *get()*, variáveis de ambiente para não ocorrer exposição de credenciais partiulares no script. 



#### def criar_servidor(self):

​		Essa função é responsável pela criação da tabela no servidor MySQL.

![18](https://user-images.githubusercontent.com/111388699/200624119-a86c418c-0bfe-468f-92a6-adb121527207.png)

​		A variável *self.conn* recebeu o método  da biblioteca mysql.connector para estabelecer a conexão, indicando como parâmetros a hospedagem do *database* com o *self.host*, o usuário com *self.my_db_user*, a senha como *self.my_db_password* e o nome do banco de dados no MySQL como *self.schema*.

​		A variável *self.cur* recebeu a variável *self.conn* com o método *cursor()*, que inicia a interação com o servidor MySQL. 

​		Na sequência a variável *self.cur* recebeu o método *execute()* para estabelecer a formatação e lacunas da tabela cnpj, sendo o número como chave primária (PK).  Varchar é uma abreviação para VARiable-length CHARacter string, que é uma sequência de caracateres de texto que pode ser tão grande quanto o tamanho especificado entre parênteses para a tabela de banco de dados da coluna em questão.

​		Por último, a variável *self.conn* recebeu o método *close()* para desconectar do servidor MySQL. 



#### def conexao_mysql(self):

​		Essa função é responsável por estabelecer a conexão com servidor MySQL e por inteirar os dados na tabela já criada.

![19](https://user-images.githubusercontent.com/111388699/200624226-7733d6e5-f9b0-4573-98e4-aa88d0941120.png)

​		A variável *self.conn* recebeu o método  da biblioteca mysql.connector para estabelecer a conexão, indicando como parâmetros a hospedagem do *database* com o *self.host*, o usuário com self.my_db_user*, a senha como "self.my_db_password* e o nome do banco de dados como *self.schema*.

​		A variável *self.cur* recebeu a variável *self.conn* com o método *cursor()*, que inicia a interação com o servidor MySQL. 

​		A variável *lista* recebeu o método *list()* para criar uma lista de objetos. A variável diretório especifica o diretório da planilha dados_cnpj.xls. 

​		A variável arquivo recebeu o método *xlrd.open_workbook()* para acessar os dados da planilha no diretório.  A variável *sheet* recebeu a variável e método *arquivo.sheet_by_index()* para contagem do index. Na sequência foi estabelecido os valores das células da planilha com o método *cell_value()*.

​		Para que os dados sejam inseridos forma desejada,  foi introduzido um laço de repetição *for*. Para cada i em alcance de 1 a 1000, a lista será preenchida pelo método *append* de todos os valores da planilha. Encerrado aqui o laço de repetição. 

​		Criada a variável *command_to_sql*, recebeu a instrução de que havendo algum dado repetido na chave primária (PK), esse seria substituído pelo último a aparecer com a mesma informação. Com isso evita-se a duplicidade de dados no *database*. 

​		A variável *self.cur* recebeu o método executemany(command_to_sql, lista)* para preparar a operação do *database* (query ou command) e executar os parâmetros sequenciais ou mapeados estabelecidos.

​		Então, a variável *self.conn* recebeu o método *commit* para efetivar as alterações feitas na tabela no servidor MySQL. 

​		Por último, a variável *self.conn* recebeu o método *close()* para desconectar do servidor MySQL. 



#### Execução - if __name__ == '__main__':

![20](https://user-images.githubusercontent.com/111388699/200625237-c488343f-8be1-4d57-bde3-8bf8ac6313d2.png)

​		Novamente, tem o objetivo de orquestrar a execução sequencial de todas as fases do envio das informações da planilha do excel para o MySQL, como um índice representativo e intuitivo, com o chamado de todos os métodos já explicados e trazendo também mensagens de êxito nas conclusões de cada etapa pelo método *print()*. 

​		Foi criada a variável *build* recebendo a classe Excel_to_Mysql, dando como parâmetros o host="localhost" e schema=’casadosdados’. Lembrando que esses parâmetros estavam sendo preparados desde a *def __init__():*.

​		É estabelecida a variável *servidor_vazio* como *True* (verdadeira) e com a condição *if* abaixo indentada tendo essa variável ainda como verdadeira, é iniciada com a orientação *try*, ou seja, que o *Python* realize a tentativa recebendo a variável *build* com o método *criar_servidor()* e exibir uma mensagem de êxito, caso ainda não exista a tabela pretendida. Ao ser finalizada a orientação *try:*, é indicado o *except Exception as e:* para que seja colocado em um método *print()* a exceção que ocorreu no código.

​		Passada essa etapa, é criada a variável tabela_existe como True (verdadeira) e com a condição if abaixo indentada tendo essa variável ainda como verdadeira, é iniciada com a orientação Try, recebendo a variável *build* com o método *conexao_mysql()*, exibindo mensagem de êxito e conclusão de todo o procedimento. Ao ser finalizada a orientação *try:*, é indicado o *except Exception as e:* para que seja colocado em um método *print()* a exceção que ocorreu no código.



## 6. Conclusão

​		Esse projeto foi criado para melhor elucidar o conhecimento trazido pela extração de dados, pois no seu desenvolvimento foi necessária a interação de várias bibliotecas do Python, bem como entender conceitos e aplicações da lógica de programação.

​		Percebeu-se também que para solucionar o problema principal foi necessário dividi-lo em pequenas tarefas para o desenvolvimento. 

​		Portanto, essa é uma forma de usar a coleta e manipulação de dados a seu favor, seja para uso pessoal ou profissional.
