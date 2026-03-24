import tkinter as tk

root1 = tk.Tk()
v = tk.IntVar()

tk.Radiobutton(root1, text="A", variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(root1, text="B", variable=v, value=2).pack(anchor=tk.W)
tk.Radiobutton(root1, text="C", variable=v, value=3).pack(anchor=tk.W)
tk.Radiobutton(root1, text="D", variable=v, value=4).pack(anchor=tk.W)
root1.mainloop()

if v == 2:
    root2 = tk.Tk()
    v = tk.IntVar()

    tk.Radiobutton(root2, text="A", variable=v, value=1).pack(anchor=tk.W)
    tk.Radiobutton(root2, text="B", variable=v, value=2).pack(anchor=tk.W)
    tk.Radiobutton(root2, text="C", variable=v, value=3).pack(anchor=tk.W)
    tk.Radiobutton(root2, text="D", variable=v, value=4).pack(anchor=tk.W)
    root2.mainloop()