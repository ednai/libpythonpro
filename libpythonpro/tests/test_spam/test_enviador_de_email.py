import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    #'remetente',
    ['foo@bar.com.br','edkujo@gmail.com']
)

def test_remetente(destinatario):
    enviador= Enviador()


    resultado=enviador.enviar(
         destinatario,
         'edsammarx@yahoo.com.br',
         'Cursos Python Pro',
         'Decima segunda  turma erle carrara aberta.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    #'destinatario',
    'remetente',
    ['','edkujo']
)

def test_remetente_invalido(remetente):
    enviador= Enviador()
    with pytest.raises(EmailInvalido):
       enviador.enviar(
            remetente,
            'edsammarx@yahoo.com.br',
            'Cursos Python Pro',
            'Decima segunda  turma erle carrara aberta.'
    )
