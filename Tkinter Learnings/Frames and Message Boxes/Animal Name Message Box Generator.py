from tkinter import *

Mainscrren = Tk()
Mainscrren.title("ANIMAL RECOGINISER BASED ON CLIKCS !!")

Screen_Title = Label(Mainscrren, text="CLICK TO MESSAGE ANIMALS !!!",anchor=N)
Screen_Title.place(relx=0.5,rely=0,anchor=N)

frame = LabelFrame(Mainscrren, text ="Select Animal")
frame.pack()


def msg(Animal_Name):
    Msg = ""

    if Animal_Name == "Monkey":
        Msg = "Hi Monkey !! Welcome to my world"
    elif Animal_Name == "Elephant":
        Msg = "Hi Elephant !! Welcome to my world"
    elif Animal_Name == "Lion":
        Msg = "Hi Lion !! Welcome to my world"
    elif Animal_Name == "Rhino":
        Msg = "Hi Rhino !! Welcome to my world"

    Shown_Message = Message(Mainscrren,text=Msg)
    Shown_Message.config(bg="lightpink")
    Shown_Message.pack()

frame_b1 = Button(frame, text="Monkey",command=lambda:msg("Monkey"))
frame_b2 = Button(frame, text="Elephant",command=lambda:msg("Elephant"))
frame_b3 = Button(frame, text="Lion",command=lambda:msg("Lion"))
frame_b4 = Button(frame, text="Rhino",command=lambda:msg("Rhino"))

frame_b1.grid(row=0,column=0,columnspan=2)
frame_b2.grid(row=1,column=0,columnspan=2)
frame_b3.grid(row=2,column=0,columnspan=2)
frame_b4.grid(row=3,column=0,columnspan=2)


Mainscrren.mainloop()