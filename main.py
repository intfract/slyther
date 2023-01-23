import os 
import time
import re

dirs = {
  "html": "templates",
  "css": "styles",
  "py": "snakes",
}

with open(f"{dirs['html']}/layout.html", "r+") as file:
  data = file.read()
  print(data)
  html = data.replace('\n', '')
  print(html)
  print(re.findall(r"{.[^{}]+}", data, re.DOTALL))
  