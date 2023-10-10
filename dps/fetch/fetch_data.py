"""
This module is used to fetch the data from the debian mirror.
"""
import gzip
from io import BytesIO
import sys
import requests

class Fetch:
    """
    This class is used to fetch the data from the debian mirror.
    """
    def __init__(self) -> None:
        """
        This function initializes the Fetch class.
        """

    def fetch_data(self, url: str) -> str:
        """
        This function fetches the data from the debian mirror.
        """
        try:
            response = requests.get(url, timeout=5) # Get the response from the server
            extracted_data = self.extract_data(response) # Extract the data from the gzip file
        except(): # If the server is not connected
            print("Failed to connect to the server. Check your internet connection")
            sys.exit(1) # Exit the program

        return extracted_data

    def extract_data(self, response: requests.models.Response) -> str:
        """
        This function extracts the data from the gzip file.
        """
        extracted_data = ""
        # Check if the response is valid
        if response.status_code != 200:
            print("Failed to download the gzip file. Enter a valid architecture.")
            sys.exit(1) # Exit the program

        with gzip.GzipFile(fileobj=BytesIO(response.content)) as f_in: # Extract the data
            extracted_data = f_in.read().decode('utf-8') # Decode the data
        return extracted_data
