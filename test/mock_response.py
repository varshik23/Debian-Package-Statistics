"""
This module contains the MockResponse class for mocking requests.get() response
"""
import io
import gzip
from test.mock_data import INPUT_DATA as data

class MockResponse:
    """
    MockResponse class for mocking requests.get() response
    """
    @property
    def content(self):
        """
        This function returns the content of the mock response
        """
        compressed_data = io.BytesIO()
        with gzip.GzipFile(fileobj=compressed_data, mode='wb') as f:
            f.write(data)
        return compressed_data.getvalue()

    @property
    def status_code(self):
        """
        This function returns the status code of the mock response
        """
        return 200
