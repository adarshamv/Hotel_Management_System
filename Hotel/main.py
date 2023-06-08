from tkinter import *
from PIL import Image,ImageTk #pip install pillow



class Main:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #===================1st image======================
        img1=Image.open(r"Images\Image.jpg")
        img1=img1.resize((1550,120),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimag=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimag.place(x=0,y=0,width=1550,height=120)

        #====================logo image======================
        img2=Image.open(r"Images\logo.png")
        img2=img2.resize((230,120),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimag=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimag.place(x=0,y=0,width=230,height=120)

        #====================title==========================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=120,width=1550,height=50)

        #====================Main Frame====================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=170,width=1550,height=620)

       

         #=================Login Page=============
       
        
      

        #=====================downImages==================
        
        img4=Image.open(r"Images\img3.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimag2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimag2.place(x=0,y=0,width=230,height=240)

        img5=Image.open(r"Images\image4.jpg")
        img5=img5.resize((230,210),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimag2=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimag2.place(x=0,y=240,width=230,height=240)
    


if __name__=="__main__":
    root=Tk()
    obj=Main(root)
    root.mainloop()