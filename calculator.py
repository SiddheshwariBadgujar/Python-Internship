

import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("350x400")

        self.entry = tk.Entry(self, font=('Arial', 24), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('*', 2, 3), ('<', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('-', 3, 3), ('0', 4, 1),
            ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self, text=text, font=('Arial', 18), width=4, height=2,
                               command=lambda text=text: self.on_button_click(text))
            button.grid(row=row, column=column, sticky="nsew")

        self.grid_rowconfigure(0, weight=2)
        for i in range(1, 5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.entry.get()
                result = str(eval(expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '<':
            expression = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, expression[:-1])
        else:
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()