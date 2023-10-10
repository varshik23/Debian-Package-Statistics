"""
Test the main module.
"""
from test.mock_response import MockResponse
import argparse
import requests

from dps.__main__ import get_top10_packages

# Initialize the arguments
arguments = argparse.Namespace()
arguments.arch = "amd64"
arguments.area = False
arguments.section = False
arguments.udeb = False
arguments.number = 10

def mock_get(*args, **kwargs):
    """
    Mock the requests.get function.
    """
    _ = args, kwargs # Ignore the arguments
    return MockResponse()

def test_get_top10_packages(monkeypatch):
    """
    Test the get_top10_packages function.
    """
    monkeypatch.setattr(requests, "get", mock_get)
    table, headers = get_top10_packages(arguments)
    assert len(table) == 9 and len(headers) == 3

def test_get_top10_packages_section(monkeypatch):
    """
    Test the get_top10_packages function in section mode.
    """
    monkeypatch.setattr(requests, "get", mock_get)
    arguments.section = True # Set the section argument to True
    table, headers = get_top10_packages(arguments)
    arguments.section = False # Set the section argument to False
    assert len(table) == 9 and len(headers) == 4

def test_get_top10_packages_area(monkeypatch):
    """
    Test the get_top10_packages function in area mode.
    """
    monkeypatch.setattr(requests, "get", mock_get)
    arguments.area = True
    table, headers = get_top10_packages(arguments)
    assert len(table) == 9 and len(headers) == 4

def test_get_top10_packages_section_area(monkeypatch):
    """
    Test the get_top10_packages function in section and area mode.
    """
    monkeypatch.setattr(requests, "get", mock_get)
    arguments.section = True
    arguments.area = True
    table, headers = get_top10_packages(arguments)
    assert len(table) == 9 and len(headers) == 5

def test_get_top_n_packages(monkeypatch):
    """
    Test the get_top_N_packages function with different values of n.
    """
    monkeypatch.setattr(requests, "get", mock_get)
    arguments.number = 5
    table, headers = get_top10_packages(arguments)
    assert len(table) == 5 and len(headers) == 5
    arguments.number = 20
    table, headers = get_top10_packages(arguments)
    assert len(table) == 9 and len(headers) == 5
