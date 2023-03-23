from tkinter import*
def clear_all():
    principle_field.delete(0,END)
    rate_field.delete(0,END)
    time_field.delete(0,END)
    t1.delete("1.0",END)
    principle_field.focus_set()
def calculate():
    t1.delete("1.0",END)
    principle=int(principle_field.get())
    rate=float(rate_field.get())
    time=int(time_field.get())
    CI=principle*(pow((1+rate/100),time))
    t1.insert(END,round(CI-principle,2))
root=Tk()
root.configure(background='light blue')
root.geometry("400x250")
root.title("compund Interst Calculater")
label1=Label(root,text="Principal ammount(Rs)").grid(row=1,column=0)
label2=Label(root,text="Rate(%)").grid(row=2,column=0)
label3=Label(root,text="Time(Years)").grid(row=3,column=0)
label1=Label(root,text="Compound Interst").grid(row=5,column=1)
 
principle_field=Entry(root)
rate_field=Entry(root)
time_field=Entry(root)
t1=Text(root,width=15,height=1)
 
principle_field.grid(row=1 ,column=1)
rate_field.grid(row=2,column=1)
time_field.grid(row=3,column=1)
t1.grid(row=5,column=1)
 
Button1=Button(root,text="Submit",command=calculate).grid(row=4,column=1,pady=10)
Button2=Button(root,text="clear",command=clear_all).grid(row=6,column=1,pady=10)
root.mainloop()