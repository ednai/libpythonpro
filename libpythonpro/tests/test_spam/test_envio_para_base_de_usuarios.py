from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Renzo', email='renzo@python.pro.br'),
            Usuario(nome='Luciano', email='renzo@python.pro.br')
        ],
        [
            Usuario(nome='Renzo', email='renzo@python.pro.br')

        ]
    ]

)
def test_qde_de_spam(sessao,usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso python Pro',
        'Confira os módulos fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count





def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@python.pro.br',
        'Curso python Pro',
        'Confira os módulos fantasticos'
    )
    enviador.enviar.assert_called_once_with (
        'luciano@python.pro.br',
        'renzo@python.pro.br',
        'Curso python Pro',
        'Confira os módulos fantasticos'

    )

# observaçao: ao importar a biblioteca Mock nao se faz necesario mais utilizar esse codigo ele foi substituido
#acima em ambos os testes so pelo Mock() advindo da biblioteca
# class EnviadorMock(Enviador):
#     def __init__(self):
#         super().__init__()
#         self.qtd_email_enviados =0
#         self.parametros_de_envio = None
#
#     def enviar(self, remetente, destinatario, assunto, corpo):
#         self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
#         self.qtd_email_enviados +=1
