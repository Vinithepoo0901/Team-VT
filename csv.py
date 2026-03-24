import tkinter as tk 

root = tk.Tk()
root.title("")

button_1 = tk.Button(root, text= "button_1").grid(row=1, sticky=tk.W)

root.mainloop()