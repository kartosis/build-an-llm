import urllib.request
import re

# Download text-file from Sebastian Raschka's GitHub
url = ("https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt")
file_path = r"C:\Users\karto\Desktop\Build LLM\the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

# Read in the file
with open(file_path, "r", encoding="utf-8") as file:
    raw_text = file.read()

print("Total number of characters: ", len(raw_text))
print(raw_text[:99])

# Regular expression (regex) tokenize

