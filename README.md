# DPS
Debian Package Statistics
## Approach
### Modularization with Object-Oriented Programming:

* The primary approach behind creating this Python command-line tool is to follow object-oriented programming principles to modularize the code. 
* This modularization aims to enhance code maintainability and readability, as well as facilitate efficient testing and future expansions.

### Efficient Module Development:

* Rather than having a single monolithic script, the focus is on building a reusable module. This module encapsulates the functionality for downloading, decompressing, parsing, and processing the data efficiently. 
* The goal is to make it an efficient command-line tool that can be used without the need to run the entire script each time.

### Command-Line Input with argparse:

* To make the tool versatile and user-friendly, the Python argparse module is used for handling command-line input.
* The tool accepts command-line arguments such as architecture, section, area, udeb, and the number of top packages (K).
* `argparse` ensures that users can customize the tool's behavior without modifying the code. It also enforces input validation and provides clear usage instructions.
### Efficient Error Handling:
* Error handling is a crucial aspect of the tool's design. It ensures that users receive informative error messages in case of incorrect input or unexpected issues.
* `argparse` helps in performing initial input validation, such as checking whether the provided architectural specifications are valid and whether the number of top packages is a positive integer.
* Additional error handling mechanisms are implemented at various stages of data processing. For example, if the download of the .gz file fails or if the decompression encounters issues, appropriate error messages are displayed to guide the user.
### Download and Decompress Data:

* The initial step is to download the compressed .gz file from the Debian mirror using the `requests` library.
* The downloaded file is then decompressed using the `gzip` library. The resulting bytes data is converted to a string using the `BytesIO` class from the io module. This approach is chosen to optimize memory usage.
* The module returns the extracted data as a string for further processing.
### Data Parsing:

* The extracted string data is then parsed using a dedicated parser module. This parsing operation separates the data into two key objects.
* One object maintains a count of the number of files associated with each package, while the other keeps track of the section and area names for each package.
* The parser module returns both of these objects as a tuple, enabling efficient access to package-related information.
### Top K Packages:

* To identify the top K packages with the highest number of associated files, a sorting approach is employed.
* Instead of a standard sorting algorithm that would operate in O(nlogn) time complexity, `heapq.nlargest` is utilized. This function reduces the time complexity to O(n * log(K)), where n represents the total number of packages. Given that K is generally much smaller than n, this approach is more optimal.
### Tabulated Output:

* The final step involves presenting the results in an organized and visually appealing manner in the command line.
* This is accomplished using the Python library `tabulate`, which helps create well-formatted tables for the user to view.
## Time spent
### Project Planning and Design:

* 2-3 hours were dedicated to understanding the project requirements and planning the implementation strategy.
* Designing the modular structure, outlining functionality, and defining the object-oriented approach were critical aspects of this phase.
### Implementation and Code Development:

* 5-6 hours were spent on implementing the codebase.
* This phase involved writing and testing individual modules, such as downloading, decompression, parsing, and processing.
* Additionally, the integration of the argparse library for command-line input and error handling mechanisms were included during this phase.
### Testing and Debugging:

* 2-3 hours were allocated to thorough testing of the CLI tool.
* A combination of unit tests and integration tests ensured the reliability and correctness of the code.
* Debugging and addressing any issues discovered during testing were important to ensure the tool's robustness.
### Documentation and README Creation:

 * 2-3 hours were spent on creating documentation, including a detailed README file.
* The README includes information about the tool's usage instructions, and approach.

## Installation
<!-- #Please include instructions on how to install and run your code -->
**1. Clone the GitHub Repository:**

First, clone the GitHub repository to your local machine using the following command:
```bash
git clone https://github.com/varshik23/Debian-Package-Statistics.git
```
**2. Navigate to the Repository Directory:**

Change your current working directory to the cloned repository directory:

```bash
cd Debian-Package-Statistics
```
**3. Install Dependencies**

To install all the necessary dependencies, use pip and the requirements.txt file:

```bash
python3 -m venv ./venv
source ${PATH}/venv/bin/activate
python3 -m pip install -r requirements.txt
```

**4. Develop the Module**

Run the following command to develop the module using Python3:

```bash
python3 setup.py develop
```

## Usage
For the tool to work, you need to provide the architecture of the system. The tool accepts the following command-line arguments:

1. -h, --help: show the help message and exit
```
dps -h

usage: dps [options] architechture

Debian Package Statistics

positional arguments:
  arch                  architecture of the system

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -a, --area            show the archive area of the packages
  -s, --section         show section of the packages
  -u, --udeb            get udeb package
  -n [NUMBER], --number [NUMBER]
                        get the top n packages

Example: dps amd64, dps -a -s amd64, dps -u amd64
```
2. Provide the architecture of the system
```bash
dps amd64
```
3. -a, --area: show the archive area of the packages
```bash
dps -a amd64
```
4. -s, --section: show section of the packages
```bash
dps -s amd64
```
5. To get both area and section
```bash
dps -a -s amd64
```
6. -u, --udeb: get udeb package
```bash
dps -u amd64
```
7. -n [NUMBER], --number [NUMBER]: get the top n packages
```bash
dps -n 10 amd64
```
## Testing
To ensure the reliability and correctness of this command-line tool, you can run tests using the framework pytest. Follow these steps to run the tests:
```bash
pytest test
```
## Author
Varshik Sonti - [GitHub](varshik23) - [LinkedIn](https://www.linkedin.com/in/varshik-sonti/) - [Portfolio](https://varshik23.github.io/Portfolio/)

