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
            parametros = (usuario.login, usuario.senha, usuario.nome_usuario, usuario.cpf ,int(usuario.perfil))
            self.conexao.executar_procedure('InserirUsuario', parametros)
            self.conexao.cursor.commit()        
        except ValueError as ex:
            raise ValueError(f"Erro ao inserir usuário: {ex}")
        finally:
            self.conexao.fechar_conexao()
            
    def login(self, login, senha):
        try:
            self.conexao.conectar()
            parametros = (login, senha)
            resultado = self.conexao.executar_procedure('Login', parametros)
            
            if resultado and len(resultado) > 0:
                usuario_data = resultado[0]

                if len(usuario_data) >= 3:
                    usuario = Usuario(
                    login=login,
                    senha=senha,
                    nome_usuario=usuario_data[0],
                    perfil=usuario_data[1],
                    cpf_param=usuario_data[2]
                )
                    return usuario
                else:
                    return None
            else:
                return None
        except ValueError as ex:
            raise ValueError(f"Erro ao selecionar usuário por login e senha: {ex}")
        finally:
            self.conexao.fechar_conexao()

# Exportar a instância da classe interna
UsuarioDados = _UsuarioDados()
