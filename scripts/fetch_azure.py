import pyodbc


connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=tcp:bahiafix.database.windows.net,1433;"
    "DATABASE=bfix_database;"
    "UID=bfixmaster;"
    "PWD=B@fix3024;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=100;"
)

cnxn = None

try:
    cnxn = pyodbc.connect(connection_string)
    cursor = cnxn.cursor()

    cursor.execute("SELECT TOP 10 * FROM pedidos")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Insira um novo registro (exemplo)
    # cursor.execute("INSERT INTO sua_tabela (coluna1, coluna2) VALUES (?, ?)", 'valor1', 'valor2')
    # cnxn.commit()

except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    print(f"Erro ao conectar ou executar a consulta: {sqlstate}")
    print(ex)

finally:
    if cnxn:
        cnxn.close()
        print("Conexão encerrada.")
