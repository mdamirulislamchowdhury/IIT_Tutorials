import tkinter as tk

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def convert():
    try:
        f = float(entry_f.get())
        c = fahrenheit_to_celsius(f)
        result_var.set(f"{c:.2f} °C")
        status_var.set("Converted successfully.")
    except ValueError:
        result_var.set("")
        status_var.set("Please enter a valid number.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("360x160")

tk.Label(root, text="Fahrenheit:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
entry_f = tk.Entry(root, width=12)
entry_f.grid(row=0, column=1, padx=8, pady=8, sticky="w")

tk.Button(root, text="Convert", command=convert).grid(row=0, column=2, padx=8, pady=8)

tk.Label(root, text="Celsius:").grid(row=1, column=0, padx=8, pady=8, sticky="e")
result_var = tk.StringVar(value="")
tk.Label(root, textvariable=result_var).grid(row=1, column=1, padx=8, pady=8, sticky="w")

status_var = tk.StringVar(value="")
tk.Label(root, textvariable=status_var, fg="green").grid(row=2, column=0, columnspan=3, pady=6)

root.columnconfigure(1, weight=1)
root.mainloop()