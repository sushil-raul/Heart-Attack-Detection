import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as needed

def extract_text_from_image(image_path):
    # Open the image file
    img = Image.open(image_path)
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(img)
    return text

def select_file():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff"), ("All files", "*.*"))
    )
    if file_path:
        # Perform OCR on the selected file
        try:
            extracted_text = extract_text_from_image(file_path)
            # Show the extracted text in a message box
            messagebox.showinfo("Extracted Text", extracted_text)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("OCR File Selector")

# Create a button to select a file
select_button = tk.Button(root, text="Select File for OCR", command=select_file)
select_button.pack(pady=25)

# Run the application
root.mainloop()
