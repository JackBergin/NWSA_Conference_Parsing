"""
Author: Jack Bergin
Date: 08-11-2023
Description: Import the libraries that we will be 
using for parsing through the pdf.
"""
import PyPDF2
import csv
from collections import Counter

"""
Function purpose: Used for parsing the pdf into csv
"""


def read_pdf(pdf_file):
    # Create a PDF object
    pdf = PyPDF2.PdfReader(pdf_file)

    # Get the number of pages
    num_pages = len(pdf.pages)

    # Initializes the text variable
    text = ""

    # Iterate through the pages
    for i in range(num_pages):
        # Get the current page
        page = pdf.pages[i]

        # Get the text on the page
        text += page.extract_text()

        # Makes all of the text lowercase so it's easier to parse through
        text = text.lower()
    # Close the PDF file
    pdf_file.close()
    return text


"""
Function purpose: Populated data in the csv
"""


def write_csv(text, csv_file):
    with open(csv_file, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Extracted Text"])
        csv_writer.writerow([text])


"""
Function purpose: Calls the above two functions in order 
for creating the csv file from the pdf.
"""


def pdf_to_csv():
    # Read the pdf and converts to string
    csv_text = read_pdf(pdf_file)

    # Writes all of the string to a csv file
    write_csv(csv_text, csv_file)


"""
Function purpose: Parse the csv for the keywords
"""


def parse_csv(csv_path, target_word):
    # Open and read the CSV file
    with open(csv_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Iterate through rows and search for the target word
        for row in csv_reader:
            for key, value in row.items():
                if target_word in value:
                    print(f"Found '{target_word}' in column '{key}': {value}")


def parse_sections():
    number_list = [f"{str(i).zfill(3)}." for i in range(5, 648)]
    print(number_list)


if __name__ == "__main__":
    # PDF file path
    pdf_file = open(
        "2018 NWSA program.pdf", "rb"
    )

    # CSV file path
    csv_file = "output.csv"

    # Pdf conversion to Csv file type for proper parsing (This only needs to be run once):
    # pdf_to_csv()

    # Keywords for parsing
    target_words = [
        "integrational issues",
        "motherhood",
        "queer studies",
        "lesbian",
        "trans",
        "race",
        "transnational",
        "class",
        "capitalism",
        "reproductive justice",
    ]

    # Initialize Counters for each target word
    word_counters = {word: Counter() for word in target_words}

    # Increase the field size limit due to data's size
    csv.field_size_limit(10000000)

    # Open and read the CSV file
    with open(csv_file, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Iterate through rows and search for the target words
        for row in csv_reader:
            for key, value in row.items():
                for word in target_words:
                    if word in value:
                        word_counters[word][word] += 1

    # Print the occurrences for each word
    for word in target_words:
        print(f"Occurrences of '{word}': {word_counters[word][word]}")

    # counters = parse_csv(csv_file, key_words)
