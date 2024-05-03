import PyPDF2 
import time
from gtts import gTTS
import os 
import tkinter as tk
from tkinter import filedialog

# Reading The Pdf File..

def Extract_PDF_FILE(PDF_PATH):
    TEXT = ""
    PDF_Reader = PyPDF2.PdfReader(open(PDF_PATH, 'rb'))
    for Number_of_Pages in range(len(PDF_Reader.pages)):
       TEXT = TEXT + PDF_Reader.pages[Number_of_Pages].extract_text()
    return TEXT 

# Function That Makes The Text Audible..

def Converting_To_Audio(text,Output_FILE):
    Audio_Converter = gTTS(text=text,lang='tr')
    Audio_Converter.save(Output_FILE)
    Ans_tag.config(text="Voice Created!")
    time.sleep(3)

# Selecting The File..

def Select_FILE():
    FILE_PATH = filedialog.askopenfilename(filetypes=[("PDF Dosyaları", "*pdf")])
    if FILE_PATH:
        PDF_Text = Extract_PDF_FILE(FILE_PATH)
        Converting_To_Audio(PDF_Text,"Save.mp3")
        os.system("start Save.mp3")
        
        
# Designing Interface..

App_Window = tk.Tk()
App_Window.title("Text Reader")
App_Window.configure(bg="black")
App_Window.geometry("250x100")
App_Window.resizable(0,0)
Enter_tag = tk.Label(App_Window,text="Welcome To Text Reader !",font=10,bg="black",foreground="white")
Select_file_BTN = tk.Button(App_Window,text="Select The Document",command=Select_FILE)
Enter_tag.grid(row=0,padx=30,pady=10)
Select_file_BTN.grid(padx=50,pady=5)
Ans_tag = tk.Label(App_Window,bg="black",foreground="white")
Ans_tag.grid(row=2,) 


App_Window.mainloop()
