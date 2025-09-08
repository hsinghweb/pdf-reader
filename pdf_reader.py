import PyPDF2
import pyttsx3
import argparse

def read_pdf_aloud(pdf_path, start_page=1, end_page=None, speed=1.0):
    try:
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        
        # Set the reading speed
        engine.setProperty('rate', engine.getProperty('rate') * speed)
        
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get total number of pages
            num_pages = len(pdf_reader.pages)
            print(f"Total pages in PDF: {num_pages}")
            
            # Validate and adjust page numbers
            start_page = max(1, min(start_page, num_pages))
            if end_page is None:
                end_page = num_pages
            end_page = max(start_page, min(end_page, num_pages))
            
            print(f"Reading from page {start_page} to {end_page} at {speed}x speed")
            
            # Extract text from each page and read it
            for page_num in range(start_page - 1, end_page):
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
    parser.add_argument("-s", "--start", type=int, default=1,
                      help="Starting page number (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=None,
                      help="Ending page number (default: last page)")
    parser.add_argument("-x", "--speed", type=float, default=1.0,
                      help="Reading speed multiplier (default: 1.0)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Read the PDF
    read_pdf_aloud(args.pdf_path, args.start, args.end, args.speed)

if __name__ == "__main__":
    main()
