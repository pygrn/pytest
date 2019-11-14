
from urllib.parse import urljoin

import pytest
import requests


@pytest.mark.functional
def test_api_ng_programs(live_server):
    url = urljoin(live_server.url, '/api/v1/groups/')
    r = requests.get(url)

    assert r.status_code == 200
    response = r.json()
