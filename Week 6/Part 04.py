import tkinter as tk

def greet():
    name = name_entry.get()
    output.config(text=f"Hello, {name or 'friend'}!")

root = tk.Tk()
root.title("Greeter")

tk.Label(root, text="Your name:").pack()
name_entry = tk.Entry(root, width=24)
name_entry.pack()

tk.Button(root, text="Greet", command=greet).pack(pady=6)

output = tk.Label(root, text="")
output.pack()

root.mainloop()