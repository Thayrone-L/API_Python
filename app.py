from flask import Flask, request, jsonify
from Negocios.FuncionarioNegocios import FuncionarioNegocios
from Dados.FuncionarioDados import _FuncionarioDados


app = Flask(__name__)

dados_funcionario = _FuncionarioDados()  # Certifique-se de ajustar conforme necessário
funcionario_negocios = FuncionarioNegocios(dados_funcionario)

# Endpoint para criar um usuário
@app.route('/funcionarios', methods=['POST'])
def criar_funcionario():
    try:
        dados = request.get_json()

        # Validar os dados de entrada
        if 'login' not in dados or 'senha' not in dados or 'nome_funcionario' not in dados or 'cpf' not in dados or 'perfil' not in dados:
            return jsonify({"erro": "Campos obrigatórios ausentes"}), 400

        resultado = funcionario_negocios.criar_funcionario(
            dados['login'],
            dados['senha'],
            dados['nome_funcionario'],
            dados['cpf'],
            dados['perfil']
        )

        return jsonify(resultado)

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Endpoint para obter um usuário por Login e senha
@app.route('/funcionarios/<string:login>/<string:senha>', methods=['GET'])
def login(login, senha):
    if not login or not senha:
            return jsonify({"erro": "Login e senha são obrigatórios."}),400
    resultado = funcionario_negocios.login(login, senha)
    return jsonify(resultado)


if __name__ == '__main__':
    app.run(debug=True)
