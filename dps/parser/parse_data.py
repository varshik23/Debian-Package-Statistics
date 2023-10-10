"""
This module parses the data.
"""
import sys
class Parser:
    """
    This class parses the data.
    """
    def __init__(self) -> None:
        """
        This function initializes the Parser class.
        """
        self.number_of_files = {} # {package_name: number_of_files}
        self.number_of_sections = {} # {package_name: (section, area)}

    def parse_data(self, data: str) -> tuple[dict, dict]:
        """
        This function parses the data.
        """
        if not data: # Check if the data is empty
            print("Error parsing Contents file")
            sys.exit(1) # Exit the program
        for line in data.splitlines(): # Split the data into lines
            if line:  # Check if the line is empty
                self.parse_line(line) # Parse the line
        return self.number_of_files, self.number_of_sections # Return the parsed data

    def parse_line(self, line: str) -> None:
        """
        This function parses the line.
        """
        line = line.split() # Split the line into words
        packages = line[-1].split(',') # Split the last word into packages
        try:
            for package in packages: # Iterate over the packages
                data = package.split('/') # Split the package into data
                if len(data) == 3: # Check if the package has area
                    area = data[0]
                else: # If the package doesn't have area
                    area = "Deprecated"
                section = data[-2] # Get the section of the package
                name = data[-1] # Get the name of the package
                if section not in self.number_of_sections:
                    self.number_of_sections[name] = (section, area) # Add the section to the dict
                self.number_of_files[name] = self.number_of_files.get(name, 0) + 1
        except():
            print("Error parsing Contents file") # Print error message
            sys.exit(1) # Exit the program
