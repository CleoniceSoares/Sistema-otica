import sqlite3

conn = sqlite3.connect('Otica.db')

cursor = conn.cursor()

# tabela cargo
cursor.execute("""
	CREATE TABLE tb_cargo(
	id_cargo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(45) NOT NULL
	);
""")

# tabela funcionário
cursor.execute("""
	CREATE TABLE tb_funcionario(
	id_funcionario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(45) NOT NULL,
    usuario VARCHAR(45) NOT NULL,
    senha VARCHAR(45) NOT NULL,
    id_cargo INTEGER NOT NULL
	);
""")

# tabela cliente
cursor.execute("""
    CREATE TABLE tb_cliente(
    id_cliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(45) NOT NULL,
    apelido VARCHAR(45) NOT NULL,
    endereco VARCHAR(45) NOT NULL,
    cpf NUMERIC(11) NOT NULL
    );
""")

# tabela médico
cursor.execute("""
    CREATE TABLE tb_medico(
    id_medico INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(45) NOT NULL,
    crm VARCHAR(15) NOT NULL
    );
""")

# tabela lente
cursor.execute("""
    CREATE TABLE tb_lente(
    id_lente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(45) NOT NULL,
    material VARCHAR(45) NOT NULL,
    valor NUMERIC(10,2),
    tamanho VARCHAR(45) NOT NULL,
    tipo VARCHAR(45) NOT NULL
    );
""")

# tabela armação
cursor.execute("""
    CREATE TABLE tb_armacao(
    id_armacao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(45) NOT NULL,
    material VARCHAR(45) NOT NULL,
    valor NUMERIC(10,2),
    tamanho VARCHAR(45) NOT NULL,
    tipo_aro VARCHAR(45) NOT NULL
    );
""")

# tabela venda
cursor.execute("""
    CREATE TABLE tb_venda(
    id_venda INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    data DATE NOT NULL,
    id_lente INTEGER,
    id_armacao INTEGER,
    valor_total NUMERIC(10,2)
    );
""")

# tabela agendamento
cursor.execute("""
    CREATE TABLE tb_agendamento(
    id_agendamento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    data DATE NOT NULL,
    valor NUMERIC(10,2)
    );
""")

# tabela consulta
cursor.execute("""
    CREATE TABLE tb_consulta(
    id_consulta INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    id_medico INTEGER NOT NULL,
    data DATE NOT NULL
    );
""")

# tabela medição longe
cursor.execute("""
    CREATE TABLE tb_longe(
    id_longe INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    olho_direito_esferico VARCHAR(45) NOT NULL,
    olho_direito_cilindrico VARCHAR(45) NOT NULL,
    olho_direito_eixo VARCHAR(45) NOT NULL,
    olho_direito_dp VARCHAR(45) NOT NULL,
    olho_esquerdo_esferico VARCHAR(45) NOT NULL,
    olho_esquerdo_cilindrico VARCHAR(45) NOT NULL,
    olho_esquerdo_eixo VARCHAR(45) NOT NULL,
    olho_esquerdo_dp VARCHAR(45) NOT NULL
    );
""")

# tabela medição perto
cursor.execute("""
    CREATE TABLE tb_perto(
    id_perto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    olho_direito_esferico VARCHAR(45) NOT NULL,
    olho_direito_cilindrico VARCHAR(45) NOT NULL,
    olho_direito_eixo VARCHAR(45) NOT NULL,
    olho_direito_dp VARCHAR(45) NOT NULL,
    olho_esquerdo_esferico VARCHAR(45) NOT NULL,
    olho_esquerdo_cilindrico VARCHAR(45) NOT NULL,
    olho_esquerdo_eixo VARCHAR(45) NOT NULL,
    olho_esquerdo_dp VARCHAR(45) NOT NULL
    );
""")

# tabela prescrição
cursor.execute("""
    CREATE TABLE tb_prescricao(
    id_prescricao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_paciente VARCHAR(45) NOT NULL,
    lente VARCHAR(45) NOT NULL,
    id_longe NUMERIC NOT NULL,
    id_perto NUMERIC NOT NULL,
    observacao VARCHAR(150) NOT NULL,
    id_medico INTEGER NOT NULL
    );
""")

print ("Tabelas criadas com sucesso!")
conn.close()
