import PyPDF2
from collections import Counter
import re

# Define the PDF file path
pdf_file_path = "/Users/berginjack/Documents/Develop/NWSA_Parsing/2018 NWSA program.pdf"

# Define the words you want to search for
target_words = [
    "motherhood",
    "lesbian",
    "trans",
    "race",
    "transnational",
    "class",
    "capitalism",
]

# Initialize Counters for each target word
word_counters = {word: Counter() for word in target_words}

# Open the PDF file
with open(pdf_file_path, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Iterate through pages and search for target words
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        page_text = page.extract_text()

        for word in target_words:
            word_occurrences = re.findall(
                r"\b" + re.escape(word) + r"\b", page_text, flags=re.IGNORECASE
            )
            word_counters[word].update(word_occurrences)

# Print the occurrences for each word
for word, counter in word_counters.items():
    print(f"Occurrences of '{word}': {sum(counter.values())}")
