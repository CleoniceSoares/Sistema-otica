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
