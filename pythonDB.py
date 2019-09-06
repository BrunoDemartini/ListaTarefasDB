import pymysql
import pymysql.cursor

class DBconnector:
	def __init__(self):
		self.host = '192.168.56.101',
		self.user = 'admin',
		self.password = 'admin123',
		self.db = 'tarefas',
		charset = 'utf8'
		cursorclass=pymysql.cursors.DictCursor

def add_tarefas(a,b,c,d,e):

        descricao = a
        prioridade = b
        dataConclusao = c
        foiConcluido = d
        nome = e
        
        with con:

            cur = con.cursor()
            cur.execute("INSERT INTO tarefas.tarefas_table(descrição,prioridade,data_conclusao,foi_concluido, nome) VALUES('"+descricao+"','"+prioridade+"','"+dataConclusao+"','"+foiConcluido+"','"+nome+")")
            cur.execute("SELECT * FROM tarefas_table")
            rows = cur.fetchall()

def listar():
        
        for row in rows:
                print(row["id"], row["nome"], row["descricao"], row["prioridade"], row["data_conclusao"], row["foi_concluido"])


def deletar_tarefa(a):

        linha = a

         with con:

            cur = con.cursor()
            cur.execute("SELECT * FROM tarefas_table")
            cur.execute("DELETE FROM tarefas_table WHERE id = '"+linha+"';")
            rows = cur.fetchall()
        
