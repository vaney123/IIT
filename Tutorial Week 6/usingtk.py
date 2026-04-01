#converting fahrenheit to celsius

import tkinter as tk

def displayMsg():
    f = float(utemp.get())
    c = (f - 32) * 5/9
    msg = ("${0:.2f} celsius".format(c))
    result.set(msg)

root = tk.Tk()
root.title("Temperature Converter")  #renaming the window name
root.geometry("320x100")

#label - ask user for the temperature in f
name = tk.Label(root, text="Enter temperature to fahrenheit: ")
name.pack()

#Entry for temp
utemp = tk.StringVar()
temp_entry = tk.Entry(root, width=20, textvariable=utemp)
temp_entry.pack()

#button
clickMe = tk.Button (root, text="Click me", width=15, command=displayMsg)
clickMe.pack()

#Entry for the result
result = tk.StringVar()
result_entry = tk.Entry(root, width=0, textvariable=result, state="readonly")
result_entry.pack()

root.mainloop()
