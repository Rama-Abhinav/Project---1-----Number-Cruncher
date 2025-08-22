from tkinter import *

MainScreen = Tk()
MainScreen.title("Basic Calculator")

Num_Bar = Entry(MainScreen, width = 50, borderwidth= 20 )
Num_Bar.grid(row=0,column=0,columnspan=5, padx=10, pady=10)

def Button_Click(num):                                 # Displays the numbers being entered floato the entry box to the user for clarity of use
    Current_Num = Num_Bar.get()
    Num_Bar.delete(0,END)
    Num_Bar.insert(0,str(Current_Num) + str(num))

def Clear():                                            # Clears the Num_Bar for the user to reuse it.
    Num_Bar.delete(0, END)

num1 = None
operation = None 

def set_operation(op):                                  # Stores First Number and then Takes the Operation to be performed and clears entry box
    global num1 , operation
    num1 = float(Num_Bar.get())
    operation = op
    Num_Bar.delete(0, END)

def Calculate_Result():
    global num1, operation
    if operation == "+":
        num2 = float(Num_Bar.get())
        Num_Bar.delete(0,END)
        Num_Bar.insert(0,str(num1+num2))
    elif operation == "-":
        num2 = float(Num_Bar.get())
        Num_Bar.delete(0,END)
        Num_Bar.insert(0,str(num1-num2))
    elif operation == "x":
        num2 = float(Num_Bar.get())
        Num_Bar.delete(0,END)
        Num_Bar.insert(0,str(num1*num2))
    elif operation == "÷":
        num2 = float(Num_Bar.get())
        Num_Bar.delete(0,END)
        Num_Bar.insert(0, str(num1/num2))
    elif operation == "xⁿ":
        Power_n = float(Num_Bar.get())
        Num_Bar.delete(0,END)
        Num_Bar.insert(0, str(num1**Power_n))
    elif operation == "%":
        Num_Bar.delete(0,END)
        Num_Bar.insert(0, f"{num1}% in decimal = {num1/100}")
    elif operation == "√":
        RootOfNum = float(Num_Bar.get())
        Num_Bar.delete(0, END)
        Num_Bar.insert(0, str(num1 ** (1/RootOfNum)))


#Buttons(1-9)
#--> lambda is being used to delay execution of Button_Click(0) until the button is actually pressed.
def Buttons():
    Button_1 = Button(MainScreen, text=1,padx=40,pady=20,command=lambda:Button_Click(1))
    Button_2 = Button(MainScreen, text=2,padx=40,pady=20,command=lambda:Button_Click(2))
    Button_3 = Button(MainScreen, text=3,padx=40,pady=20,command=lambda:Button_Click(3))
    Button_4 = Button(MainScreen, text=4,padx=40,pady=20,command=lambda:Button_Click(4))
    Button_5 = Button(MainScreen, text=5,padx=40,pady=20,command=lambda:Button_Click(5))
    Button_6 = Button(MainScreen, text=6,padx=40,pady=20,command=lambda:Button_Click(6))
    Button_7 = Button(MainScreen, text=7,padx=40,pady=20,command=lambda:Button_Click(7))
    Button_8 = Button(MainScreen, text=8,padx=40,pady=20,command=lambda:Button_Click(8))
    Button_9 = Button(MainScreen, text=9,padx=40,pady=20,command=lambda:Button_Click(9))
    Button_0 = Button(MainScreen, text=0,padx=40,pady=20,command=lambda:Button_Click(0))

    #Ops Buttons
    Button_Equals = Button(MainScreen, text='=',padx=90,pady=20, command=Calculate_Result)
    Button_Plus = Button(MainScreen, text='+',padx=40,pady=20,command =lambda:set_operation('+'))
    Button_Minus = Button(MainScreen, text='-',padx=40,pady=20,command =lambda:set_operation('-'))
    Button_Multiply = Button(MainScreen, text='x',padx=40,pady=20,command =lambda:set_operation('x'))
    Button_Divide = Button(MainScreen, text='÷',padx=40,pady=20,command =lambda:set_operation('÷'))
    Button_PowerOff = Button(MainScreen, text='xⁿ',padx=40,pady=20,command =lambda:set_operation('xⁿ'))
    Button_Percentage = Button(MainScreen, text='%',padx=40,pady=20,command =lambda:set_operation('%'))
    Button_Rootof = Button(MainScreen, text='√',padx=40,pady=20,command =lambda:set_operation('√'))
    Button_Clear = Button(MainScreen, text='C',padx=40,pady=20,command=Clear)


    Button_1.grid(row=1 ,column=0)
    Button_2.grid(row=1 ,column=1)
    Button_3.grid(row=1 ,column=2)
    Button_Plus.grid(row=1,column=3)

    Button_4.grid(row=2 ,column=0)
    Button_5.grid(row=2 ,column=1)
    Button_6.grid(row=2 ,column=2)
    Button_Minus.grid(row=2,column=3)

    Button_7.grid(row=3 ,column=0)
    Button_8.grid(row=3 ,column=1)
    Button_9.grid(row=3 ,column=2)
    Button_Multiply.grid(row=3, column=3)

    Button_0.grid(row=4, column=0)
    Button_Percentage.grid(row=4,column=1)
    Button_Rootof.grid(row=4,column=2)
    Button_Divide.grid(row=4, column=3)

    Button_Clear.grid(row=5, column=0)
    Button_Equals.grid(row=5, column=1, columnspan=2)
    Button_PowerOff.grid(row=5,column=3)
Buttons()

MainScreen.mainloop()