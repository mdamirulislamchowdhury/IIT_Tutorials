import tkinter as tk

root = tk.Tk()           # create the main window
root.title("My First App")
root.geometry("320x160") # width x height (optional)

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

root.mainloop()          # start the event loop


import tkinter as tk

def say_hello():
    print("Hello from the button!")

root = tk.Tk()
root.title("Callbacks")

btn = tk.Button(root, text="Click me", command=say_hello)
btn.pack(pady=10)

root.mainloop()