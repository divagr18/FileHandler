import tkinter as tk
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from fpdf import FPDF
import os 
import pandas as pd



directory_path = filedialog.askdirectory(title="Select Directory")
files = os.listdir(directory_path)
csv_file = "D:\FIle Handler\Book1.csv"
df = pd.read_csv(csv_file,header=None)
df.reset_index(drop=True, inplace=True)
x = 0

for file in files:
    if (x<=len(df)):
        print(df.iloc[x,0])
        old_file = os.path.join(directory_path, file)
        new_file = os.path.join(directory_path, df.iloc[x,0])
        if not os.path.exists(new_file):
            os.rename(old_file, new_file)
        x = x+1














