""" Since exported files from readme.io are written in markdown, we need to convert them into normal .txt files for the OpenAI language models in order to train them. This code basically grabs all the markdown source files
in the current directory, converts them into plain text and then uses the BeautifulSoup to parse the HTML codes."""

import markdown
import os
from bs4 import BeautifulSoup

# Set the file extension of the markdown files
extension = '.md'

# Get the current working directory
cwd = os.getcwd()

# Create a list of markdown files in the current directory
markdown_files = [f for f in os.listdir(cwd) if f.endswith(extension)]

# Sort the list of markdown files alphabetically
markdown_files.sort()

# Create an empty string to hold the converted text
converted_text = ''

# Loop through the markdown files and convert their contents to text
for file in markdown_files:
    with open(file, 'r', encoding='utf-8') as f:
        md = f.read()
        converted_text += markdown.markdown(md) + '\n'

# Remove HTML tags and elements from the converted text
soup = BeautifulSoup(converted_text, 'html.parser')
plain_text = soup.get_text()

# Write the plain text to a file
with open('converted_text.txt', 'w', encoding='utf-8') as f:
    f.write(plain_text)
