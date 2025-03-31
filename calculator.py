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
            text="CALCULATOR",
            
            # text position
            #command=click_button,

            # button look
            relief="groove"
            )

        self.button_1.grid(row=1, column=2)
        

    # ---------- CREATE WIDGETS --------- #
    def create_widgets(self):

        # button 1
        self.btn_calculator = tk.Button(
                text="1",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 5
        self.btn_calculator.grid(row=5, column=1, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=5, column=1, padx=PAD, pady=PAD, sticky='W')

        # button 2
        self.btn_calculator = tk.Button(
            text="2",
            #command=self.get_data
        )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 5
        self.btn_calculator.grid(row=5, column=2, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=5, column=2, padx=PAD, pady=PAD, sticky='W')
        
        # button 3
        self.btn_calculator = tk.Button(
            text="3",
            #command=self.get_data
        )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 10
        self.btn_calculator.grid(row=5, column=2, padx=PAD, pady=PAD, sticky='E')
        self.lbl_calculator.grid(row=5, column=2, padx=PAD, pady=PAD, sticky='E')

        # button 4
        self.btn_calculator = tk.Button(
                text="4",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 10
        self.btn_calculator.grid(row=5, column=3, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=5, column=3, padx=PAD, pady=PAD, sticky='W')

        # button 5
        self.btn_calculator = tk.Button(
                text="5",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 10
        self.btn_calculator.grid(row=5, column=3, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=5, column=3, padx=PAD, pady=PAD, sticky='W')
        
        # button 6
        self.btn_calculator = tk.Button(
                text="6",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 10
        self.btn_calculator.grid(row=5, column=3, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=5, column=3, padx=PAD, pady=PAD, sticky='W')

        # button 7
        self.btn_calculator = tk.Button(
                text="7",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 10
        self.btn_calculator.grid(row=5, column=3, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=5, column=3, padx=PAD, pady=PAD, sticky='W')   
        # The enter key will activate the calculate method
        #self.root.bind("<Return>", self.get_data)
        #self.root.bind("<KP_Enter>", self.get_data)
        
           

calculator = Calculator()


calculator.root()
calculator.create_widgets()
calculator.root.mainloop()
    




