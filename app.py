from flask import Flask, request, jsonify
from Negocios.UsuarioNegocios import UsuarioNegocios
from Dados.UsuarioDados import _UsuarioDados


app = Flask(__name__)

dados_usuario = _UsuarioDados()  # Certifique-se de ajustar conforme necessário
usuario_negocios = UsuarioNegocios(dados_usuario)

# Endpoint para criar um usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    try:
        dados = request.get_json()

        # Validar os dados de entrada
        if 'login' not in dados or 'senha' not in dados or 'nome_usuario' not in dados or 'cpf' not in dados or 'perfil' not in dados:
            return jsonify({"erro": "Campos obrigatórios ausentes"}), 400

        resultado = usuario_negocios.criar_usuario(
            dados['login'],
            dados['senha'],
            dados['nome_usuario'],
            dados['cpf'],
            dados['perfil']
        )

        return jsonify(resultado)

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Endpoint para obter um usuário por Login e senha
@app.route('/usuarios/<string:login>/<string:senha>', methods=['GET'])
def login(login, senha):
    if not login or not senha:
            return jsonify({"erro": "Login e senha são obrigatórios."}),400
    resultado = usuario_negocios.login(login, senha)
    return jsonify(resultado)


if __name__ == '__main__':
    app.run(debug=True)
