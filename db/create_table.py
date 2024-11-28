import sqlite3
import pandas as pd

# Caminho do arquivo e nome do banco de dados
file_path = './xlsx/dados_filtrados_por_trimestre_PIB_ED.xlsx'
db_path = './db/database.db'

# Carregar os dados do Excel
df = pd.read_excel(file_path, sheet_name='dados_filtrados_por_trimestre_P')

# Conectar ao banco de dados SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Criar as tabelas PIB e Investimento
cursor.execute('''
CREATE TABLE IF NOT EXISTS PIB (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    periodo TEXT UNIQUE NOT NULL,
    valor REAL NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Investimento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    periodo TEXT NOT NULL,
    valor REAL NOT NULL,
    subcategoria TEXT NOT NULL,
    FOREIGN KEY (periodo) REFERENCES PIB(periodo)
);
''')

print("Tables created successfully.")

# Inserir dados na tabela PIB
pib_data = df[['Periodo', 'Valor']].drop_duplicates().dropna()
pib_data.columns = ['periodo', 'valor']  # Renomear colunas para consistência

for _, row in pib_data.iterrows():
    cursor.execute("INSERT OR IGNORE INTO PIB (periodo, valor) VALUES (?, ?)", (row['periodo'], row['valor']))

# Inserir dados na tabela Investimento
investimento_data = df[['Período', 'Valor Pago', 'Subfunção']].dropna()
investimento_data.columns = ['periodo', 'valor', 'subcategoria']  # Renomear colunas para consistência

for _, row in investimento_data.iterrows():
    cursor.execute("INSERT INTO Investimento (periodo, valor, subcategoria) VALUES (?, ?, ?)", 
                   (row['periodo'], row['valor'], row['subcategoria']))

# Confirmar mudanças e fechar a conexão
conn.commit()
print("Data inserted successfully.")
conn.close()
