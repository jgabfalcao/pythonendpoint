import os

# Caminho do arquivo do banco de dados
db_path = './db/database.db'

# Deletar o arquivo do banco de dados
if os.path.exists(db_path):
    os.remove(db_path)
    print("Arquivo do banco de dados deletado com sucesso.")
else:
    print("O arquivo do banco de dados não existe.")