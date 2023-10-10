"""
Test the fetch module.
"""
from test.mock_response import MockResponse
import subprocess
import pytest
import requests
from dps.fetch import Fetch

def mock_get(*args, **kwargs):
    """
    This function mocks the requests.get() function.
    """
    _ = args, kwargs
    return MockResponse()

def test_fetch(monkeypatch):
    """
    This function tests the fetch module.
    """
    monkeypatch.setattr(requests, "get", mock_get)
    fetch = Fetch()
    url = "http://ftp.uk.debian.org/debian/dists/stable/main/Contents-amd64.gz"
    data = fetch.fetch_data(url)
    assert len(data) == 1464

def test_fetch_invalid_arch():
    """
    This function tests the fetch module with an invalid architecture.
    """
    assert subprocess.run(["python", "-m", "dps", "abc"], check = False).returncode == 2

def test_fetch_invalid_arch_udeb():
    """
    This function tests the fetch module with an invalid udeb architecture.
    """
    assert subprocess.run(["python", "-m", "dps", "-u", "abc"], check = False).returncode == 2

def test_fetch_invalid_url():
    """
    This function tests the fetch module with an invalid url.
    """
    fetch = Fetch()
    url = "http://ftp.uk.debian.org/debian/dists/stable/main/Contents-amd64"
    with pytest.raises(SystemExit) as exc_info:
        fetch.fetch_data(url)
    assert exc_info.value.code == 1
