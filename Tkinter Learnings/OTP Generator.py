# Taking Name, Date of Birth and Phone Number and Generate an alphanumeric Otp

from tkinter import * 
import re

MS = Tk()

def Clear_Box(Click):
    Click.widget.delete(0,END)
    
Name_Entry = Entry(MS, width = 50,borderwidth=20 )
Name_Entry.grid(row=0,column=0,columnspan=4)
Name_Entry.insert(0,"Enter Name") 
Name_Entry.bind("<Button-1>", Clear_Box)

DOB_Entry = Entry(MS, width = 50,borderwidth=20 )
DOB_Entry.grid(row=1,column=0,columnspan=4)
DOB_Entry.insert(0,"DD/MM/YYYY:") 
DOB_Entry.bind("<Button-1>", Clear_Box)

PhoneNum_Entry = Entry(MS, width = 50,borderwidth=20 )
PhoneNum_Entry.grid(row=2,column=0,columnspan=4)
PhoneNum_Entry.insert(0,"Enter Phone Number") 
PhoneNum_Entry.bind("<Button-1>", Clear_Box)

def Save_Name():
    global Name_Letters
    global Name_Letters_List
    Name_Letters = Name_Entry.get()
    Name_Letters_List = []
    for letter in Name_Letters:
        result = re.search(r'[A-Za-z]{1}',letter)
        if result :
            Name_Letters_List.append(letter)
        else:
            pass
    return Name_Letters_List

def Save_DOB():
    global DOB
    DOB = DOB_Entry.get()
    DOB_List = []
    for num in DOB:
        result = re.search(r'[0-9]{1}',num)
        if result:
            DOB_List.append(int(num))
    return DOB_List
    
def Save_PhoneNumber():
    global Phone
    Phone = PhoneNum_Entry.get()
    PhoneNum_List = []
    for PhNum in Phone:
        result = re.search(r'[0-9]{1}',PhNum)
        if result:
            PhoneNum_List.append(PhNum)
    print(PhoneNum_List)


Enter_bt = Button(MS, text = 'Enter',width= 50,command=Save_Name)
Enter_bt = Button(MS, text = 'Enter',width= 50,command=Save_DOB)
Enter_bt = Button(MS, text = 'Enter',width= 50,command=Save_PhoneNumber)
Enter_bt.grid(row=4,column=0,columnspan=3)














MS.mainloop()