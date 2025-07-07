import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd

print("Welcome to PyName. Select your Folder.")
directory_path = filedialog.askdirectory(title="Select Directory")
files = os.listdir(directory_path)
files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(directory_path, x)))
print("Select your CSV file.")
csv_file = filedialog.askopenfile(
    title="Select CSV", filetypes=(("CSV Files", "*.csv"), ("All files", "*.*"))
)
df = pd.read_csv(csv_file)
df.reset_index(drop=True, inplace=True)
x = 0


def operation(x):
    """Renames files in the directory based on names provided in a CSV file.

    Iterates through a global list of files and renames each file to the corresponding
    name specified in the DataFrame `df`, preserving the original file extension.
    If the number of files does not match the number of names in the CSV, prompts
    the user to provide a corrected CSV and retries the operation.

    Args:
        x (int): The starting index to match files with names in the CSV."""
    for file in files:
        print(file)
        if x <= len(df):
            if len(files) == len(df.iloc[:, 0]):
                extension = file.split(".")
                extens = str(extension[-1])
                old_file = os.path.join(directory_path, file)
                new_file = os.path.join(directory_path, df.iloc[x, 0])
                new_file = new_file + "." + extens
                if not os.path.exists(new_file):
                    os.rename(old_file, new_file)
                    print("file renamed to" + df.iloc[x, 0])
            else:
                print(
                    "The number of files is different from the number of names in the CSV. Please provide a fixed CSV."
                )
                getCSV()
                operation()
        x = x + 1


def getCSV():
    """Opens a file dialog to prompt the user to select a CSV file.

    Returns:
        file-like object or None: The opened CSV file object if a file is selected; otherwise, None."""
    csv_file = filedialog.askopenfile(title="Select CSV")


operation(0)
