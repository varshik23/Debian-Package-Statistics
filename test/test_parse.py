"""
Test the parser module.
"""
from test.mock_data import INPUT_DATA as DATA
import pytest
from dps.parser import Parser

DATA = DATA.decode("utf-8")

def test_parse():
    """
    Test the parse function.
    """
    parser = Parser()
    packages, sections = parser.parse_data(DATA)
    assert len(packages) == 9 and len(sections) == 9
    assert packages["abpoa"] == 7
    assert sections["abpoa"] == ("science", "Deprecated")

def test_parse_invalid_data_line():
    """
    Test the parse function with invalid data line.
    """
    parser = Parser()
    with pytest.raises(IndexError):
        parser.parse_line("invalid data line")
    with pytest.raises(SystemExit):
        parser.parse_data("")

def test_multiple_packages():
    """
    Test the parse function with multiple packages.
    """
    parser = Parser()
    packages,_ = parser.parse_data(DATA)
    assert "bzip2" in packages
    assert "bzip2-static" in packages
    assert "bzip2-mt" in packages
