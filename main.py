from tkinter import *
from PIL import ImageTk
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")

        #Background Image
        self.bg=ImageTk.PhotoImage(file="images/1.jpg.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.root

        #Lgin Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=330, y=150, width=580, height=400)

        #Title & subtitle
        title=Label(Frame_login, text="Login Here", font=("Impact",35,"bold"), fg="#6162FF", bg="white").place(x=90, y=30)
        subtitle=Label(Frame_login, text="Members Login Area", font=("Goudy old style",15,"bold"), fg="#1d1d1d", bg="white").place(x=90, y=100)

        #Username
        lbl_user=Label(Frame_login, text="Username", font=("Goudy old style",15,"bold"), fg="grey", bg="white").place(x=98, y=140)
        self.username=Entry(Frame_login,  font=("Goudy old style",35,"bold"), fg="#7E6E6", bg="white")
        self.username.place(x=90,y=170,width=320,height=35)


root=Tk()
obj = Login(root)
root.mainloop().resizable(False,False)