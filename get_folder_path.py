import os
from tkinter import Tk, filedialog

def get_folder_path():
    root = Tk()
    root.withdraw()
    # Use file dialog to choose the folder
    folder_path = filedialog.askdirectory(title="Choose a Folder")
    root.destroy()  # Close the Tkinter window

    return folder_path