
def read_logs():
  with open("app.log","r") as file:
    return file.readlines()

def analyze(lines):
  log_count = {
              "INFO": 0,
              "WARNING": 0,
              "ERROR": 0
              }
  
  for line in lines:
      if "INFO" in line:
          log_count["INFO"] += 1
      elif "WARNING" in line:
          log_count["WARNING"] += 1
      elif "ERROR" in line:
          log_count["ERROR"] += 1
      else:
        pass
    
  return log_count

lines = read_logs()
counts = analyze(lines)
print("log counts are: ", counts)


