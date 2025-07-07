import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd

directory_path = filedialog.askdirectory(title="Select Directory")
files = os.listdir(directory_path)
files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(directory_path, x)))
csv_file = filedialog.askopenfile(
    title="Select CSV", filetypes=(("CSV Files", "*.csv"), ("All files", "*.*"))
)
df = pd.read_csv(csv_file)
df.reset_index(drop=True, inplace=True)
x = 0


def operation(x):
    """Rename files in a directory based on names from a DataFrame, matching file extensions.

    Args:
        x (int): Starting index to match files with DataFrame rows.

    The function iterates through a global list of files and renames each file to the corresponding name in a global DataFrame 'df', preserving the original file extension. If the number of files does not match the number of names in the DataFrame, it prompts the user to provide a corrected CSV and restarts the operation. It assumes the presence of global variables: 'files' (list of filenames), 'df' (DataFrame with new names), and 'directory_path' (path to files). The function performs in-place renaming and prints status messages. No value is returned."""
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
    """```python
    ""\"
    Open a file dialog for the user to select a CSV file.

    Prompts the user with a file selection dialog restricted to CSV files and returns the opened file object.

    Returns:
        file object: A file-like object for the selected CSV file, or None if no file was selected.
    ""\"
    ```"""
    csv_file = filedialog.askopenfile(title="Select CSV")


operation(0)
