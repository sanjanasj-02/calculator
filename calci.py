import tkinter as tk
class Calculator(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Colorful Calculator")
        self.geometry("320x450")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.expression = ""

        # Entry widget to display expressions and results
        self.entry = tk.Entry(
            self,
            font=("Arial", 20),
            bd=10,
            relief=tk.RIDGE,
            justify='right',
            bg="#F0F0F0"
        )
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=5, sticky="nsew")

        # Button colors
        button_colors = {
            'numbers': "#FFB74D",      
            'operators': "#FFB74D",   
            'equals': "#FFB74D",       
            'clear': "#FFB74D",        
            'delete': "#FFB74D",       
            'parentheses': "#FFB74D",  
            'power': "#FFB74D"          
        }

        # Buttons layout with color categories
        buttons = [
            ('7', 1, 0, 'numbers'), ('8', 1, 1, 'numbers'), ('9', 1, 2, 'numbers'), ('/', 1, 3, 'operators'),
            ('4', 2, 0, 'numbers'), ('5', 2, 1, 'numbers'), ('6', 2, 2, 'numbers'), ('*', 2, 3, 'operators'),
            ('1', 3, 0, 'numbers'), ('2', 3, 1, 'numbers'), ('3', 3, 2, 'numbers'), ('-', 3, 3, 'operators'),
            ('0', 4, 0, 'numbers'), ('.', 4, 1, 'numbers'), ('=', 4, 2, 'equals'), ('+', 4, 3, 'operators'),
            ('C', 5, 0, 'clear'), ('(', 5, 1, 'parentheses'), (')', 5, 2, 'parentheses'), ('', 5, 3, 'power')
        ]

        for (text, row, col, category) in buttons:
            tk.Button(
                self,
                text=text,
                font=("Arial", 14),
                width=5,
                height=2,
                bg=button_colors.get(category, "#FFFFFF"),
                activebackground="#BDBDBD",
                command=lambda t=text: self.button_clicked(t)
            ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Configure grid weights for responsiveness
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

    def button_clicked(self, text):
        if text == "=":
            try:
                result = eval(self.expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
                self.expression = str(result)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
                self.expression = ""
        elif text == "C":
            self.entry.delete(0, tk.END)
            self.expression = ""
        else:
            self.expression += text
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

if __name__ == "_main_":
    app = Calculator()
    app.mainloop()
