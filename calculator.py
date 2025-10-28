import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("450x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        self.expression = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Main container with padding
        main_frame = tk.Frame(self.root, bg="#f5f5f5")
        main_frame.pack(expand=True, fill="both", padx=15, pady=15)

        # Display frame with shadow effect
        display_outer = tk.Frame(main_frame, bg="#d0d0d0", padx=2, pady=2)
        display_outer.pack(fill="both", pady=(0, 20))

        display_frame = tk.Frame(display_outer, bg="#ffffff")
        display_frame.pack(expand=True, fill="both")

        # Result display
        display_font = font.Font(family="Segoe UI", size=36, weight="normal")
        display = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=display_font,
            bg="#ffffff",
            fg="#2c3e50",
            anchor="e",
            padx=20,
            pady=30
        )
        display.pack(expand=True, fill="both")

        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg="#f5f5f5")
        buttons_frame.pack(expand=True, fill="both")

        # Button layout
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        button_font = font.Font(family="Segoe UI", size=20, weight="normal")

        # Color scheme
        colors = {
            'number': {'bg': '#ffffff', 'fg': '#2c3e50', 'active': '#ecf0f1'},
            'operator': {'bg': '#3498db', 'fg': '#ffffff', 'active': '#2980b9'},
            'clear': {'bg': '#e74c3c', 'fg': '#ffffff', 'active': '#c0392b'},
            'equals': {'bg': '#27ae60', 'fg': '#ffffff', 'active': '#229954'}
        }

        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                if button_text == '=':
                    # Make equals button span 2 columns
                    btn = tk.Button(
                        buttons_frame,
                        text=button_text,
                        font=button_font,
                        bg=colors['equals']['bg'],
                        fg=colors['equals']['fg'],
                        activebackground=colors['equals']['active'],
                        activeforeground='#ffffff',
                        relief="flat",
                        borderwidth=0,
                        cursor="hand2",
                        command=lambda: self.calculate()
                    )
                    btn.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=3, pady=3)
                elif button_text == 'C':
                    btn = tk.Button(
                        buttons_frame,
                        text=button_text,
                        font=button_font,
                        bg=colors['clear']['bg'],
                        fg=colors['clear']['fg'],
                        activebackground=colors['clear']['active'],
                        activeforeground='#ffffff',
                        relief="flat",
                        borderwidth=0,
                        cursor="hand2",
                        command=lambda: self.clear()
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
                elif button_text in ['/', '*', '-', '+']:
                    btn = tk.Button(
                        buttons_frame,
                        text=button_text,
                        font=button_font,
                        bg=colors['operator']['bg'],
                        fg=colors['operator']['fg'],
                        activebackground=colors['operator']['active'],
                        activeforeground='#ffffff',
                        relief="flat",
                        borderwidth=0,
                        cursor="hand2",
                        command=lambda b=button_text: self.append_to_expression(b)
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
                else:
                    btn = tk.Button(
                        buttons_frame,
                        text=button_text,
                        font=button_font,
                        bg=colors['number']['bg'],
                        fg=colors['number']['fg'],
                        activebackground=colors['number']['active'],
                        activeforeground='#2c3e50',
                        relief="flat",
                        borderwidth=0,
                        cursor="hand2",
                        command=lambda b=button_text: self.append_to_expression(b)
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)

        # Configure grid weights for responsive design
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1, minsize=80)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1, minsize=100)

    def append_to_expression(self, value):
        if self.result_var.get() == "0" and value != ".":
            self.expression = str(value)
        else:
            self.expression += str(value)
        self.result_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.result_var.set("0")

    def calculate(self):
        try:
            result = eval(self.expression)
            # Format the result nicely
            if isinstance(result, float) and result.is_integer():
                result = int(result)
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