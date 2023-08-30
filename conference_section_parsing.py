import PyPDF2
from collections import Counter
import re

global_count = 0

def section_headers():

    # 2018 NWSA program
    # Define the headers that mark the beginning of sections
    number_list_2018 = [f"{str(i).zfill(3)}." for i in range(5, 648)]
    # Needs to be included due to naming conflicts for the first 5-19 events
    custom_headers_2018 = ['005. Digital', '006. Bodies', '007. Academic', '008.', '009.',
                  '010. Gender', '011. Art', '012. Making', 
                  '013. Imagínate', '014. Continuing', '015. (De)Regulating', 
                  '016. Gender', '017. (Il)Legible', '018. Inviting', '019. Cite']
    

    custom_headers=custom_headers_2018
    number_list=number_list_2018
    for i in range(0, len(custom_headers)):
        number_list[i] = custom_headers[i]
        
    return number_list


def extract_section_text(pdf_reader, start_page, end_page):
    section_text = ""
    for page_number in range(start_page, end_page):
        page = pdf_reader.getPage(page_number)
        section_text += page.extractText()
    return section_text


# Define the PDF file path
pdf_file_path = "/home/jackbergin/Documents/GitHub_Work/NWSA_Conference_Parsing/2018 NWSA program.pdf"

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

section_headers = section_headers()

# Initialize a global Counter to hold the total counts
global_word_counter = Counter()

with open(pdf_file_path, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Iterate through pages and search for section headers
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        page_text = page.extract_text()

        for i in range(len(section_headers)):
            current_header = section_headers[i]
            next_header = section_headers[(i + 1) % len(section_headers)]

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

                # Add section word occurrences to the global Counter
                global_word_counter.update(section_word_counter)

# Print the occurrences for each word globally
print("Total occurrences for all sections:")
for word, count in global_word_counter.items():
    print(f"'{word}': {count}")

print("Total word count:", sum(global_word_counter.values()))