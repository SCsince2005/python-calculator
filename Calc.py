import tkinter as tk

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("300x400")
        
        # Variables to store calculation
        self.current = ""
        self.total = 0
        
        # Create the display
        self.display = tk.Entry(self.root, width=20, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        
        # You'll add buttons here
        self.create_buttons()
        
    def create_buttons(self):
        # Start with just one button to test
        btn_1 = tk.Button(self.root, text="1", width=7, height=4, command=lambda: self.button_click(1))
        btn_1.grid(row=1, column=0)
        btn_2 = tk.Button(self.root, text="2", width=7, height=4, command=lambda: self.button_click(2))
        btn_2.grid(row=1, column=1)
        btn_3 = tk.Button(self.root, text="3", width=7, height=4, command=lambda: self.button_click(3))
        btn_3.grid(row=1, column=2)
        btn_4 = tk.Button(self.root, text="4", width=7, height=4, command=lambda: self.button_click(4))
        btn_4.grid(row=2, column=0)
        btn_5 = tk.Button(self.root, text="5", width=7, height=4, command=lambda: self.button_click(5))
        btn_5.grid(row=2, column=1)
        btn_6 = tk.Button(self.root, text="6", width=7, height=4, command=lambda: self.button_click(6))
        btn_6.grid(row=2, column=2)
        btn_7 = tk.Button(self.root, text="7", width=7, height=4, command=lambda: self.button_click(7))
        btn_7.grid(row=3, column=0)
        btn_8 = tk.Button(self.root, text="8", width=7, height=4, command=lambda: self.button_click(8))
        btn_8.grid(row=3, column=1)
        btn_9 = tk.Button(self.root, text="9", width=7, height=4, command=lambda: self.button_click(9))
        btn_9.grid(row=3, column=2)
        btn_0 = tk.Button(self.root, text="0", width=7, height=4, command=lambda: self.button_click(0))
        btn_0.grid(row=4, column=1)
        btn_add = tk.Button(self.root, text="+", width=7, height=4, command=lambda: self.operation_click("+"))
        btn_add.grid(row=1, column=3)
        btn_sub = tk.Button(self.root, text="-", width=7, height=4, command=lambda: self.operation_click("-"))
        btn_sub.grid(row=2, column=3)
        btn_mul = tk.Button(self.root, text="*", width=7, height=4, command=lambda: self.operation_click("*"))
        btn_mul.grid(row=3, column=3)
        btn_div = tk.Button(self.root, text="/", width=7, height=4, command=lambda: self.operation_click("/"))
        btn_div.grid(row=4, column=3)
        btn_eq = tk.Button(self.root, text="=", width=7, height=4, command=self.calculate)
        btn_eq.grid(row=4, column=0)
        btn_clr = tk.Button(self.root, text="Clear", width=7, height=4, command=lambda: self.clear_display())
        btn_clr.grid(row=4, column=2)
    
    def button_click(self, number):
        # Get current text in display
        current = self.display.get()
    
        # Clear the display
        self.display.delete(0, tk.END)
    
        # Add the new number to what was already there
        self.display.insert(0, current + str(number)) 
    
    def clear_display(self):
        self.display.delete(0, tk.END)
        self.current = ""
        self.total = 0

    def operation_click(self, op):
        # Store the current number
        current_number = self.display.get()

        if current_number:
            if self.current == "":
                # First number
                self.total = float(current_number)
            else:
                # We have a previous operation, calculate it
                self.calculate()

        # Store the operation
        self.current = op
        self.display.delete(0, tk.END)

    def calculate(self):
        current_number = self.display.get()

        if current_number and self.current:
            try:
                if self.current == "+":
                    result = self.total + float(current_number)
                elif self.current == "-":
                    result = self.total - float(current_number)
                elif self.current == "*":
                    result = self.total * float(current_number)
                elif self.current == "/":
                    if float(current_number) == 0:
                        self.display.delete(0, tk.END)
                        self.display.insert(0, "Error")
                        return
                    result = self.total / float(current_number)

                self.total = result
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.current = ""

            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        
    def run(self):
        self.root.mainloop()

# Run the calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
