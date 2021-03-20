from tkinter import *
import time

word = "Typing Speed Test"
story = "this is a book"
start = 0.0
end = 0.0

root = Tk()
root.title("英打測速")
root.geometry("1000x750")

def reset():
    global end
    end = 0.0
    f_lab.configure(text="")
    ent.delete(0, "end")

def play():
    global start
    start = time.time()
    # print(start)

def finish():
    global end
    # end = time.time()
    if story == ent.get():
        end = time.time()
        ans = f'{str(round((14/5)/((end-start)/60)))} 字/分 '
        f_lab.configure(text=ans)
    else:
        f_lab.configure(text="Wrong Input")

lab = Label(root, text=word, fg="red")
lab.config(font=("Courier", 88))
lab.grid(row=0, column=0, ipadx=45, ipady=45)

s_lab = Label(root, text=story)
s_lab.config(font=("Courier", 20))
s_lab.grid(row=1, column=0, ipadx=45, ipady=45)

ent = Entry(root, width = 40, font=("Helvetica", 32))
ent.grid(row=2, column=0, ipadx=45, ipady=45)

btn = Button(text="再測試一次", command=reset)
btn.grid(row=3, column=0, pady=10)

s_btn = Button(text="開始", command=play)
s_btn.grid(row=4, column=0, pady=10)

f_btn = Button(text="結束", command=finish)
f_btn.grid(row=5, column=0, pady=10)

f_lab = Label(root, text="", fg="purple")
f_lab.config(font=("Courier", 88))
f_lab.grid(row=6, column=0, pady=10)

root.mainloop()