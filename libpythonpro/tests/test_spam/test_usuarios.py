from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario= Usuario(nome='Renzo',email='renzo@python.pro.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios=[
        Usuario(nome='Renzo', email='renzo@python.pro.br'),
        Usuario(nome='Luciano', email='renzo@python.pro.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()





# from libpythonpro.spam.db import Conexao
# from libpythonpro.spam.modelos import Usuario
#
# def conexao():
#     return conexao
#
#
# def test_salvar_usuario():
#     conexao = Conexao()
#     sessao = conexao.gerar_sessao()
#     usuario= Usuario(nome='Renzo')
#     sessao.salvar(usuario)
#     assert isinstance(usuario.id, int)
#     sessao.roll_back() #desfaz todas as operacoe ja feita ao terminar a sessao
#     sessao.fechar()
#     conexao.fechar()
#
#
# def test_listar_usuario():
#     conexao = Conexao()
#     sessao = conexao.gerar_sessao()
#     usuarios=[Usuario(nome='Renzo'), Usuario(nome='Luciano')]
#     for usuario in usuarios:
#         sessao.salvar(usuario)
#     assert usuarios == sessao.listar()
#     sessao.roll_back() # teardown -desfaz todas as operacoe ja feita ao terminar a sessao
#     sessao.fechar() #teardown  encerrarmento da sessao
#     conexao.fechar() #teardown  encerrarmento da conexao
