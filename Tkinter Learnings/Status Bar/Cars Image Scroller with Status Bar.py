
from tkinter import *
from  PIL import ImageTk, Image

Mainscreen = Tk()
Mainscreen.title("Cars Image Scroller")
Mainscreen.iconbitmap(r"Tkinter Learnings\Icon, Image, Exit Buttons\Mini Project\Logo.ico")

#Setting Images
Img1 = ImageTk.PhotoImage(Image.open(r"Tkinter Learnings\Icon, Image, Exit Buttons\Mini Project\Img1.png"))
Img2 = ImageTk.PhotoImage(Image.open(r"Tkinter Learnings\Icon, Image, Exit Buttons\Mini Project\Img2.png"))
Img3 = ImageTk.PhotoImage(Image.open(r"Tkinter Learnings\Icon, Image, Exit Buttons\Mini Project\Img3.png"))
Img4 = ImageTk.PhotoImage(Image.open(r"Tkinter Learnings\Icon, Image, Exit Buttons\Mini Project\Img4.png"))
Img5 = ImageTk.PhotoImage(Image.open(r"Tkinter Learnings\Icon, Image, Exit Buttons\Mini Project\Img5.png"))

Image_List = [Img1,Img2,Img3,Img4,Img5]
Image_Num = [1,2,3,4,5]

ImgOnScreen = Label(Mainscreen,image=Img1)
ImgOnScreen.grid(row=0,column=0,columnspan=3)


def Move(Image_Number):
    global ImgOnScreen
    global Button_Forward
    global Button_Back
    ImgOnScreen.grid_forget()
    ImgOnScreen = Label(Mainscreen,image=Image_List[Image_Number])
    
    Button_Forward = Button(Mainscreen, text=">>", command=lambda:Move(Image_Number + 1),fg="White",bg="red")
    Button_Back = Button(Mainscreen , text = "<<",command=lambda:Move(Image_Number - 1),fg="White",bg="red")

    if Image_Number == 4:
        Button_Forward = Button(Mainscreen, text=">>", state=DISABLED,fg="White",bg="red")
    elif Image_Number == 0:
        Button_Back = Button(Mainscreen, text="<<", state=DISABLED,fg="White",bg="red")

    ImgOnScreen.grid(row=0,column=0,columnspan=3)
    Button_Back.grid(row=1,column=0)
    Button_Forward.grid(row=1,column=2)

    Status = Label(Mainscreen, text = f"Image {(str(Image_Num[Image_Number]))} of {len(Image_List)}",anchor=E,fg="green",bg="black",font="Arial")
    Status.grid(row=2, column=0, columnspan=3,sticky=W+E)




#Buttons
Button_Forward = Button(Mainscreen, text=">>", command=lambda:Move(0),fg="White",bg="red")
Button_Exit = Button(Mainscreen, text = 'EXIT', command= Mainscreen.quit,fg="White",bg="red")
Button_Back = Button(Mainscreen, text="<<",command=lambda:Move(0),fg="White",bg="red")

Button_Back.grid(row=1,column=0)
Button_Exit.grid(row=1,column=1)
Button_Forward.grid(row=1,column=2)






Mainscreen.mainloop()