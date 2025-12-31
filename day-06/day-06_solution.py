import argparse

class LogAnalyzer:
    def __init__(self, log_file):

        self.log_file = log_file
        self.counts = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0,
            "UNKNOWN": 0
        }

    def read_logs(self):
    
        try:
            with open(self.log_file, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            print("Log file not found:", self.log_file)
            return []
        
    def analyze(self, lines):

        for line in lines:
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1
            else:
                self.counts["UNKNOWN"] += 1

        return self.counts
    
def main():
    parser = argparse.ArgumentParser("Log Analyzer CLI Tool")
    parser.add_argument("--file", required=True)

    args = parser.parse_args()

    analyzer = LogAnalyzer(args.file)
    lines = analyzer.read_logs()

    if not lines:
        print("No log to analyze")

    result = analyzer.analyze(lines)
    print("Log Summary:")

    for level, count in result.items():
        print(level, ":", count)

if __name__ == "__main__":
    main()
