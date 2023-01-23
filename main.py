import os 
import time
import re

dirs = {
  "html": "templates",
  "css": "styles",
  "py": "snakes",
}

def interpret(string: str):
  print(string)

with open(f"{dirs['html']}/layout.html", "r+") as file:
  data = file.read()
  print(data)
  html = data.replace('\n', '')
  print(html)
  snippets = re.findall(r"{.[^{}]+}", data, re.DOTALL)
  for i, snippet in enumerate(snippets):
    interpret(snippet)