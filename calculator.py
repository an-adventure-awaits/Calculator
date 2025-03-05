"""
Name: calculator.py
Author: Ansonia McIntire
Date: 1/23/2025
Purpose:
"""

# import tkinter
import tkinter as tk

class Calculator:

    def root(self):
        self.root = tk.Tk()

        self.root.title("CALCULATOR")

        self.root.geometry("300x400")

        self.root.configure(bg='pink')


        # button
        self.button_1 = tk.Button(
            self.root,
            text="Calculator",
            
            # text position
            #command=click_button,

            # button look
            relief="groove"
            )

        self.button_1.grid(row=4, column=1)

    # ---------- CREATE WIDGETS --------- #
    def create_widgets(self):
        self.btn_calculator = tk.Button(
            text="Calculate",
            #command=self.get_data
        )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 10
        self.btn_calculator.grid(row=0, column=0, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=1, column=0, padx=PAD, pady=PAD, sticky='W')

        # The enter key will activate the calculate method
        #self.root.bind("<Return>", self.get_data)
        #self.root.bind("<KP_Enter>", self.get_data)
       

           

calculator = Calculator()


calculator.root()
calculator.create_widgets()
calculator.root.mainloop()
    




