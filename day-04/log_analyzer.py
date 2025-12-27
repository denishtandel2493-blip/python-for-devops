import json

def read_logs():
  with open("app.log","r") as file:
  print(file.readlines())

read_logs()

