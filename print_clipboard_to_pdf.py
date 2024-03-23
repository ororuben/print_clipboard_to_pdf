import PyPDF2 # pip install PyPDF2
import tkinter as tk # pip install tkinter
from tkinter import filedialog # pip install tkinter
import io # pip install io
import win32clipboard #

# Function to retrieve clipboard content
def get_clipboard_text(): # define function to retrieve clipboard content
    win32clipboard.OpenClipboard() # opens the clipboard
    clipboard_data = win32clipboard.GetClipboardData() # retrieves the clipboard content
    win32clipboard.CloseClipboard() # closes the clipboard
    return clipboard_data # returns the clipboard content

# Function to save text to PDF
def save_text_to_pdf(text): # define function to save text to PDF
    root = tk.Tk() #creates a tkinter window
    root.withdraw() #hides the tkinter window
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path: # if file path is not empty
        pdf = PyPDF2.PdfFileWriter() # creates a new pdf file
        pdf.addPage(PyPDF2.pdf.PageObject.createTextPage(text)) # adds the text to the new pdf file
        with open(file_path, "wb") as f: # opens the file for writing
            pdf.write(f) # writes the new pdf file to the file
        print("PDF saved successfully!") # prints a success message

# Main function
def main(): # define main function
    clipboard_text = get_clipboard_text() # retrieves the clipboard
    if clipboard_text: # if clipboard text is not empty
        save_text_to_pdf(clipboard_text) # saves the clipboard text to PDF
    else: # if clipboard text is empty
        print("Clipboard is empty!") # prints an error message

if __name__ == "__main__": # if main function is called
    main() # calls the main function
