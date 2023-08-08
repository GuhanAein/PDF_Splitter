import PyPDF2
import tkinter as tk
from tkinter import filedialog

def split_pdf(input_path, output_dir, splits, page_numbers):
    pdf = PyPDF2.PdfReader(input_path)

    for split_index in range(splits):
        start_page = page_numbers[split_index][0]
        end_page = page_numbers[split_index][1]

        output_name = input(f"Enter the name for split {split_index + 1}: ")
        output_path = f"{output_dir}/{output_name}.pdf"
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(start_page - 1, end_page):
            pdf_writer.add_page(pdf.pages[page_num])

        with open(output_path, "wb") as output_file:
            pdf_writer.write(output_file)
        print(f"Split {split_index + 1} saved as {output_path}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])

    if not file_path:
        print("No file selected.")
        return

    output_dir = filedialog.askdirectory(title="Select a directory to save the split PDFs")
    if not output_dir:
        print("No output directory selected.")
        return

    splits = int(input("Enter the number of splits: "))
    page_numbers = []

    for i in range(splits):
        start_page = int(input(f"Enter the starting page number for split {i + 1}: "))
        end_page = int(input(f"Enter the ending page number for split {i + 1}: "))
        page_numbers.append((start_page, end_page))

    split_pdf(file_path, output_dir, splits, page_numbers)
    print("PDF splitting completed.")

if __name__ == "__main__":
    main()
