import sys
import heapq
from dps.fetch import Fetch
from dps.parser import Parser
from dps.print import Print

def vaidate_input(args):
    pass

def main():
    path = "http://ftp.uk.debian.org/debian/dists/stable/main/"
    args = sys.argv[1:]
    if len(args) > 1:
        print("Too many arguments. Type 'dps' for help.")
        sys.exit(1)
    elif len(args) == 0:
        p = Print()
        p.print_desc()
        sys.exit(1)
    else:
        arc = sys.argv[1]
        fetch = Fetch()
        parser = Parser()
        data = fetch.fetch_data(path + "Contents-" + arc + ".gz")
        packages = parser.parse_data(data)
        top_10 = heapq.nlargest(10, packages.items(), key = lambda x: x[1])
        for i in range(len(top_10)):
            print(i + 1, '.', top_10[i][0], ":", top_10[i][1])
    
if __name__ == "__main__":
    main()