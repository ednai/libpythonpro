import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    #fase de SETUP
    conexao_obj = Conexao()
    yield conexao_obj  #yield é uma funcao geradora
    # fase de TEAR DOWN
    conexao_obj.fechar()


@pytest.fixture()
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back() #desfaz todas as operacoe ja feita ao terminar a sessao
    sessao_obj.fechar()