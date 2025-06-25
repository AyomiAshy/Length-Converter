import tkinter as tk
def convert():
    try:
        inches = float(entry_inch.get())
        cm = inches * 2.54
        label_result.config(text=f"{cm:.2f} cm")
    except ValueError:
        label_result.config(text="Invalid input")
root = tk.Tk()
root.title("Length Converter")
tk.Label(root, text="Inches:").grid(row=0, column=0, padx=10, pady=10)
entry_inch = tk.Entry(root)
entry_inch.grid(row=0, column=1, padx=10, pady=10)
btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.grid(row=1, column=0, columnspan=2, pady=10)
label_result = tk.Label(root, text="0.00 cm")
label_result.grid(row=2, column=0, columnspan=2, pady=10)
root.mainloop()