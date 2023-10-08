class Parser:
    def __init__(self) -> None:
        # self.packageData = {}
        self.NumberOfFilesInPackage = {}

    def parse_data(self, data: str) -> dict:
        for line in data.splitlines():
            if line:
                self.parse_line(line)
        return self.NumberOfFilesInPackage
    
    def parse_line(self, line: str) -> None:
        line = line.split()
        # fileName = line[-2]
        packages = line[-1].split(',')
        for package in packages:
            name = package.split('/')[-1]
            self.NumberOfFilesInPackage[name] = self.NumberOfFilesInPackage.get(name, 0) + 1