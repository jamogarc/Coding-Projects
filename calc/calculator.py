import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.expression = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg="#2b2b2b")
        display_frame.pack(expand=True, fill="both")

        # Result display
        display_font = font.Font(family="Arial", size=32, weight="bold")
        display = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=display_font,
            bg="#2b2b2b",
            fg="#ffffff",
            anchor="e",
            padx=20,
            pady=20
        )
        display.pack(expand=True, fill="both")

        # Buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill="both")

        # Button layout
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        button_font = font.Font(family="Arial", size=18, weight="bold")

        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                if button_text == '=':
                    # Make equals button span 2 columns
                    btn = tk.Button(
                        buttons_frame,
                        text=button_text,
                        font=button_font,
                        bg="#4CAF50",
                        fg="white",
                        activebackground="#45a049",
                        command=lambda: self.calculate()
                    )
                    btn.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=2, pady=2)
                elif button_text == 'C':
                    btn = tk.Button(
                        buttons_frame,
                        text=button_text,
                        font=button_font,
                        bg="#f44336",
                        fg="white",
                        activebackground="#da190b",
                        command=lambda: self.clear()
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                elif button_text in ['/', '*', '-', '+']:
                    btn = tk.Button(
                        buttons_frame,
                        text=button_text,
                        font=button_font,
                        bg="#ff9800",
                        fg="white",
                        activebackground="#e68900",
                        command=lambda b=button_text: self.append_to_expression(b)
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                else:
                    btn = tk.Button(
                        buttons_frame,
                        text=button_text,
                        font=button_font,
                        bg="#e0e0e0",
                        fg="black",
                        activebackground="#bdbdbd",
                        command=lambda b=button_text: self.append_to_expression(b)
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)

        # Configure grid weights for responsive design
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1)

    def append_to_expression(self, value):
        self.expression += str(value)
        self.result_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.result_var.set("")

    def calculate(self):
        try:
            result = eval(self.expression)
            self.result_var.set(str(result))
            self.expression = str(result)
        except:
            self.result_var.set("Error")
            self.expression = ""

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
