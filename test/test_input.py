"""
This file contains tests for the input validation of the CLI.
"""
import subprocess

def test_invalid_cli_input():
    """
    This function tests the CLI with invalid input.
    """
    assert subprocess.run(["python", "-m", "dps", "-a", "abc"], check = False).returncode == 2
    assert subprocess.run(["python", "-m", "dps", "-s", "abc"], check = False).returncode == 2
    assert subprocess.run(["python", "-m", "dps", "-n", "abc"], check = False).returncode == 2
    assert subprocess.run(["python", "-m", "dps", "-a", "-s"], check = False).returncode == 2
    assert subprocess.run(["python", "-m", "dps", "-a", "-n"], check = False).returncode == 2
    assert subprocess.run(["python", "-m", "dps", "-s", "-n"], check = False).returncode == 2
    assert subprocess.run(["python", "-m", "dps", "-a", "-s", "-n"], check = False).returncode == 2
    assert subprocess.run(["python", "-m", "dps", "-a", "-k", "abc"], check = False).returncode == 2
