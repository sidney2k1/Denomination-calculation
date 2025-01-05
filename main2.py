from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
root=Tk()
root.geometry("650x650")
root.title("Denominator Calculation")
root.configure(bg="light blue")
upload=Image.open("app_img.jpg")
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(root,image=image,bg="light blue")
label.place(x=180,y=20)
label1=Label(root,text="Hey user! Welcome to denomination counter application",bg="light blue")
label1.place(relx=0.5,y=340,anchor=CENTER)
def msg():
    msgbox=messagebox.showinfo("alert","Do you want to calculate the denomination count?")
    if msgbox=="ok":
        topwin()
button1=Button(root,text="lets get started",bg="brown",fg="white",command=msg)
button1.place(x=260,y=360)
def topwin():
    top=Toplevel()
    top.geometry("400x400")
    top.title("Denomination calculator")
    top.configure(bg="light grey")
    label2=Label(top,text="enter total amount",bg="light grey")
    entry=Entry(top)
    label=Label(top,text="Here are the total number of notes found in the number youve given",bg="light grey")
    l1=Label(top,text="2000",bg="light grey")
    l2=Label(top,text="500",bg="light grey")
    l3=Label(top,text="100",bg="light grey")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    def calculator():
        try:
            global amount
            amount=int(entry.get())
            note2000=amount//2000
            amount%=2000
            note500=amount//500
            amount%=500
            note100=amount//100
            amount%=100
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))
        except ValueError:
            messagebox.showerror("Error","Please enter a valid number")
    btn=Button(top,text="Calculate",command=calculator,bg="brown",fg="white")
    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    label.place(x=140,y=170)
    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)
    top.mainloop()
root.mainloop()
