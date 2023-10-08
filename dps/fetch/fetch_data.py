import gzip
from io import BytesIO
import requests

class Fetch:
    def __init__(self) -> None:
        pass

    def fetch_data(self, url: str) -> str:

        response = requests.get(url)
        extracted_data = ""

        # Check if the download was successful (status code 200)
        if response.status_code == 200:
            # Step 2: Extract the contents of the gzip file in-memory
            with gzip.GzipFile(fileobj=BytesIO(response.content)) as f_in:
                extracted_data = f_in.read().decode('utf-8')  # Decode to string assuming it's text data

        else:
            print("Failed to download the gzip file. Enter a valid architecture.")

        
        return extracted_data