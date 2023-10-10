"""
This module is the entry point of the program.
"""
import heapq
import argparse
from tabulate import tabulate
from dps.fetch import Fetch
from dps.parser import Parser


ARC = ["all", "amd64", "arm64", "armel", "armhf",
    "i386", "mips64el", "mipsel", "ppc64el", "s390x"] # List of architectures

def get_top10_packages(args: argparse.Namespace) -> tuple[list, list]:
    """
    This function returns the top 10 packages from the mirror.
    """
    mirror_url = "http://ftp.uk.debian.org/debian/dists/stable/main/" # URL of the mirror
    fetch = Fetch() # Create an instance of the Fetch class
    parser = Parser() # Create an instance of the Parser class

    if args.udeb: # If the user wants to get udeb packages
        mirror_url += "Contents-udeb-" + args.arch + ".gz"
    else:
        mirror_url += "Contents-" + args.arch + ".gz"

    data = fetch.fetch_data(mirror_url) # Fetch the data from the mirror
    packages, sections = parser.parse_data(data) # Parse the data

    table = heapq.nlargest(args.number,
            packages.items(),
            key = lambda x: x[1]) # Get the top n packages

    headers = ["No.", "Package Name", "Number of Files"] # Initialize the headers

    for i,val in enumerate(table): # Iterate through the table
        table[i] = (i+1,) + val # Add the index
        if args.section: # If the user wants to get the section of the packages
            if i == 0:
                headers.append("Section") # Add the section header
            table[i] = table[i] + (sections[table[i][1]][0],) # Add the section to the table
        if args.area: # If the user wants to get the area of the packages
            if i == 0:
                headers.append("Area") # Add the area header
            table[i] = table[i] + (sections[table[i][1]][1],) # Add the area to the table

    return table, headers # Return the table and headers

def main() -> None:
    """
    This function is the entry point of the program.
    """
    parsed_args = argparse.ArgumentParser(description="Debian Package Statistics",
                                          usage = "%(prog)s [options] architechture",
                                          epilog=
                                          """
                                          Example: %(prog)s amd64, %(prog)s -a -s amd64
                                          """) # Initialize the parser
    parsed_args.add_argument("arch", metavar="arch", type=str, choices=ARC,
                            help="architecture of the system") # Add the architecture argument
    parsed_args.add_argument("-v", "--version", action="version",
                            version="%(prog)s 0.1.0") # Add the version argument
    parsed_args.add_argument("-a", "--area", action="store_true",
                            help="show the archive area of the packages") # Add the area argument
    parsed_args.add_argument("-s", "--section", action="store_true",
                            help="show section of the packages") # Add the section argument
    parsed_args.add_argument("-u", "--udeb", action="store_true",
                            help="get udeb package") # Add the udeb argument
    parsed_args.add_argument("-n", "--number", type=int, default=10,
                            nargs='?', help="get the top n packages") # Add the number argument
    args = parsed_args.parse_args() # Parse the arguments
    table, headers = get_top10_packages(args) # Get the table and headers
    print(tabulate(table, headers)) # Print the tables

if __name__ == "__main__":
    main()
