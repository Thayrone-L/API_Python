import sys
sys.path.append(r'C:\Users\thayr\OneDrive\Documentos\repositorios\Python\Testes\API_Python')

from Dao.ConexaoSQL import ConexaoBanco
from Entidades.Usuario import Usuario

class _UsuarioDados:
    def __init__(self):
        self.conexao = ConexaoBanco()

    def inserir_usuario(self, usuario):
        try:
            self.conexao.conectar()
            parametros = (usuario.login, usuario.senha, usuario.nome_usuario, int(usuario.perfil))
            self.conexao.executar_procedure('InserirUsuario', parametros)
        except ValueError as ex:
            raise ValueError(f"Erro ao inserir usuário: {ex}")
        finally:
            self.conexao.fechar_conexao()
            
    def login (self, login, senha):
        try:
            self.conexao.conectar()
            parametros = (login, senha)
            resultado = self.conexao.executar_procedure('Login', parametros)
            return Usuario(*resultado[0]) if resultado else None
        except ValueError as ex:
            raise ValueError(f"Erro ao selecionar usuário por login e senha: {ex}")
        finally:
            self.conexao.fechar_conexao()


# Exportar a instância da classe interna
UsuarioDados = _UsuarioDados()
