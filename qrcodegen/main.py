import qrcode
from tkinter import *
from tkinter import messagebox

def generate_qr():
    text = DataEntry.get()
    filename = FileNameEntry.get()
    try:
        qr = qrcode
        img = qr.make(text)
        img.save(filename)
    except:
        messagebox.showerror(title="Error", message="QR Code export failed")
        return
    messagebox.showinfo(title="Complete", message=f"QR code exported successfully with file name is {filename}")

window = Tk()

TitleText = Label(window, text="QR Code Generator by Khoi", font=('Arial',20)).grid(row=0,column=0,columnspan=2)



DataLabel = Label(window, text="Your Data : ").grid(row=1,column=0)
DataEntry = Entry(window, width=40)
DataEntry.grid(row=1,column=1)

FileNameLabel = Label(window, text="File Name : ").grid(row=2,column=0)
FileNameEntry = Entry(window, width= 40)
FileNameEntry.grid(row=2,column=1)

ConfirmButton = Button(window, text="Generate", command=generate_qr).grid(row=3,column=0)


window.mainloop()

