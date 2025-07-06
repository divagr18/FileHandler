import tkinter as tk
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from fpdf import FPDF
import os
import pandas as pd


def selectfile():
    """Open a file selection dialog to choose a file and return its contents as a string.

    Prompts the user to select a file using a file dialog limited to all files and text files. Reads the entire contents of the selected file and returns it.

    Returns:
        str: The contents of the selected file.

    Raises:
        FileNotFoundError: If no file is selected or the file cannot be opened."""
    file_path = filedialog.askopenfilename(
        title="Select a File", filetypes=(("All files", "*.*"), ("Text files", "*.txt"))
    )
    with open(file_path, "r") as file:
        file_content = file.read()
        return file_content


def convert(file_content):
    pdf_output_path = filedialog.asksaveasfilename(
        title="Save As PDF",
        defaultextension=".pdf",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")),
    )
    pdf_canvas = canvas.Canvas(pdf_output_path, pagesize=letter)
    lines = file_content.split("\n")
    y_position = 750
    for line in lines:
        pdf_canvas.drawString(100, y_position, line)
        y_position -= 12
    pdf_canvas.save()


def rename_ultra():
    directory_path = filedialog.askdirectory(title="Select Directory")
    files = os.listdir(directory_path)
    csv_file = "D:\\FIle Handler\\Book1.csv"
    df = pd.read_csv(csv_file)
    for file in files:
        os.rename("from.extension.whatever", "to.another.extension")
    for index, filename in enumerate(files, start=1):
        old_filepath = os.path.join(directory_path, filename)
        new_filename = f"{prefix}_{index:03d}{extension}"
        new_filepath = os.path.join(directory_path, new_filename)
        os.rename(old_filepath, new_filepath)


prefix = "file"
extension = ".txt"
rename_ultra()
