import tkinter as tk


def on_button_click():
    print("ppp")

root = tk.Tk()
root.title("Button Example")
root.geometry("300x200") 

my_button = tk.Button(root, text="Click Me", command=on_button_click).grid(row=0, sticky=tk.W)
my_button_2 = tk.Button(root, text="Click moi", command=on_button_click).grid(row=1, sticky=tk.W)




root.mainloop()