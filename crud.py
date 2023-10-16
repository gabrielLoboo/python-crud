import cx_Orace

#obter/criar um conexão com o Oracle
def getConnection():
    try:
        conn = cx_Orace.connect(user="rm99708", password="180105", host="oracle.fiap.com.br", port="1521", service_name="orcl")
        print(f'Conexao: {conn.version}')
    except Exception as e:
        print('Erro ao obter uma conexão' , e)
    return conn

def select():
    conn = getConnection()
    cursor = conn.cursor()
    query = "SELECT * FROM CEO_DETAILS"
    cursor.execute(query)
    for result in cursor:
        print(result)
    conn.commit()

def insert(ceo):
    conn = getConnection()
    cursor = conn.cursor()
    query = "INSERT INTO CEO_DETAILS values('1', 'Gabriel', '12345')" 
    cursor.execute(query)
    conn.commit()
      
def update():
    try:
        conn = getConnection()
        cursor = conn.cursor()
        query = "UPDATE CEO_DETAILS set cpf = 123456 WHERE nome = 'Gabriel'"
    except Exception as e:
        print(f'Something went wrong {e}')
    finally:
        conn.commit()
        conn.close()
    

def delete():
    try:
        conn - getConnection()
        cursor = conn.cursor()
        query = "DELETE FROM CEO_DETAILS where nome = 'Gabriel'"
        cursor.execute(query)
        conn.commit()
        print('CEO removed!')
    except Exception as e:
        print(f'Something went wrong: {e}')
    finally:
        conn.close()

    
def close_connection(conn):
    try:
        conn.close()
        print(f'Connection closed!')
    except Exception as e:
        print(f'Something went wrong: {e}')


#principal
print(f'Obtendo do dados do BD')

conn = getConnection()
select()
insert()
close_connection(conn)

        
