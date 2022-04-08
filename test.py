from tkinter import *

from PIL import Image, ImageTk
import tkinter.messagebox as msgbox


root = Tk()
root.geometry("700x500")
root.resizable(False,False)
root.title("ATM Diagnostic System")
root.configure(bg='white')

frame1 = Frame(root)
frame1.configure(background="white")
frame1.pack()
def first():
    # msgbox.showinfo("Hello", "Red Button clicked")
    clear_frame()

    label2 = Label(frame1, text="Is there any technical error like Internet Connection, Power Cut, too many transactions processed in one go? ",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Yes!", padx=10, pady=10, font=("Arial", 20), fg="green", command=soln1, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack(side=LEFT)
    btn3 = Button(frame1, text="No!", padx=10, pady=10, font=("Arial", 20), fg="green", command=proceed1,
                  bg="white")
    btn3.place(x=250, y=150)
    btn3.pack(side=RIGHT)

def proceed1():
    clear_frame()

    label2 = Label(frame1,
                   text="Are you Join Account Holder for this specific card? ",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Yes!", padx=10, pady=10, font=("Arial", 20), fg="green", command=soln2, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack(side=LEFT)
    btn3 = Button(frame1, text="No!", padx=10, pady=10, font=("Arial", 20), fg="green", command=proceed2,
                  bg="white")
    btn3.place(x=250, y=150)
    btn3.pack(side=RIGHT)
def proceed2():
    clear_frame()

    label2 = Label(frame1,
                   text="Are you feed too many times at once in an ATM or spending more time than your normal spending time?",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Yes!", padx=10, pady=10, font=("Arial", 20), fg="green", command=soln3, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack(side=LEFT)
    btn3 = Button(frame1, text="No!", padx=10, pady=10, font=("Arial", 20), fg="green", command=proceed3,
                  bg="white")
    btn3.place(x=250, y=150)
    btn3.pack(side=RIGHT)
def proceed3():
    clear_frame()

    label2 = Label(frame1,
                   text="Debit Card Expired?",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Yes!", padx=10, pady=10, font=("Arial", 20), fg="green", command=soln4, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack(side=LEFT)
    btn3 = Button(frame1, text="No!", padx=10, pady=10, font=("Arial", 20), fg="green", command=proceed4,
                  bg="white")
    btn3.place(x=250, y=150)
    btn3.pack(side=RIGHT)

def proceed4():
    clear_frame()

    label2 = Label(frame1,
                   text="Are you cross daily transaction limit?",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Yes!", padx=10, pady=10, font=("Arial", 20), fg="green", command=soln5, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack(side=LEFT)
    btn3 = Button(frame1, text="No!", padx=10, pady=10, font=("Arial", 20), fg="green", command=proceed5,
                  bg="white")
    btn3.place(x=250, y=150)
    btn3.pack(side=RIGHT)

def proceed5():
    clear_frame()

    label2 = Label(frame1,
                   text="ATM issue: When your ATM does not dispense cash, despite sufficient balance?",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Yes!", padx=10, pady=10, font=("Arial", 20), fg="green", command=soln6, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack(side=LEFT)
    btn3 = Button(frame1, text="No!", padx=10, pady=10, font=("Arial", 20), fg="green", command=proceed6,
                  bg="white")
    btn3.place(x=250, y=150)
    btn3.pack(side=RIGHT)

def proceed6():
    clear_frame()

    label2 = Label(frame1,
                   text="Mismatch in AVs and CVV?",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Yes!", padx=10, pady=10, font=("Arial", 20), fg="green", command=soln7, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack(side=LEFT)
    btn3 = Button(frame1, text="No!", padx=10, pady=10, font=("Arial", 20), fg="green", command=exit,
                  bg="white")
    btn3.place(x=250, y=150)
    btn3.pack(side=RIGHT)




def soln1():
    clear_frame()

    label2 = Label(frame1,
                   text="You can either wait, or try again on another machine",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Exit", padx=10, pady=10, font=("Arial", 20), fg="green", command=exit, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack()

def soln2():
    clear_frame()

    label2 = Label(frame1,
                   text="Your partner may be deactivated the card as they have also the power to do so",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Exit", padx=10, pady=10, font=("Arial", 20), fg="green", command=exit, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack()

def soln3():
    clear_frame()

    label2 = Label(frame1,
                   text="ATM security system consider it as suspicious transaction.",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Exit", padx=10, pady=10, font=("Arial", 20), fg="green", command=exit, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack()
def soln4():
    clear_frame()

    label2 = Label(frame1,
                   text="Contact with respective ATM service retailer.",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Exit", padx=10, pady=10, font=("Arial", 20), fg="green", command=exit, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack()

def soln5():
    clear_frame()

    label2 = Label(frame1,
                   text="Try to withdraw money for the next day",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Exit", padx=10, pady=10, font=("Arial", 20), fg="green", command=exit, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack()

def soln6():
    clear_frame()

    label2 = Label(frame1,
                   text="Chances are your card is getting penetrated by scammers. Get a quick details of the ATM, time and amount you were trying to remove. Visit your bank notify the problem to them. They will immediately block your debit card and issue you new one. ",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Exit", padx=10, pady=10, font=("Arial", 20), fg="green", command=exit, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack()
def soln7():
    clear_frame()

    label2 = Label(frame1,
                   text="Immediately visit your bank branch",
                   font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER, wraplength=600,
                   pady=30)
    label2.pack()
    btn2 = Button(frame1, text="Exit", padx=10, pady=10, font=("Arial", 20), fg="green", command=exit, bg="white")
    btn2.place(x=50, y=150)
    btn2.pack()



def clear_frame():
   for widgets in frame1.winfo_children():
      widgets.destroy()
def exit():
    root.destroy()

label1 = Label(frame1, text="Did your ATM fail to dispense cash even when you had sufficient balance? ", font=("Arial", 20), background="white", fg="green", compound=CENTER, justify=CENTER,wraplength=600 ,pady=30)
label1.pack()
btn1 = Button(frame1,text="Yes!",padx=10,pady=10,font=("Arial", 20),fg="green",command=first, bg="white")
btn1.place(x=250, y=150)
btn1.pack()


root.mainloop()