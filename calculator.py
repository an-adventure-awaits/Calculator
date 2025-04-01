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

        self.root.geometry("400x500")

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

        self.button_1.grid(row=1, column=3)
        

    # ---------- CREATE WIDGETS --------- #
    def create_widgets(self):

# button 1
        self.btn_calculator = tk.Button(
                text="   1   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=9, column=1, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=9, column=1, padx=PAD, pady=PAD, sticky='W') 
        

# button 2
        self.btn_calculator = tk.Button(
            text="   2   ",
            #command=self.get_data
        )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=9, column=2, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=9, column=2, padx=PAD, pady=PAD, sticky='W') 
        
        
# button 3
        self.btn_calculator = tk.Button(
            text="   3   ",
            #command=self.get_data
        )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=9, column=3, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=9, column=3, padx=PAD, pady=PAD, sticky='W')
        

# button 4
        self.btn_calculator = tk.Button(
                text="   4   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=7, column=1, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=7, column=1, padx=PAD, pady=PAD, sticky='W')

# button 5
        self.btn_calculator = tk.Button(
                text="   5   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=7, column=2, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=7, column=2, padx=PAD, pady=PAD, sticky='W')
        
# button 6
        self.btn_calculator = tk.Button(
                text="   6   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=7, column=3, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=7, column=3, padx=PAD, pady=PAD, sticky='W')

# button 7
        self.btn_calculator = tk.Button(
                text="   7   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=5, column=1, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=5, column=1, padx=PAD, pady=PAD, sticky='W')
        

# button 8
        self.btn_calculator = tk.Button(
                text="   8   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=5, column=2, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=5, column=2, padx=PAD, pady=PAD, sticky='W')
         

# button 9
        self.btn_calculator = tk.Button(
                text="   9   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=5, column=3, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=5, column=3, padx=PAD, pady=PAD, sticky='W')
        

# button 0 
        self.btn_calculator = tk.Button(
                text="   0   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=12, column=2, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=12, column=2, padx=PAD, pady=PAD, sticky='W') 

# button ÷ (divided by) 
        self.btn_calculator = tk.Button(
                text="   ÷   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=5, column=4, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=5, column=4, padx=PAD, pady=PAD, sticky='W') 

# button x (multiplied by) 
        self.btn_calculator = tk.Button(
                text="   x   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=7, column=4, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=7, column=4, padx=PAD, pady=PAD, sticky='W') 

# button - (subtracted by) 
        self.btn_calculator = tk.Button(
                text="   -   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=9, column=4, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=9, column=4, padx=PAD, pady=PAD, sticky='W')

# button + (added by)
        self.btn_calculator = tk.Button(
                text="   +   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=12, column=4, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=12, column=4, padx=PAD, pady=PAD, sticky='W') 

# button . (decimal)
        self.btn_calculator = tk.Button(
                text="   .   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=12, column=3, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=12, column=3, padx=PAD, pady=PAD, sticky='W') 

# button = (equals)
        self.btn_calculator = tk.Button(
                text="   =   ",
                #command=self.get_data
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=15, column=4, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=15, column=4, padx=PAD, pady=PAD, sticky='W') 

        # The enter key will activate the calculate method
        #self.root.bind("<Return>", self.get_data)
        #self.root.bind("<KP_Enter>", self.get_data)
        
           

calculator = Calculator()


calculator.root()
calculator.create_widgets()
calculator.root.mainloop()
    




