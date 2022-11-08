import mysql.connector     # Disponibiliza função para conectar ao MySQL 
import xlrd				   # Ferramenta para extrair informações de um .xls 
import os                  # Funcionalidades dependentes do sistema operacional

class Excel_to_Mysql():

	def __init__(self, host, schema):
		# Alocando argumentos
		self.host = host
		self.schema = schema

		# Inicializando objetos
		self.conn = None
		self.cur = None
		self.my_db_user = os.environ.get('MY_DB_USER')
		self. my_db_password = os.environ.get('MY_DB_PASS')

	def criar_servidor(self):
		# Criação da tabela no servidor MySQL:
		## Função importada da biblioteca mysql.connector para estabelecer conexão com MySQL.
		self.conn = mysql.connector.connect(host = self.host,
										user = self.my_db_user,
										passwd = self.my_db_password, 
										database = self.schema)
		self.cur = self.conn.cursor()

		## Ferramenta para estabelecer dados de formatação e lacunas das tabelas.
		self.cur.execute("create table cnpjs(NUMERO varchar(30) primary key," 
						"NOME varchar(150), STATUS varchar(10), ENDERECO varchar(80))")
		self.conn.close()

	def conexao_mysql(self):
		# Função importada da biblioteca mysql.connector para estabelecer conexão com MySQL.
		self.conn = mysql.connector.connect(host = self.host,
										user = self.my_db_user,
										passwd = self.my_db_password, 
										database = self.schema)
		self.cur = self.conn.cursor()
		lista = list()
		diretorio = ("C:\\Users\\ccece\\Documents\\Projetos AD\\"
			"3 - Criação de banco de dados de CNPJ\\dados_cnpj.xls")
		arquivo = xlrd.open_workbook(diretorio)
		sheet = arquivo.sheet_by_index(0)
		sheet.cell_value(0,0)
		
		for i in range(1,1000):
			lista.append(tuple(sheet.row_values(i)))

		command_to_sql = ("replace into cnpjs(NUMERO,NOME,STATUS,ENDERECO)"
			 "values(%s,%s,%s,%s)")

		self.cur.executemany(comand_to_sql, lista)

		self.conn.commit()

		self.conn.close()


if __name__=='__main__':
	build = Excel_to_Mysql(host = "localhost", schema = "casadosdados")
	# Execução sequencial de todas as fases da classe Excel_to_Mysql:
	# 1. Criação da planilha e sua formatação no servidor MySQL
	servidor_vazio = True
	if servidor_vazio:
		try:
			build.criar_servidor()
			print('criar_servidor executado com sucesso')
		except Exception as e:
			print('Tabela já existente no servidor MySQL', e)
			pass

	# 2. Estabelecer conexão e inserir tabela no servidor MySQL		
	tabela_existe = True
	if tabela_existe:
		try:
			build.conexao_mysql()
			print('conexao_mysql executada com sucesso')			
			print('Excel_to_Mysql concluído!')
		except Exception as e:
			print('Tabela já contém informações', e)
			pass


	
	