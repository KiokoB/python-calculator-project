import tkinter as tk
# we give tkinter the alias tk for easier 

#color scheme for the calculator
bg_main = "#1C1C1C"
bg_special = "#B9BBB6"
bg_button = "#505050"
bg_operator = "#FF9500"
bg_text = "#ffffff"

# we use class to create a calculator object
class Calculator:
    def __init__(self, root):
        # initialize calculater with root as main window
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.root.geometry("575x718")
        self.root.configure(bg=bg_main)
        # StringVar is a variable in tkinter that stores a string value and updates the display when the user inputs a value.
        self.expression = tk.StringVar()  
        self.expression.set("0")
        # Creates the user interface
        self._build_ui_()

    def _build_ui_(self):
        display_frame = tk.Frame(self.root, bg=bg_main)
        display_frame.pack(fill="both")
        # Label widget shows text on the screen
        tk.Label(display_frame, textvariable=self.expression, font=("Times New Roman", 60), bg=bg_main, fg=bg_text, anchor="e", width=20).pack(fill="both")


        button_layout = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["00", "0", ".", "="],
        ]
        button_frame = tk.Frame(self.root, bg=bg_main)
        button_frame.pack(fill="both")

        for r, row in enumerate(button_layout):
            for c, label in enumerate(row):
                if label == "=":
                    bg_color = bg_operator
                elif label in ["C", "⌫", "%"]:
                    bg_color = bg_special
                    fg_color = bg_main
                elif label in ["+", "-", "*", "/"]:
                    bg_color = bg_operator
                else:
                    bg_color = bg_button
                # creates a button widget with specified label
                button = tk.Button(button_frame, text=label, 
                    font=("Times New Roman", 32), bg=bg_color,
                        fg=bg_text, width=4, height=2, command=lambda button=label: self.on_click(button))
                
                #.grid places the button in grid layout
                button.grid(row=r, column=c, padx=4, pady=4)

    # Add this helper method to your class
    def _update_display(self, value):
        # If the expression is longer than 12 chars, show "..." + last 12 chars
        display = str(value)
        if len(display) > 12:
            display = "..." + display[-12:]
        self.expression.set(display)

    def on_click(self, value):
        current = self.expression.get()

        if value == "C":
            self._update_display("0")
        elif value == "⌫":
            if len(current) > 1:
                self._update_display(current[:-1])
            else:
                self._update_display("0")
        elif value == "=":
            try:
                result = eval(current)
                if float(result).is_integer():
                    self._update_display(int(result))
                else:
                    self._update_display(round(result, 10))
            except Exception:
                self._update_display("Error")
        else:
            if current == "0" and value not in ("+", "-", "*",    "/", "%", "."):
                self._update_display(value)
            else:
                self._update_display(current + value)



if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    # keeps the window open until user closes it
    root.mainloop()
