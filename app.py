import tkinter as tk

root = tk.Tk()

tk.Label(root, text='Label left', bg='green').pack(
    side='left', expand=True, fill='both'
)

tk.Label(root, text='Label1', bg='green').pack(side='left', fill='both', expand=True)
tk.Label(root, text='Label2', bg='red').pack(side='top', fill='both', expand=True)


tk.Label(root, text='Label left', bg='green').pack(
    side='left', expand=True, fill='both'
)

tk.Label(root, text='Label left', bg='green').pack(
    side='left', expand=True, fill='both'
)


root.mainloop()