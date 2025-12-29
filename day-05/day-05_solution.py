import json

class LogAnalyze:

  def __init__(self, file_name, output_file):
     
     self.file_name = file_name
     self.output_file = output_file

  def read_logs(self):   
    try:
      with open(self.file_name,"r") as file:
        lines = file.readlines()

      if not lines:
        print("log file is empty")

      return lines
    
    except FileNotFoundError:
      print("file is does not exist")
      return []
    
  def write_json(self, counts):
      with open(self.output_file, "w") as f:
        json.dump(counts, f)    
    
  def analyze(self):
    log_count = {
                "INFO": 0,
                "WARNING": 0,
                "ERROR": 0
                }
    lines = self.read_logs()
    
    for line in lines:
        if "INFO" in line:
            log_count["INFO"] += 1
        elif "WARNING" in line:
            log_count["WARNING"] += 1
        elif "ERROR" in line:
            log_count["ERROR"] += 1
        else:
          pass
    self.write_json(log_count)
    
log_1 = LogAnalyze("app.log", "output.json")
log_count = log_1.analyze()
# print("log summary:", log_count)
# log_1.write_json(log_count)

log_1 = LogAnalyze("app1.log", "output1.json")
log_count = log_1.analyze()
