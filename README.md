# PDF Reader

A command-line tool that reads PDF files aloud using text-to-speech technology.

## Features

- Read PDF files from start to end
- Customize starting and ending pages
- Adjust reading speed
- Clear command-line interface

## Requirements

- Python 3.x
- Dependencies:
  - PyPDF2 (3.0.1)
  - pyttsx3 (2.90)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/hsinghweb/pdf-reader.git
cd pdf-reader
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python pdf_reader.py path/to/your/file.pdf
```

### Optional Parameters

- `-s` or `--start`: Starting page number (default: 1)
- `-e` or `--end`: Ending page number (default: last page)
- `-x` or `--speed`: Reading speed multiplier (default: 1.0)

### Examples

1. Read entire PDF at normal speed:
```bash
python pdf_reader.py document.pdf
```

2. Read from page 5 to end:
```bash
python pdf_reader.py document.pdf -s 5
```

3. Read pages 5-10 only:
```bash
python pdf_reader.py document.pdf -s 5 -e 10
```

4. Read at 1.5x speed:
```bash
python pdf_reader.py document.pdf -x 1.5
```

5. Read pages 5-10 at 2x speed:
```bash
python pdf_reader.py document.pdf -s 5 -e 10 -x 2.0
```
