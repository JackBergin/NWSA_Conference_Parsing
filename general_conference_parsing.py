import PyPDF2

def extract_pdf_content(pdf_path, start_page, end_page, keywords):
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

def parser():
    pdf_paths = [r"pdf_files\2015_program.pdf", 
                 r"pdf_files\2016_program.pdf", 
                 r"pdf_files\2017_program.pdf", 
                 r"pdf_files\2018_program.pdf", 
                 r"pdf_files\2019_program.pdf"]
    
    start_page = [40, 50, 62, 60, 60]  # Starting from the first page
    end_page = [232, 290, 267, 299, 152]    # Ending at the fifth page
    # Keywords for parsing
    keywords = [
        "intergenerational",
        "motherhood",
        "queer",
        "lesbian",
        "gay",
        "trans",
        "race",
        "transnational",
        "class",
        "capitalism",
        "reproductive justice",
    ]    

    for index in range(0, len(pdf_paths)):
        extracted_content, keyword_counts = extract_pdf_content(pdf_paths[index], start_page[index], end_page[index], keywords)
        iterator=2015
        iterator=iterator+index

        print(f'------------------------- {iterator} General Conference -------------------------')
        for keyword, count in keyword_counts.items():
            print(f"Cumulative count of the keyword '{keyword}': {count}")

if __name__ == "__main__":
    parser()