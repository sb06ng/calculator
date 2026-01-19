import tkinter as tk
from functools import partial

from .logic import calculate

CALCULATOR_WIDTH = 700
CALCULATOR_HEIGHT = 700

PADDING = 2

FONT = ("Arial", 14)
EQUATION_FONT = ("Arial", 20)
COLORS = {"bg": "#f0f0f0", "calc_bg": "#0000ff", "entry_bg": "white"}
BUTTON_COLORS = {
    "number": "#ffffff",
    "main_operator": "#ff9500",
    "clear": "#ff1111",
    "function": "#ffcc00",
}

FUNCTIONS = ["sin", "tan", "sqrt", "fac", "pow"]
BACKSPACE_SYM = "\u232b"

BUTTONS_LAYOUT = [
    [FUNCTIONS[0], "C", BACKSPACE_SYM, "(", ")"],
    [FUNCTIONS[1], "7", "8", "9", "/"],
    [FUNCTIONS[2], "4", "5", "6", "*"],
    [FUNCTIONS[3], "1", "2", "3", "-"],
    [FUNCTIONS[4], "0", ".", "=", "+"],
]


class Calculator:
    """
    create a calculator class that represent the calculator-GUI
    """

    def __init__(self, master):
        self.root = master
        self.root.title("Calculator GUI")
        self.root.geometry(f"{CALCULATOR_WIDTH}x{CALCULATOR_HEIGHT}")
        self.root.configure(background=COLORS["bg"])

        # self.root.bind('<Key>', self.handle_keypress)
        self.root.bind("<Return>", lambda e: self.process_calculation())
        self.root.bind("<BackSpace>", lambda e: self.on_button_click("<-"))
        self.root.bind("<Escape>", lambda e: self.on_button_click("C"))

        # create the area where the equation exist
        self.equation = tk.StringVar()
        self.entry = tk.Entry(
            master,
            textvariable=self.equation,
            font=EQUATION_FONT,
            justify="left",
            bd=10,
            insertwidth=PADDING * 2,
            bg=COLORS["entry_bg"],
        )
        self.entry.pack(side="top", fill="x")

        self.button_frame = tk.Frame(master, bg=COLORS["calc_bg"])
        self.button_frame.pack(side="top", fill="both", expand=True)

        self.create_button_grid()

    def create_button_grid(self):
        """
        create the button grid
        """
        num_columns = len(BUTTONS_LAYOUT[0])
        for c in range(num_columns):
            self.button_frame.columnconfigure(c, weight=1)

        num_rows = len(BUTTONS_LAYOUT)
        for r in range(num_rows):
            self.button_frame.rowconfigure(r, weight=1)

        for row, row_list in enumerate(BUTTONS_LAYOUT):
            for column, label in enumerate(row_list):
                self.create_button(label, row, column)

    def create_button(self, text: str, row: int, column: int):
        """
        create the button widget
        Args:
            text: the text of the button
            row: which row of the button
            column: which column of the button
        """
        if text.isdigit() or text == ".":
            btn_color = BUTTON_COLORS["number"]
        elif text in ["=", "+", "-", "*", "/"]:
            btn_color = BUTTON_COLORS["main_operator"]
        elif text == "C":
            btn_color = BUTTON_COLORS["clear"]
        else:
            btn_color = BUTTON_COLORS["function"]

        btn = tk.Button(
            self.button_frame,
            text=text,
            bg=btn_color,
            font=FONT,
            relief="flat",
            activebackground="#cccccc",
            command=partial(self.on_button_click, text),
        )
        btn.grid(row=row, column=column, sticky="nsew", padx=PADDING, pady=PADDING)

        btn.bind("<Enter>", lambda e: btn.config(background="#dddddd"))
        btn.bind("<Leave>", lambda e: btn.config(background=btn_color))

    def on_button_click(self, value: str):
        """
        What to do when the button clicks
        it sets the equation according to the value passed
        Args:
            value: the value of the button

        """
        current_text = self.equation.get()

        if current_text == "Error":
            self.equation.set("")
            return

        if value in FUNCTIONS:
            self.equation.set(current_text + value + "(")

        elif value == "C":
            self.equation.set("")

        elif value == "=":
            self.process_calculation()

        elif value == BACKSPACE_SYM:
            deleted = False
            # Check if we are deleting a function (e.g., 'sin(')
            for func in FUNCTIONS:
                func_pattern = func + "("
                if current_text.endswith(func_pattern):
                    # Remove the entire length of 'func('
                    new_text = current_text[: -len(func_pattern)]
                    self.equation.set(new_text)
                    deleted = True
                    break

            # If no function was found, just delete one character
            if not deleted:
                self.equation.set(current_text[:-1])
        else:
            self.equation.set(current_text + value)
        self.button_frame.focus_set()

    def handle_keypress(self, event):
        """Map keyboard keys to calculator actions"""
        char = event.char
        # Allow numbers and basic operators
        if char in "0123456789.+-*/(),":
            self.on_button_click(char)

    def process_calculation(self):
        expression = self.equation.get()
        try:
            result = calculate(expression)
            self.equation.set(result)
        except Exception as e:
            self.equation.set(f"Error: {e}")
            self.root.after(2000, lambda: self.equation.set(expression))
