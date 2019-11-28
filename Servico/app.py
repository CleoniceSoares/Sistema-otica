# importações
from flask import Flask
from flask import request
from flask import jsonify
from flask_json_schema import JsonSchema, JsonValidationError
from flask_cors import CORS
import logging
import sqlite3

app = Flask(__name__)

# Logging
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("oticaapp.log")
handler.setFormatter(formatter)
logger = app.logger
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# validação
schema = JsonSchema()
schema.init_app(app)

cargo_schema = {
    "required": ["nome"],
    "properties": {
        "nome" : {"type" : "string"}
    }
}

funcionario_schema = {
    "required": ["nome", "usuario", "senha", "id_cargo"],
    "properties": {
        "nome" : {"type" : "string"},
        "usuario" : {"type" : "string"},
        "senha" : {"type" : "string"},
        "id_cargo" : {"type" : "integer"}
    }
}

cliente_schema = {
    "required": ["nome", "apelido", "endereco", "cpf"],
    "properties": {
        "nome" : {"type" : "string"},
        "apelido" : {"type" : "string"},
        "endereco" : {"type" : "string"},
        "cpf" : {"type" : "integer"}
    }
}

medico_schema = {
    "required": ["nome", "crm"],
    "properties": {
        "nome" : {"type" : "string"},
        "crm" : {"type" : "string"}
    }
}

lente_schema = {
    "required": ["nome", "material", "valor", "tamanho", "tipo_aro"],
    "properties": {
        "nome" : {"type" : "string"},
        "material" : {"type" : "string"},
        "valor" : {"type" : "integer"},
        "tamanho" : {"type" : "string"},
        "tipo_aro" : {"type" : "string"}
    }
}

DATABASE_NAME = "Otica.db"

# cadastrar cargo
@app.route("/cargo", methods = ["POST"])
@schema.validate(cargo_schema)
def setCargo():
    logger.info("Cadastrando cargo.")
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cargo = request.get_json()
        nome = cargo["nome"]

        cursor.execute("""
            insert into tb_cargo(nome)
            values(?);
        """, (nome, ))
        conn.commit()
        id = cursor.lastrowid
        cargo["id"] = id
    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)
    finally:
        if conn:
            conn.close()
    logger.info("Cargo cadastrado com sucesso.")
    return jsonify(cargo)

# cadastrar funcionario
@app.route("/funcionario", methods = ["POST"])
@schema.validate(funcionario_schema)
def setFuncionario():
    logger.info("Cadastrando funcionario.")
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        funcionario = request.get_json()
        nome = funcionario["nome"]
        usuario = funcionario["usuario"]
        senha = funcionario["senha"]
        id_cargo = funcionario["id_cargo"]

        cursor.execute("""
            insert into tb_funcionario(nome, usuario, senha, id_cargo)
            values(?, ?, ?, ?);
        """, (nome, usuario, senha, id_cargo))
        conn.commit()
        id = cursor.lastrowid
        funcionario["id"] = id
    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)
    finally:
        if conn:
            conn.close()
    logger.info("Funcionario cadastrado com sucesso.")
    return jsonify(funcionario)

# cadastrar cliente
@app.route("/cliente", methods = ["POST"])
@schema.validate(cliente_schema)
def setCliente():
    logger.info("Cadastrando cliente.")
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cliente = request.get_json()
        nome = cliente["nome"]
        apelido = cliente["apelido"]
        endereco = cliente["endereco"]
        cpf = cliente["cpf"]

        cursor.execute("""
            insert into tb_cliente(nome, apelido, endereco, cpf)
            values(?, ?, ?, ?);
        """, (nome, apelido, endereco, cpf))
        conn.commit()
        id = cursor.lastrowid
        cliente["id"] = id
    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)
    finally:
        if conn:
            conn.close()
    logger.info("Cliente cadastrado com sucesso.")
    return jsonify(cliente)

# cadastrar medico
@app.route("/medico", methods = ["POST"])
@schema.validate(medico_schema)
def setMedico():
    logger.info("Cadastrando medico.")
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        medico = request.get_json()
        nome = medico["nome"]
        crm = medico["crm"]

        cursor.execute("""
            insert into tb_medico(nome, crm)
            values(?, ?);
        """, (nome, crm))
        conn.commit()
        id = cursor.lastrowid
        medico["id"] = id
    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)
    finally:
        if conn:
            conn.close()
    logger.info("Médico cadastrado com sucesso.")
    return jsonify(medico)

# cadastrar lente
@app.route("/lente", methods = ["POST"])
@schema.validate(lente_schema)
def setLente():
    logger.info("Cadastrando lente.")
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        lente = request.get_json()
        nome = lente["nome"]
        material = lente["material"]
        valor = lente["valor"]
        tamanho = lente["tamanho"]
        tipo = lente["tipo"]

        cursor.execute("""
            insert into tb_lente(nome, material, valor, tamanho, tipo)
            values(?, ?, ?, ?, ?);
        """, (nome, material, valor, tamanho, tipo))
        conn.commit()
        id = cursor.lastrowid
        lente["id"] = id
    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)
    finally:
        if conn:
            conn.close()
    logger.info("Lente cadastrada com sucesso.")
    return jsonify(lente)

# cadastrar armação
@app.route("/armacao", methods = ["POST"])
@schema.validate(armacao_schema)
def setArmacao():
    logger.info("Cadastrando armação.")
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        armacao = request.get_json()
        nome = armacao["nome"]
        material = armacao["material"]
        valor = armacao["valor"]
        tamanho = armacao["tamanho"]
        tipo_aro = armacao["tipo_aro"]

        cursor.execute("""
            insert into tb_armacao(nome, material, valor, tamanho, tipo_aro)
            values(?, ?, ?, ?, ?);
        """, (nome, material, valor, tamanho, tipo_aro))
        conn.commit()
        id = cursor.lastrowid
        armacao["id"] = id
    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)
    finally:
        if conn:
            conn.close()
    logger.info("Armação cadastrado com sucesso.")
    return jsonify(armacao)

# realizar venda
@app.route("/venda", methods = ["POST"])
@schema.validate(venda_schema)
def setVenda():
    logger.info("Realizando venda.")
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        venda = request.get_json()
        data = venda["data"]
        id_lente = venda["id_lente"]
        id_armacao = venda["id_armacao"]

        cursor.execute("""
            insert into tb_venda(data, id_lente, id_armacao)
            values(?, ?, ?);
        """, (data, id_lente, id_armacao))
        conn.commit()
        id = cursor.lastrowid
        venda["id"] = id
    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)
    finally:
        if conn:
            conn.close()
    logger.info("Venda realizada com sucesso.")
    return jsonify(venda)

# realizar agendamento
@app.route("/agendamento", methods = ["POST"])
@schema.validate(agendamento_schema)
def setAgendamento():
    logger.info("Realizando agendamento.")
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        agendamento = request.get_json()
        id_cliente = agendamento["id_cliente"]
        id_medico = agendamento["id_medico"]
        data = agendamento["data"]

        cursor.execute("""
            insert into tb_agendamento(id_cliente, id_medico, data)
            values(?, ?, ?);
        """, (id_cliente, id_medico, data))
        conn.commit()
        id = cursor.lastrowid
        agendamento["id"] = id
    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)
    finally:
        if conn:
            conn.close()
    logger.info("Agendamento realizada com sucesso.")
    return jsonify(agendamento)

# realizar consulta
@app.route("/consulta", methods = ["POST"])
@schema.validate(consulta_schema)
def setConsulta():
    logger.info("Realizando consulta.")
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        consulta = request.get_json()
        id_cliente = consulta["id_cliente"]
        id_medico = consulta["id_medico"]
        data = consulta["data"]

        cursor.execute("""
            insert into tb_consulta(id_cliente, id_medico, data)
            values(?, ?, ?);
        """, (id_cliente, id_medico, data))
        conn.commit()
        id = cursor.lastrowid
        consulta["id"] = id
    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)
    finally:
        if conn:
            conn.close()
    logger.info("Consulta realizada com sucesso.")
    return jsonify(consulta)

# realizar medição para longe
@app.route("/longe", methods = ["POST"])
@schema.validate(longe_schema)
def setLonge():
    logger.info("Realizando medição para longe.")
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        longe = request.get_json()
        olho_direito_esferico = longe["olho_direito_esferico"]
        olho_direito_cilindrico = longe["olho_direito_cilindrico"]
        olho_direito_eixo = longe["olho_direito_eixo"]
        olho_direito_dp = longe["olho_direito_dp"]
        olho_esquerdo_esferico = longe["olho_esquerdo_esferico"]
        olho_esquerdo_cilindrico = longe["olho_esquerdo_cilindrico"]
        olho_esquerdo_eixo = longe["olho_esquerdo_eixo"]
        olho_esquerdo_dp = longe["olho_esquerdo_dp"]

        cursor.execute("""
            insert into tb_longe(olho_direito_esferico, olho_direito_cilindrico,
            olho_direito_eixo, olho_direito_dp, olho_esquerdo_esferico, olho_esquerdo_cilindrico, olho_esquerdo_eixo, olho_esquerdo_dp)
            values(?, ?, ?, ?, ?, ?, ?, ?);
        """, (olho_direito_esferico, olho_direito_cilindrico, olho_direito_eixo, olho_direito_dp, olho_esquerdo_esferico, olho_esquerdo_cilindrico, olho_esquerdo_eixo, olho_esquerdo_dp))
        conn.commit()
        id = cursor.lastrowid
        longe["id"] = id
    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)
    finally:
        if conn:
            conn.close()
    logger.info("Medição para longe realizada com sucesso.")
    return jsonify(longe)

# realizar medição para perto
@app.route("/perto", methods = ["POST"])
@schema.validate(perto_schema)
def setPerto():
    logger.info("Realizando medição para perto.")
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        perto = request.get_json()
        olho_direito_esferico = perto["olho_direito_esferico"]
        olho_direito_cilindrico = perto["olho_direito_cilindrico"]
        olho_direito_eixo = perto["olho_direito_eixo"]
        olho_direito_dp = perto["olho_direito_dp"]
        olho_esquerdo_esferico = perto["olho_esquerdo_esferico"]
        olho_esquerdo_cilindrico = perto["olho_esquerdo_cilindrico"]
        olho_esquerdo_eixo = perto["olho_esquerdo_eixo"]
        olho_esquerdo_dp = perto["olho_esquerdo_dp"]

        cursor.execute("""
            insert into tb_perto(olho_direito_esferico, olho_direito_cilindrico,
            olho_direito_eixo, olho_direito_dp, olho_esquerdo_esferico, olho_esquerdo_cilindrico, olho_esquerdo_eixo, olho_esquerdo_dp)
            values(?, ?, ?, ?, ?, ?, ?, ?);
        """, (olho_direito_esferico, olho_direito_cilindrico, olho_direito_eixo, olho_direito_dp, olho_esquerdo_esferico, olho_esquerdo_cilindrico, olho_esquerdo_eixo, olho_esquerdo_dp))
        conn.commit()
        id = cursor.lastrowid
        perto["id"] = id
    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)
    finally:
        if conn:
            conn.close()
    logger.info("Medição para perto realizada com sucesso.")
    return jsonify(perto)

# realizar prescrição
@app.route("/prescricao", methods = ["POST"])
@schema.validate(prescricao_schema)
def setPrescricao():
    logger.info("Realizando prescrição.")
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        prescricao = request.get_json()
        id_cliente = prescricao["id_cliente"]
        lente = prescricao["lente"]
        id_longe = prescricao["id_longe"]
        id_perto = prescricao["id_perto"]
        observacao = prescricao["observacao"]
        id_medico = prescricao["id_medico"]

        cursor.execute("""
            insert into tb_prescricao(id_cliente, lente, id_longe, id_perto, observacao, id_medico)
            values(?, ?, ?, ?, ?, ?);
        """, ())
        conn.commit()
        id = cursor.lastrowid
        prescricao["id"] = id
    except(sqlite3.Error, Exception) as e:
        logger.error("Aconteceu um erro.")
        logger.error("Exceção: %s" % e)
    finally:
        if conn:
            conn.close()
    logger.info("Prescrição realizada com sucesso.")
    return jsonify(prescricao)
