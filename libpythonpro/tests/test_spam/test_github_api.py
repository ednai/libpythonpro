from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/47866756?v=4'
    resp_mock.json.return_value = {
        'login': 'ednai', 'id': 47866756, 'node_id': 'MDQ6VXNlcjQ3ODY2NzU2',
        'avatar_url': url,
    }
    get_mock=mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url




def test_buscar_avatar(avatar_url):
    url=github_api.buscar_avatar('ednai'
                                 )
    assert avatar_url ==url



def test_buscar_avatar_integracao():

    url=github_api.buscar_avatar('edna')
    assert 'https://avatars.githubusercontent.com/u/328600?v=4'==url