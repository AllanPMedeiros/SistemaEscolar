from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/alunos', methods=['POST'])
@swag_from({
    'tags': ['Alunos'],
    'description': 'Cria um novo aluno.',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'aluno_id': {'type': 'string'},
                'nome': {'type': 'string'},
                'endereco': {'type': 'string'},
                'cidade': {'type': 'string'},
                'estado': {'type': 'string'},
                'cep': {'type': 'string'},
                'pais': {'type': 'string'},
                'telefone': {'type': 'string'}
            },
            'example': {
                'aluno_id': '123',
                'nome': 'João Silva',
                'endereco': 'Rua A, 123',
                'cidade': 'São Paulo',
                'estado': 'SP',
                'cep': '01000-000',
                'pais': 'Brasil',
                'telefone': '(11) 99999-9999'
            }
        }
    }],
    'responses': {
        201: {'description': 'Aluno criado com sucesso'},
        400: {'description': 'Erro na requisição'}
    }
})
def create_aluno():
    data = request.get_json()
    # Lógica de inserção fictícia para documentação
    return jsonify({"message": "Aluno criado com sucesso"}), 201


@app.route('/alunos/<string:aluno_id>', methods=['GET'])
@swag_from({
    'tags': ['Alunos'],
    'description': 'Busca um aluno pelo ID.',
    'parameters': [{
        'name': 'aluno_id',
        'in': 'path',
        'required': True,
        'type': 'string'
    }],
    'responses': {
        200: {
            'description': 'Dados do aluno',
            'examples': {
                'application/json': {
                    "aluno_id": "123",
                    "nome": "João Silva",
                    "endereco": "Rua A, 123",
                    "cidade": "São Paulo",
                    "estado": "SP",
                    "cep": "01000-000",
                    "pais": "Brasil",
                    "telefone": "(11) 99999-9999"
                }
            }
        },
        404: {'description': 'Aluno não encontrado'}
    }
})
def read_aluno(aluno_id):
    return jsonify({
        "aluno_id": aluno_id,
        "nome": "João Silva",
        "endereco": "Rua A, 123",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01000-000",
        "pais": "Brasil",
        "telefone": "(11) 99999-9999"
    }), 200

# Similar structure can be copied for:
# - /turmas
# - /professores
# - /pagamentos
# - /presencas
# - /atividades
# - /atividades_alunos
# - /usuarios

# A rota raiz para Swagger UI
@app.route('/')
def docs_redirect():
    return jsonify({"message": "Acesse a documentação em /apidocs/"}), 200

if __name__ == '__main__':
    app.run(debug=True)
