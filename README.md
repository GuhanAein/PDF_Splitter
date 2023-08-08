# PDF Splitter

A Python script that allows you to split a PDF file into multiple smaller PDF files based on page ranges.

## Description

This Python script uses the PyPDF2 library to split a given PDF file into multiple smaller PDFs. You can specify the number of splits you want and provide the starting and ending page numbers for each split. The script then creates separate PDF files for each split, allowing you to efficiently extract specific sections of a larger PDF document.

## Features

- Interactive user interface using `tkinter` for selecting the input PDF file and output directory.
- Specify the number of splits and the page ranges for each split.
- Customizable output file names for each split.

## Getting Started

1. Make sure you have Python installed on your system.
2. Clone this repository: `git clone https://github.com/your-username/pdf-splitter.git`
3. Navigate to the project directory: `cd pdf-splitter`
4. Install required dependencies: `pip install PyPDF2`
5. Run the script: `python pdfsplit.py`

## Usage

1. Run the script and follow the prompts to select the input PDF file.
2. Specify the output directory where the split PDF files will be saved.
3. Provide the number of splits you want to create.
4. For each split, enter the starting and ending page numbers.
5. Enter a custom name for each split PDF.



The resulting split PDF files will be saved in the chosen output directory.
