import tkinter as tk


def write_selections():
    print("These items were selected")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# button = tk.Button(frame,
#                    text="QUIT",
#                    fg="red",
#                    command=quit)
# button.pack(side=tk.LEFT)
write_it = tk.Button(frame,
                   text="display selection",
                   command=write_selections)
write_it.pack(side=tk.LEFT)

root.mainloop()