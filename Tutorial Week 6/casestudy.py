import tkinter as tk

def calculateresult(m1, m2, m3):
    avg = (m1 + m2 + m3) / 3

    if avg >=  50:
        status = "Passed"
    else:
        status = "Failed"
    return avg, status

def calculate():
    try:
        m1 = float(entry1.get())
        m2 = float(entry2.get())
        m3 = float(entry3.get())

        avg, status = calculateresult(m1, m2, m3)

        resultlabel.config(text=f"Average: {avg:.2f} | {status}")

        if status == "Passed":
            root.config(bg="lightgreen")
        else:
            root.config(bg="red")

    except ValueError:
        resultlabel.config(text="Please enter valid input")

def clearfields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    resultlabel.config(text="")
    root.config(bg="white")

root = tk.Tk()
root.title("Student Marks Calculator")
root.geometry("300x250")

tk.Label(root, text="Mark 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Mark 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Mark 3:").pack()
entry3 = tk.Entry(root)
entry3.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=5)
tk.Button(root, text="Clear", command=clearfields).pack(pady=5)

resultlabel = tk.Label(root, text="", font=("Arial", 12))
resultlabel.pack(pady=10)

root.mainloop()
