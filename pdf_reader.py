import PyPDF2
import pyttsx3
import argparse

def read_pdf_aloud(pdf_path):
    try:
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get total number of pages
            num_pages = len(pdf_reader.pages)
            print(f"Total pages in PDF: {num_pages}")
            
            # Extract text from each page and read it
            for page_num in range(num_pages):
                # Get the page
                page = pdf_reader.pages[page_num]
                
                # Extract text from the page
                text = page.extract_text()
                
                print(f"\nReading page {page_num + 1}...")
                # Read the text aloud
                engine.say(text)
                engine.runAndWait()
                
    except FileNotFoundError:
        print(f"Error: The file {pdf_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Read PDF file aloud")
    parser.add_argument("pdf_path", help="Path to the PDF file to be read")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Read the PDF
    read_pdf_aloud(args.pdf_path)

if __name__ == "__main__":
    main()
