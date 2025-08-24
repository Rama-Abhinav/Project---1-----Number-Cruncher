from tkinter import *
from PIL import ImageTk, Image

MainScreen = Tk()
MainScreen.title("Image Viewer")
MainScreen.iconbitmap(r"C:\Users\ironm\OneDrive\Desktop\Project Code Workspaces\Project - 1 --- Number Cruncher\Tkinter Learnings\Icon, Image, Exit Buttons\Icon.png")

My_Img = ImageTk.PhotoImage(Image.open(r"C:\Users\ironm\OneDrive\Desktop\Project Code Workspaces\Project - 1 --- Number Cruncher\Tkinter Learnings\Icon, Image, Exit Buttons\Image.jpg"))
On_screen = Label(MainScreen, image=My_Img)
On_screen.pack()

Exit_pAGE = Button(MainScreen, text = "Done seeing?", command=MainScreen.quit, bg = "red", fg="white")
Exit_pAGE.pack()



MainScreen.mainloop()