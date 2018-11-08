from tkinter import*
master=Tk()
master.title("Arga troll")
master.geometry("500x500")
for i in range (5):
    for j in range(5):
        button=Button(master, text=i, height = 10, width = 40)
        button.grid(row=i, column=j)    

# button1=Button(master,text="B1")
# button1.grid(row=1,column=1)

# button2=Button(master, text="B2")
# button2.grid(row=1,column=2)

# button3=Button(master,text="B3")
# button3.grid(row=1,column=3)

# button4=Button(master,text="B4")
# button4.grid(row=1,column=4)

# button5=Button(master,text="B5")
# button5.grid(row=1,column=5)

master.mainloop()