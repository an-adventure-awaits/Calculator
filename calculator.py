"""
Name: calculator.py
Author: Ansonia McIntire
Date: 1/23/2025
Purpose:
"""

# import tkinter
import tkinter as tk
from tkinter import ttk

class Calculator:

    def root(self):
        self.root = tk.Tk()

        self.root.title("CALCULATOR")

        self.root.geometry("350x450")

        self.root.configure(bg='pink')

        #self.entry = tk.Entry(
            #self.root)
    

        #self.entry.pack()
        
    # ---------- CREATE WIDGETS --------- #
    def create_widgets_txt_box(self):
        PAD=3
        #self.txt = tk.Text(self.root, height=5, width=40)

        self.display = tk.Label(
            self.root,
            height=5,
            width=38,
            text="Answer:"
            )
        self.display.grid(row=1, column=1, padx=PAD, pady=PAD, sticky='W')
        
    
    def button_number_one(self):
        self.number_1 = 1
        #if self.button_clicked:
        

            # button 1
        self.btn_calculator = tk.Button(
                text="   1   ",
                command=self.number_1
            )

        self.lbl_calculator = tk.Label(
            wraplength=250,
            justify="left"
        )

        PAD = 3
        self.btn_calculator.grid(row=9, column=1, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=9, column=1, padx=PAD, pady=PAD, sticky='W') 

        self.output = tk.Label(
            wraplength=250,
            justify="left",
            text="1"
            )
        

    def button_number_two(self):
        self.number_2 = 2

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
        

    def button_number_three(self):
        self.number_3 = 3

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
    

    def button_number_four(self):
        self.number_4 = 4

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
    

    def button_number_five(self):
        self.number_5 = 5

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
    
    
    def button_number_six(self):
        self.number_6 = 6

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
        
    
    def button_number_seven(self):
        self.number_7 = 7

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
        self.btn_calculator.grid(row=6, column=1, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=6, column=1, padx=PAD, pady=PAD, sticky='W')

            
    def button_number_eight(self):

        self.number_8 = 8

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
        self.btn_calculator.grid(row=6, column=2, padx=PAD, pady=PAD, sticky='W')
        self.lbl_calculator.grid(row=6, column=2, padx=PAD, pady=PAD, sticky='W')
         
    
    def button_number_nine(self):
        self.number_9 = 9

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


    def button_number_zero(self):
        self.number_0 = 0

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

    def divided_by(self):

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

    def mulitplied_by(self):
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

    def subtracted_by(self):

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

    def added_by(self):

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

    def decimal(self):

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

    def equals(self):

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


    def create_widgets_buttons(self):
        pass



        # The enter key will activate the calculate method
        #self.root.bind("<Return>", self.get_data)
        #self.root.bind("<KP_Enter>", self.get_data)

    def create_calculations(self):
        
        # possibly create a dictionary or something like that
        # addition
        """number + number"""

        # subtration
        """number - number"""

        # divition
        """number / number"""

        # multipliction
        """numer * number"""

        # equals
        """number (+_*/) ex amout of numbers = answer"""
    
    def addition(self):
        pass

    def subtraction(self):
        pass

    def mulitplication(self):
        pass

    def division(self):
        pass

           

calculator = Calculator()

calculator.root()


calculator.create_widgets_buttons()
calculator.button_number_one()
calculator.button_number_two()
calculator.button_number_three()
calculator.button_number_four()
calculator.button_number_five()
calculator.button_number_six()
calculator.button_number_seven()
calculator.button_number_eight()
calculator.button_number_nine()
calculator.button_number_zero()
calculator.divided_by()
calculator.mulitplied_by()
calculator.subtracted_by()
calculator.added_by()
calculator.decimal()
calculator.equals()
calculator.create_widgets_txt_box()
calculator.root.mainloop()
    




