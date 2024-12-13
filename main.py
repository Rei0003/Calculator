import tkinter as tk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename = "darkly")
window.title("Calculator")
window.geometry("500x500")

# title
title_label = ttk.Label(window, text = "Calculator", font = "Arial 24 bold")


# frames
f_frame = ttk.Frame(window)
s_frame = ttk.Frame(window)
t_frame = ttk.Frame(window)
fo_frame = ttk.Frame(window)
l_frame = ttk.Frame(window)
# Buttons
B0 = ttk.Button(l_frame, text = 0)
B1 = ttk.Button(s_frame, text = 1)
B2 = ttk.Button(s_frame, text = 2)
B3 = ttk.Button(s_frame, text = 3)
B4 = ttk.Button(t_frame, text = 4)
B5 = ttk.Button(t_frame, text = 5)
B6 = ttk.Button(t_frame, text = 6)
B7 = ttk.Button(fo_frame, text = 7)
B8 = ttk.Button(fo_frame, text = 8)
B9 = ttk.Button(fo_frame, text = 9)
B_point = ttk.Button(l_frame, text = ".")
B_plus = ttk.Button(l_frame, text = "+")
B_equals = ttk.Button(l_frame, text = "=")
B_minus = ttk.Button(fo_frame, text = "-")
B_times = ttk.Button(t_frame, text = "x")
B_divide = ttk.Button(s_frame, text = ":")

# pack
title_label.pack()
f_frame.pack(pady = 2)
B1.pack(side = "left", padx = 2)
B2.pack(side = "left", padx = 2)
B3.pack(side = "left", padx = 2)
B_divide.pack(side = "left", padx = 2)
s_frame.pack(pady = 2)
B4.pack(side = "left", padx = 2)
B5.pack(side = "left", padx = 2)
B6.pack(side = "left", padx = 2)
B_times.pack(side = "left", padx = 2)
t_frame.pack(pady = 2)
B7.pack(side = "left", padx = 2)
B8.pack(side = "left", padx = 2)
B9.pack(side = "left", padx = 2)
B_minus.pack(side = "left", padx = 2)
fo_frame.pack(pady = 2)
B0.pack(side = "left", padx = 2)
B_point.pack(side = "left", padx = 2)
B_plus.pack(side = "left", padx = 2)
B_equals.pack(side = "left", padx = 2)
l_frame.pack(pady = 2)

# run
window.mainloop()