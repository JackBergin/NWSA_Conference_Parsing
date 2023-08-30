import PyPDF2

def extract_pdf_content(pdf_path, start_page, end_page, keywords):
    """
    Extract content from a range of pages of a PDF and count keyword occurrences.

    Parameters:
    - pdf_path (str): Path to the PDF file.
    - start_page (int): Starting page number (0-indexed).
    - end_page (int): Ending page number (0-indexed).
    - keywords (list): List of keywords to count occurrences.

    Returns:
    - dict: Dictionary with page number as key and content as value.
    - dict: Dictionary with keyword as key and its count as value.
    """
    content = {}
    keyword_counts = {keyword: 0 for keyword in keywords}
    
    # Open the PDF file in binary read mode
    with open(pdf_path, 'rb') as file:
        # Initialize PDF reader
        pdf_reader = PyPDF2.PdfReader(file)

        # Loop through the specified page range and extract content
        for page_num in range(start_page, end_page + 1):
            if 0 <= page_num < len(pdf_reader.pages):
                page = pdf_reader.pages[page_num]
                page_content = page.extract_text()
                content[page_num] = page_content

                # Count each keyword in the page content
                for keyword in keywords:
                    keyword_counts[keyword] += page_content.lower().count(keyword.lower())

    return content, keyword_counts

def count_for_2019():
    pdf_path = r"C:\Users\jackc\Documents\NWSA_Conference_Parsing\pdf_files\2019_program.pdf"
    start_page = 60  # Starting from the first page
    end_page = 152    # Ending at the fifth page
    # Keywords for parsing
    keywords = [
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
    extracted_content, keyword_counts = extract_pdf_content(pdf_path, start_page, end_page, keywords)

    for keyword, count in keyword_counts.items():
        print(f"Cumulative count of the keyword '{keyword}': {count}")

def count_for_2018():
    pdf_path = r"C:\Users\jackc\Documents\NWSA_Conference_Parsing\pdf_files\2018_program.pdf"
    start_page = 60  # Starting from the first page
    end_page = 299    # Ending at the fifth page
    # Keywords for parsing
    keywords = [
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
    extracted_content, keyword_counts = extract_pdf_content(pdf_path, start_page, end_page, keywords)

    for keyword, count in keyword_counts.items():
        print(f"Cumulative count of the keyword '{keyword}': {count}")

def count_for_2017():
    pdf_path = r"C:\Users\jackc\Documents\NWSA_Conference_Parsing\pdf_files\2017_program.pdf"
    start_page = 62  # Starting from the first page
    end_page = 267    # Ending at the fifth page
    # Keywords for parsing
    keywords = [
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
    extracted_content, keyword_counts = extract_pdf_content(pdf_path, start_page, end_page, keywords)

    for keyword, count in keyword_counts.items():
        print(f"Cumulative count of the keyword '{keyword}': {count}")

def count_for_2016():
    pdf_path = r"C:\Users\jackc\Documents\NWSA_Conference_Parsing\pdf_files\2016_program.pdf"
    start_page = 50  # Starting from the first page
    end_page = 290    # Ending at the fifth page
    # Keywords for parsing
    keywords = [
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
    extracted_content, keyword_counts = extract_pdf_content(pdf_path, start_page, end_page, keywords)

    for keyword, count in keyword_counts.items():
        print(f"Cumulative count of the keyword '{keyword}': {count}")


def count_for_2015():
    pdf_path = r"C:\Users\jackc\Documents\NWSA_Conference_Parsing\pdf_files\2015_program.pdf"
    start_page = 40  # Starting from the first page
    end_page = 232    # Ending at the fifth page
    # Keywords for parsing
    keywords = [
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
    extracted_content, keyword_counts = extract_pdf_content(pdf_path, start_page, end_page, keywords)

    for keyword, count in keyword_counts.items():
        print(f"Cumulative count of the keyword '{keyword}': {count}")

if __name__ == "__main__":
    print(f"------------------ 2015 ------------------------")
    count_for_2015()
    print(f"------------------ 2016 ------------------------")
    count_for_2016()
    print(f"------------------ 2017 ------------------------")
    count_for_2017()
    print(f"------------------ 2018 ------------------------")
    count_for_2018()
    print(f"------------------ 2019 ------------------------")
    count_for_2019()