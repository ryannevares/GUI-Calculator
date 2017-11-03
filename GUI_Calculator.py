
"""

Author: Ryan Nevares
Title: GUI Calculator
Version: 1.0
This is my first attempt at a graphical-based 10-key calculator written in python, it relies on Tkinter and ttk
This is my first fully functional GUI application so I hope you enjoy it.

Shoutout to YouTuber Derek Banas for assisting me with this project

This is also my first app written in Python 3.5 as I have previously only used 2.7

Please report any bugs to ryannevares@gmail.com

"""

from tkinter import *
from tkinter import ttk


class Calculator:
    calc_value = 0.0  # Initialized value
    # Keep track of which math buttons have been pushed
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self, value):
        entry_val = self.number_entry.get()  # Store the value of the button pressed
        entry_val += value
        self.number_entry.delete(0, 'end')
        self.number_entry.insert(0, entry_val)

    def math_button_press(self, value):
        # reset to false so that only one math function can be live at a time
        self.div_trigger = False
        self.mult_trigger = False
        self.add_trigger = False
        self.sub_trigger = False
        self.calc_value = float(self.entry_value.get())
        print(self.calc_value)

        if value == "/":
            print("/ pressed")
            self.div_trigger = True
        elif value == "*":
            print("* pressed")
            self.mult_trigger = True
        elif value == "+":
            print("+ pressed")
            self.add_trigger = True
        elif value == "-":
            print("- pressed")
            self.sub_trigger = True
        else:
            return False

        self.number_entry.delete(0, "end")  # clear the entry box

    def equal_button_press(self):
        # calculate the solution
        if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:
            if self.add_trigger:
                self.solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                self.solution = self.calc_value - float(self.entry_value.get())
            elif self.mult_trigger:
                self.solution = self.calc_value * float(self.entry_value.get())
            elif self.div_trigger:
                self.solution = self.calc_value / float(self.entry_value.get())

            print("Value 1: ", self.calc_value, "Value 2: ", float(self.entry_value.get()), "Solution", self.solution)
            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, self.solution)

    def clear(self):
        # clear the screen
        self.number_entry.delete(0, "end")
        self.calc_value = 0

    def __init__(self, root):
        self.entry_value = StringVar(root, value="")  # This is the value displayed on the calculator's screen
        root.title("Calculator")
        root.geometry("550x200")
        root.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("TButton", font="Serif 15", padding=5)
        style.configure("TEntry", font="Serif 18", padding=10)

        # Entry Field (calculator display)
        self.number_entry = ttk.Entry(root, textvariable=self.entry_value, width=50)

        self.number_entry.grid(row=0, columnspan=3, sticky=N)

        # Number buttons
        self.button7 = ttk.Button(root, text="7", foreground=blue, command=lambda: self.button_press("7")).grid(row=1, column=0)
        self.button8 = ttk.Button(root, text="8", command=lambda: self.button_press("8")).grid(row=1, column=1)
        self.button9 = ttk.Button(root, text="9", command=lambda: self.button_press("9")).grid(row=1, column=2)
        self.button4 = ttk.Button(root, text="4", command=lambda: self.button_press("4")).grid(row=2, column=0)
        self.button5 = ttk.Button(root, text="5", command=lambda: self.button_press("5")).grid(row=2, column=1)
        self.button6 = ttk.Button(root, text="6", command=lambda: self.button_press("6")).grid(row=2, column=2)
        self.button1 = ttk.Button(root, text="1", command=lambda: self.button_press("1")).grid(row=3, column=0)
        self.button2 = ttk.Button(root, text="2", command=lambda: self.button_press("2")).grid(row=3, column=1)
        self.button3 = ttk.Button(root, text="3", command=lambda: self.button_press("3")).grid(row=3, column=2)
        self.button0 = ttk.Button(root, text="0", command=lambda: self.button_press("0")).grid(row=4, column=1)

        # Math buttons
        self.div_button = ttk.Button(root, text="/", command=lambda: self.math_button_press("/")).grid(row=1, column=3)
        self.mult_button = ttk.Button(root, text="*", command=lambda: self.math_button_press("*")).grid(row=2, column=3)
        self.add_button = ttk.Button(root, text="+", command=lambda: self.math_button_press("+")).grid(row=3, column=3)
        self.sub_button = ttk.Button(root, text="-", command=lambda: self.math_button_press("-")).grid(row=4, column=3)

        # Equals Button
        self.eq_button = ttk.Button(root, text="=", command=lambda: self.equal_button_press()).grid(row=4, column=2)

        # Clear Button
        self.clr_button = ttk.Button(root, text="Clear", command=lambda: self.clear()).grid(row=4, column=0)


root = Tk()
calc = Calculator(root)
root.mainloop()

""" FUTURE SUGGESTIONS: Add more functions (square root etc.)
Make the interface look nicer
"""
