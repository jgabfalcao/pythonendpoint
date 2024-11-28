#Objetivo
#URL Base
#Endpoints
#Quais Recursos
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': "O Senhor dos Aneis",
        'autor' : "João"
    },
    {
        'id': 2,
        'titulo': "Diario de um Banana",
        'autor' : "Pedro"
    },
    {
        'id': 3,
        'titulo': "Cinderela",
        'autor' : "Fabricio"
    },
]

@app.route('/livros', methods=['GET'])
def obterLivros():
    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])
def obterLivrosPorId(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        else:
            return make_response(jsonify("Livro inexistente"), 404)

@app.route('/livros/<int:id>', methods=['PUT'])
def editarLivroPorID(id):
    livroAlterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livroAlterado)
            return jsonify(livros[indice])
        
@app.route('/livros', methods=['POST'])
def incluirNovoLivro():
    novoLivro = request.get_json()
    livros.append(novoLivro)

    return jsonify(livros)

app.run(port=5000, host="localhost",debug=True)