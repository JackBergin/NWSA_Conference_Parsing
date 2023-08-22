import PyPDF2
from collections import Counter
import re


def section_headers():
    # Define the headers that mark the beginning of sections
    number_list = [f"{str(i).zfill(3)}." for i in range(20, 648)]
    print(number_list)
    return number_list


def extract_section_text(pdf_reader, start_page, end_page):
    section_text = ""
    for page_number in range(start_page, end_page):
        page = pdf_reader.getPage(page_number)
        section_text += page.extractText()
    return section_text


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

section_headers = section_headers()
# Initialize Counters for each target word
word_counters = {word: Counter() for word in target_words}

with open(pdf_file_path, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Iterate through pages and search for section headers
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        page_text = page.extract_text()

        for i in range(len(section_headers)):
            current_header = section_headers[i]
            next_header = section_headers[
                (i + 1) % len(section_headers)
            ]  # Wrap around to the first header if needed

            if current_header in page_text:
                start_index = page_text.index(current_header)
                end_index = (
                    page_text.index(next_header)
                    if next_header in page_text
                    else len(page_text)
                )

                section_text = page_text[start_index:end_index]

                # Initialize a Counter for this section
                section_word_counter = Counter()

                for word in target_words:
                    word_occurrences = re.findall(
                        r"\b" + re.escape(word) + r"\b",
                        section_text,
                        flags=re.IGNORECASE,
                    )
                    section_word_counter.update(word_occurrences)

                # Print the occurrences for each word within this section
                print(f"Occurrences for '{current_header}':")
                for word, count in section_word_counter.items():
                    print(f"'{word}': {count}")
                print()
