from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
import tkinter as tk
import webbrowser
import datetime
import time
root =Tk()

root.title('login')
root.geometry('925x500+700+200')
root.configure(bg="white")
root.resizable(False,False)

now=datetime.datetime.now()

def dey():
    for frame in main_frame.winfo_children():
        frame.destroy()

    
    cont=Entry(frame,width=50,fg='black',border=2,bg='lightblue',font=('Times New Roman',14,'bold'))
    cont.place(x=30,y=80)
    cont.insert(0,'Contact number')
    cont.bind('<FocusIn>',on_enter)
    cont.bind('<FocusOut>',on_leave)
    def sign():
        u=cont.get()
        eng(u)
        if u=='+7418014335':
            sent()
    Button(frame,width=20,pady=7,text='Send result',bg='orange',font=('Times New Roman',12,'bold'),fg='black',command=sign).place(x=70,y=150)

def syllabus_e():
    un=Frame(root)
    un=Frame(root,width=2000,height=500,bg='white')
    un.place(x=0,y=frame(un,width=4200,height=4500,bg='lightblue').place(x=-100,y=-100))
    Label(un,image=img2,bg='lightblue').place(x=200,y=25)
    
    Button(frame,width=20,pady=7,text='English syllabus',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=lin_e).place(x=50,y=0)
    Button(frame,width=20,pady=7,text='Physics syllabus',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=lin_s).place(x=50,y=50)
    Button(frame,width=20,pady=7,text='NEET syllabus',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=lin_n).place(x=50,y=100)
    Button(frame,width=20,pady=7,text='JEE syllabus',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=lin_j).place(x=50,y=150)
    Button(frame,width=20,pady=7,text='Compute science syllabus',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=lin_c).place(x=50,y=200)
    Button(frame,width=20,pady=7,text='Maths syllabus',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=lin_m).place(x=50,y=250)

    Button(frame,width=20,pady=7,text='Back',bg='yellow',font=('Times New Roman',10,'bold'),fg='white',command=back).place(x=50,y=320)    
    
    
    
def lin_e():
    webbrowser.open("https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-prose-chapter-1/")
def lin_s():
    webbrowser.open("https://www.tntextbooks.in/p/12th-books.html")
def lin_n():
    webbrowser.open("https://www.tntextbooks.in/p/12th-books.html")
def lin_j():
    webbrowser.open("https://www.tntextbooks.in/p/12th-books.html")
def lin_c():
    webbrowser.open("https://www.tntextbooks.in/p/12th-books.html")
def lin_m():
    webbrowser.open("https://www.tntextbooks.in/p/12th-books.html")



    
    
    
    
def signin():
    username=user.get()
    password=code.get()
    
    if ((username=='gugan'or username=='sanjay')and(password=='**' or password=='123' )):    
        #Label(screen,text="Welcome to our page",bg="orange",font=('Times New Roman(Body)',23,'bold')).pack(expand=True)
        #search()
        import sqlite3
        conn=sqlite3.connect("sab1.db")
        cursor=conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS rog1
                          (name TEXT,m INTEGER,m1 INTEGER,m2 INTEGER,m3 INTEGER,m4 INTEGER,m5 INTEGER,Phone_number INTEGER)''')
        cursor.execute("INSERT INTO rog1(name) VALUES (' " +username+ "')")
        cursor.execute("SELECT name FROM rog1")
        rows = cursor.fetchall()
        print(rows)
        conn.commit()
        
        
        search()
        
    elif username!='gugan' and password!='****':
        messagebox.showerror("Invalid","Invalid Username and Password")
    elif password!='****':
        messagebox.showerror("Invalid","Invalid Password")
    elif username!='gugan':
         messagebox.showerror("Invalid","Invalid Username")

img = PhotoImage(file='bg.png',width=1000,height=700)
img2=PhotoImage(file='connect.png',width=900,height=500)
img3=PhotoImage(file='sci1.png',width=1000,height=500)
img4=PhotoImage(file='fat.png',width=900,height=200)
img5=PhotoImage(file='bio.png',width=1000,height=900)
img6=PhotoImage(file='maths.png',width=1000,height=500)
img7=PhotoImage(file='jee.png',width=1000,height=500)
img8=PhotoImage(file='sci3.png',width=1000,height=500)
img9=PhotoImage(file='qu.png',width=950,height=900)
img10=PhotoImage(file='eng2.png',width=1300,height=1000)
img11=PhotoImage(file='dis.png',width=1300,height=950)

Label(root,width=1000,height=700,image=img,bg='green').place(x=0,y=0)
frame=Frame(root,width=320,height=450,bg='brown')
frame.place(x=480,y=70)
heading=Label(frame,text='Sign in',fg='black',bg='brown',font=('Times New Roman',23,'bold'))
heading.place(x=100,y=5)


def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user=Entry(frame,width=20,fg='black',border=2,bg='lightblue',font=('Times New Roman',14,'bold'))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


#________________________________________________________

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    
    name=code.get()
    
    if name=='':
        
        code.insert(0,'Password')

code=Entry(frame,width=20,fg='black',border=2,bg='lightblue',font=('Times New Roman',14,'bold'))
code.place(x=30,y=140)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=167)
Button(frame,width=29,pady=7,text='Log in',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',border=0,command=signin).place(x=30,y=250)

#---------------------------------------------------------cont

'''def on_enter(e):
    cot.delete(0,'end')
def on_leave(e):
    name=cot.get()
    if name=='':
        cot.insert(0,'Contact')
cot=Entry(frame,width=20,fg='black',border=2,bg='lightblue',font=('Times New Roman',14,'bold'))
print(cot.get)
cot.place(x=30,y=200)
cot.insert(0,'Contact')
cot.bind('<FocusIn>',on_enter)
cot.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=227)
contact=cot.get()
'''

#------------------------------------------------------contend

#def dey():
    #for frame in main_frame.winfo_children():
       # frame.destroy()
    
def empty():
    fr=Frame(root,bg='white')
    back_btn=Button(options_frame,text='back',font=('Times New Roman',15,'bold'),
                   fg="black",bd=0,bg='pink',command=lambda:empty)
    back_btn.place(x=250,y=50)
    fr.pack(side=TOP)
    fr.pack_propagate(False)
    fr.configure(width=950,height=80)



     
    def indicate(lb,page):
            hide_indicators()
            lb.config(bg="blue")
            
def opt():
    options_frame=Frame(root,bg="pink")
    show_btn=Button(options_frame,text='+',font=('Times New Roman',15,'bold'),fg="black",bd=0,bg='pink',
                   command=lambda:indicate(show_indicate,home_page))
    show_btn.place(x=10,y=50)

    show_indicate=Label(options_frame,text='',bg="pink")
    show_indicate.place(x=3,y=50,width=5,height=40)
    show_btn.place(x=10,y=20)
    syall=Button(options_frame,text='Syallabus',font=('Times New Roman',15,'bold'),fg="black",bd=0,bg='pink',command=syllabus_e).place(x=30,y=20)
    
    #back_btn=Button(options_frame,text='back',font=('Times New Roman',15,'bold'),fg="black",bd=0,bg='pink',command=)
    #syall.place(x=250,y=50)
    syall=Label(options_frame,text='',bg="yellow")
    #syall.place(x=350,y=50,width=500,height=40)
    #syall.place(x=700,y=20)
    
   # back()
    options_frame.pack(side=BOTTOM)
    options_frame.pack_propagate(False)
    options_frame.configure(width=950,height=80)

    def indicate(lb,page):
        hide_indicators()
        lb.config(bg="blue")
        lb.place(x=0,y=15)
    
    def hide_indicators():
        show_indicate.config(bg="pink")

def home_page():
    home_frame=tk.Frame(main_frame)

    lb=tk.Label(home_frame,text="Hello",font=('Times New Roman',15,'bold'))
    lb.pack()
    home_frame.pack(pady=20)

#def hide_indicators(opt):
    #show_indicate.config(bg="pink")
    '''menu_indicate.config(bg="pink")
    cont_indicate.config(bg="pink")
    about_indicate.config(bg="pink")'''
def indicats(lb,page):
    hide_indicators()
    lb.config(bg="red")
    lb.config(width=500,height=500)
    lb.place(x=0,y=15)
    
def back():
    
    wut=Frame(root)
    wut=Frame(root,width=2000,height=500,bg='white')
    wut.place(x=0,y=0)
    
   
    frame=Frame(wut,width=4200,height=4500,bg='lightblue').place(x=-100,y=-100)
    Label(wut,image=img2,bg='lightblue').place(x=250,y=25)
    

    Button(frame,width=29,pady=7,text='English',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=yu_eng_st).place(x=00,y=0)

    Button(frame,width=29,pady=7,text='NEET',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=yu_neet_st).place(x=0,y=50)

    Button(frame,width=29,pady=7,text='JEE',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=yu_jee_st).place(x=0,y=100)
    
    Button(frame,width=29,pady=7,text="Maths",bg='green',font=('Times New Roman',10,'bold'),fg='white',command=yu_mat_st).place(x=0,y=150)

    Button(frame,width=29,pady=7,text='Compute science',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=yu_csc_st).place(x=0,y=200)
    
    Button(frame,width=29,pady=7,text='Physics',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=yu_sci_st).place(x=0,y=250)
    
    
def subj():
    english()


        #if search=='science':
#        science_que()

def search():
    
    
    wun=Frame(root)
    wun=Frame(root,width=2000,height=500,bg='white')
    wun.place(x=0,y=0)
    
    
    frame=Frame(wun,width=4200,height=4500,bg='lightblue').place(x=-100,y=-100)
    Label(wun,image=img2,bg='lightblue').place(x=200,y=25)
    
    Button(frame,width=20,pady=7,text='English',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=yu_eng_st).place(x=0,y=0)

    Button(frame,width=20,pady=7,text='NEET',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=yu_neet_st).place(x=0,y=50)

    Button(frame,width=20,pady=7,text='JEE',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=yu_jee_st).place(x=0,y=100)

    Button(frame,width=20,pady=7,text="Maths",bg='green',font=('Times New Roman',10,'bold'),fg='white',command=yu_mat_st).place(x=0,y=150)

    Button(frame,width=20,pady=7,text='Compute science',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=yu_csc_st).place(x=0,y=200)
    Button(frame,width=20,pady=7,text='Physics',bg='green',font=('Times New Roman',10,'bold'),fg='white',command=yu_sci_st).place(x=0,y=250)
    
    opt()
#---------------------------------eng you
def eng_yu():
    webbrowser.open("https://www.youtube.com/results?search_query=english+syllabus+class+12+cbse+2022-23")
    
def yu_eng_st():
    nun=Frame(root)
    nun=Frame(root,width=2000,height=500,bg='white')
    nun.place(x=0,y=0)
    
    
    frame=Frame(nun,width=4200,height=4500,bg='pink').place(x=-100,y=-100)
    Label(nun,image=img10,bg='pink').place(x=0,y=0)
    
    label=Label(frame,text="English!",fg='black',bg='lightpink',font=('Times New Roman',40)).place(x=400,y=0)


    Button(frame,width=27,pady=7,text='Test',bg='green',font=('Times New Roman',20,'bold'),fg='white',command=disc).place(x=300,y=270)
    Button(frame,width=27,pady=7,text='Videos',bg='green',font=('Times New Roman',20,'bold'),fg='white',command=eng_yu).place(x=300,y=340)
    Button(frame,width=27,pady=7,text='Back',bg='red',font=('Times New Roman',20,'bold'),fg='white',command=back).place(x=300,y=400)
    
    
def disc():
    nun=Frame(root)
    nun=Frame(root,width=2000,height=500,bg='white')
    nun.place(x=0,y=0)
    frame=Frame(nun,width=4200,height=4500,bg='pink').place(x=-100,y=-100)
    Label(nun,image=img11,bg='pink').place(x=0,y=0)
    
    Button(frame,width=15,pady=7,text='Lets start the test!',bg='pink',font=('Times New Roman',15,'bold'),fg='black',command=english).place(x=100,y=450)
#-------------------------------eng end
#-------------------------------engdata
def eng():
    import sqlite3
    conn=sqlite3.connect("sab1.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rog1
                    (name TEXT,m INTEGER,m1 INTEGER,m2 INTEGER,m3 INTEGER,m4 INTEGER,m5 INTEGER,Phone_number INTEGER)''')
    cursor.execute("INSERT INTO rog1(m) VALUES ('1')")
    cursor.execute("SELECT name,COUNT(m) FROM rog1 Order By m")
    rows = cursor.fetchall()
    print(rows)
    conn.commit()


    import sqlite3
    import io
    import csv
    d=open('C:\\Users\\Admin\\Documents\\58.csv','w')
    c=csv.writer(d)
    connection=sqlite3.connect("sab1.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM rog1")
    co=[i[0]for i in cursor.description]
    c.writerow(co)
    data=cursor.fetchall()
    for item in data:
        c.writerow(item)
    d.close()
    

    
                
    
    with open('C:\\Users\\Admin\\Documents\\58.csv',"r",newline=None)as fd:
        r=csv.reader(fd)
        for line in fd:
            line=line.replace("\n","")
            print(line)
    for i in range( len(rows)):
        for j in range (len(rows)):
            print(rows[j][1])
            if(rows[j][1]>=5):
                import pywhatkit
                a=pywhatkit.sendwhatmsg("+7418014335","YOU HAVE GOT ANOTHER FREE COURSE",now.hour,now.minute+3)
                print(a)

    cursor.close()
    connection.close()
    
    
    

#def test():
    
    '''def on_enter(e):
        search.delete(0,'end')
    def on_leave(e):
        name=search.get()
        if name=='':
            search.insert(0,'Enter_What_you_prefer')
    frame=Frame(sc,width=40,height=30,bg='white')
    #frame.place(x=80,y=50)
    #frame.insert(0,'Enter What you prefer')'''
    
    #user=Entry(frame,width=20,fg='black',border=2,bg='white',font=('Times New Roman',14,'bold'))
    #search=Entry(frame,width=600,fg='black',border=2,bg='white',font=('Times New Roman',14,'bold'))
    #search.place(x=0,y=0)
    #search.insert(0,'Enter What you prefer')
    #Button(sec,width=15,pady=2,text='English',bg='purple',font=('Times New Roman',10,'bold'),border=0,command=subj).place(x=100,y=2)
    
   
    #search.bind('<FocusIn>',on_enter)
    #search.bind('<FocusOut>',on_leave)
    #opt()

    
'''def back_1():
    frame=Frame(sc,width=4200,height=4500,bg='white')
    
    frame=Frame(sc,width=400,height=30,bg='white')
    frame.place(x=80,y=50)'''

#---------------------------------------------------eng

def english():
    run=Frame(root)
    run=Frame(root,width=2000,height=500,bg='white')
    run.place(x=0,y=0)
    '''can=Canvas(run)
    scr=tk.Scrollbar(run,orient=VERTICAL,command=can.yview)
    scr.pack(side=RIGHT,fill=Y)
    can.configure(yscrollcommand=scr.set)
    can.bind('<Configure>',lambda e:can.configure(scrollregion=can.bbox("all")))


    run=Frame(can)

    can.create_window((0,0),window=run,anchor="nw",)'''

    #run.pack(side=LEFT,fill=BOTH,expand=1)

    #run.pack(fill=BOTH,expand=1)

    '''
    
    
    '''
    
    

    #run=Frame(can)

    #can.create_window((0,0),window=run,anchor="nw",)


    frame=Frame(run,width=4200,height=4500,bg='blue').place(x=-100,y=-100)
    Label(run,image=img3,bg='blue').place(x=10,y=0)

    
    Button(frame,text='\t\tLets move on to the question!',font=('Times New Roman',25)).place(x=10,y=10)


    label=Label(frame,text="1.If I'd realized this before, I ............... in such a mess now",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)
    

    Button(frame,width=29,pady=7,text='a).Wouldn',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=130)

    Button(frame,width=29,pady=7,text='b).Wont have been',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='c).Had not been',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='d).Wouldnt have been',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)

    Button(frame,width=29,pady=7,text="e).Weren't",bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=eng).place(x=20,y=270)

    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_2).place(x=50,y=320)
    
def next_2():
    sun=Frame(root)
    sun=Frame(root,width=2000,height=500,bg='white')
    sun.place(x=0,y=0)
    frame=Frame(sun,width=4200,height=4500,bg='white').place(x=-100,y=-100)

    
    #Button(frame,text='\t\tLets move on to the question!',font=('Times New Roman',25)).place(x=10,y=10)
    
    frame=Frame(sun,width=4200,height=4500,bg='blue').place(x=-100,y=-100)
    Label(sun,image=img3,bg='blue').place(x=10,y=0)


    label=Label(frame,text="2.............. an unmarried mother herself, she wouldsympathize with you and appreciate your problems. ",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)

    Button(frame,width=29,pady=7,text='a).Accepting',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=130)

    Button(frame,width=29,pady=7,text='b).Admitting',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='c).To be',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=eng).place(x=20,y=200)
    Button(frame,width=29,pady=7,text='d).Being ',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)

    Button(frame,width=29,pady=7,text='e).To have been',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=270)

    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_3).place(x=50,y=320)
    
def next_3():
    bun=Frame(root)
    bun=Frame(root,width=2000,height=500,bg='white')
    bun.place(x=0,y=0)
    frame=Frame(bun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    frame=Frame(bun,width=4200,height=4500,bg='blue').place(x=-100,y=-100)
    Label(bun,image=img3,bg='blue').place(x=10,y=0)

    label=Label(frame,text="3.It must have been an interesting performance. Iwould like ............... it, too. I'm sorry I missed it. ",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).To be seeing',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=eng).place(x=20,y=130)

    Button(frame,width=29,pady=7,text='b).To have seen',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='c).To see ',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)
    Button(frame,width=29,pady=7,text='d).To have been seen',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)

    Button(frame,width=29,pady=7,text='e).to have been seeing',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=270)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_4).place(x=50,y=320)
def next_4():
    gun=Frame(root)
    gun=Frame(root,width=2000,height=500,bg='white')
    gun.place(x=0,y=0)
    frame=Frame(gun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    frame=Frame(gun,width=4200,height=4500,bg='blue').place(x=-100,y=-100)
    Label(gun,image=img3,bg='blue').place(x=10,y=0)

    label=Label(frame,text="4.Isn't it about time ............... taking things seriously?",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).For you starting',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=eng).place(x=20,y=130)

    Button(frame,width=29,pady=7,text='b).To have been starting',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='c).You to start',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)
    Button(frame,width=29,pady=7,text='d).Starting ',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)

    Button(frame,width=29,pady=7,text='e).You started',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=270)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_5).place(x=50,y=320)

    
def next_5():
    tun=Frame(root)
    tun=Frame(root,width=2000,height=500,bg='white')
    tun.place(x=0,y=0)
    frame=Frame(tun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    frame=Frame(tun,width=4200,height=4500,bg='blue').place(x=-100,y=-100)
    Label(tun,image=img3,bg='blue').place(x=10,y=0)

    label=Label(frame,text="5.What did you think of the ﬁlm __?",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).That you saw it last week ',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=130)

    Button(frame,width=29,pady=7,text='b).If you saw last week',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='c).Last week you saw it',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)
    Button(frame,width=29,pady=7,text='d).You did see it last week',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)

    Button(frame,width=29,pady=7,text='e).you saw last week',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=eng).place(x=20,y=270)
    Button(frame,width=29,pady=7,text='Finish',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=sent).place(x=50,y=320)
#------------------------------eng
#------------------------------scidt
def sci_():
    import sqlite3
    conn=sqlite3.connect("sab1.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rog1
                    (name TEXT,m INTEGER,m1 INTEGER,m2 INTEGER,m3 INTEGER,m4 INTEGER,m5 INTEGER,Phone_number INTEGER)''')
    cursor.execute("INSERT INTO rog1 (m1) VALUES ('1')")
    cursor.execute("SELECT name,COUNT(m1) FROM rog1 Order By m1")
    rows = cursor.fetchall()
    print(rows)
    conn.commit()


    import sqlite3
    import io
    import csv
    d=open('C:\\Users\\Admin\\Documents\\58.csv','w')
    c=csv.writer(d)
    connection=sqlite3.connect("sab1.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM rog1")
    co=[i[0]for i in cursor.description]
    c.writerow(co)
    data=cursor.fetchall()
    for item in data:
        c.writerow(item)
    d.close()
    

    
                
    
    with open('C:\\Users\\Admin\\Documents\\58.csv',"r",newline=None)as fd:
        r=csv.reader(fd)
        for line in fd:
            line=line.replace("\n","")
            print(line)
    for i in range( len(rows)):
        for j in range (len(rows)):
            if(rows[j][1]>=5):
                import pywhatkit
                a=pywhatkit.sendwhatmsg("+7418014335","YOU HAVE GOT ANOTHER FREE COURSE",now.hour,now.minute+2)
                print(a)

    cursor.close()
    connection.close()
#-------------------------------sciset

#------------------------------sciyu
def sci_yu():
    webbrowser.open("https://www.youtube.com/results?search_query=physics+syllabus+class+12+cbse+2022-23")
  

def yu_sci_st():
    ne=Frame(root)
    ne=Frame(root,width=2000,height=500,bg='white')
    ne.place(x=0,y=0)
    
    
    frame=Frame(ne,width=4200,height=4500,bg='pink').place(x=-100,y=-100)
    Label(ne,image=img10,bg='pink').place(x=0,y=0)
    
    label=Label(frame,text="Science",fg='black',bg='lightpink',font=('Times New Roman',40)).place(x=400,y=0)


    Button(frame,width=27,pady=7,text='Test',bg='green',font=('Times New Roman',20,'bold'),fg='white',command=disc_sc).place(x=300,y=270)
    Button(frame,width=27,pady=7,text='Videos',bg='green',font=('Times New Roman',20,'bold'),fg='white',command=sci_yu).place(x=300,y=340)
    Button(frame,width=27,pady=7,text='Back',bg='red',font=('Times New Roman',20,'bold'),fg='white',command=back).place(x=300,y=400)
    

def disc_sc():
    cu=Frame(root)
    cu=Frame(root,width=2000,height=500,bg='white')
    cu.place(x=0,y=0)
    
    
    frame=Frame(cu,width=4200,height=4500,bg='pink').place(x=-100,y=-100)
    Label(cu,image=img11,bg='pink').place(x=0,y=0)
    
    Button(frame,width=15,pady=7,text='Lets start the test!',bg='pink',font=('Times New Roman',15,'bold'),fg='black',command=sci).place(x=100,y=450)
   

#------------------------------Sciyuend
def sci():
    fun=Frame(root)
    fun=Frame(root,width=2000,height=500,bg='white')
    fun.place(x=0,y=0)
    frame=Frame(fun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(fun,image=img8,bg='lightblue').place(x=0,y=0)
    
    
    Button(frame,text='\t\tLets move on to the question!',font=('Times New Roman',25)).place(x=10,y=10)


    label=Label(frame,text="1.For light incident from air on a slab of refractive index 2,\n the maximum possible angle of refraction is",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).30^0',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=sci_).place(x=20,y=135)

    Button(frame,width=29,pady=7,text='b).40^0',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='c).50^0',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)
    Button(frame,width=29,pady=7,text='d).60^0',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)

    Button(frame,width=29,pady=7,text='e).80^0',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=270)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_s2).place(x=50,y=320)
    
def next_s2():
    pun=Frame(root)
    pun=Frame(root,width=2000,height=500,bg='white')
    pun.place(x=0,y=0)
    frame=Frame(pun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(pun,image=img8,bg='lightblue').place(x=0,y=0)
    
    label=Label(frame,text="2.When a biconvex lens of glass having refractive index 1.47 is dipped in a liquid,\n it acts as a plane sheet of glass. This implies that the liquid must have refractive index,",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Less than one',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=135)

    Button(frame,width=29,pady=7,text='b).Less than that of glass',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='c).Greater than that of glass',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)
    Button(frame,width=29,pady=7,text='d).Equal to that of glass',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=sci_).place(x=20,y=230)

    Button(frame,width=29,pady=7,text='e).All the above',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=270)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_s3).place(x=50,y=320)
    

def next_s3():
    yun=Frame(root)
    yun=Frame(root,width=2000,height=500,bg='white')
    yun.place(x=0,y=0)
    frame=Frame(yun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(yun,image=img8,bg='lightblue').place(x=0,y=0)
    
    label=Label(frame,text="3.A plane glass is placed over a various coloured letters\n (violet, green, yellow, red) The letter which appears to be raised more is",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Red',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=135)

    Button(frame,width=29,pady=7,text='b).Green',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=sci_).place(x=20,y=170)

    Button(frame,width=29,pady=7,text='c).Yellow',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)
    Button(frame,width=29,pady=7,text='d).Violet',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)

    Button(frame,width=29,pady=7,text='e).All the above',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=270)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_s4).place(x=50,y=320)
def next_s4():
    qun=Frame(root)
    qun=Frame(root,width=2000,height=500,bg='white')
    qun.place(x=0,y=0)
    frame=Frame(qun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(qun,image=img8,bg='lightblue').place(x=0,y=0)
    
    label=Label(frame,text="4.The radius of curvature of curved surface at a thin planoconvex lens is 10 cm and\n the refractive index is 1.5. If the plane surface is silvered, then the focal length will be",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Red',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=sci_).place(x=20,y=135)

    Button(frame,width=29,pady=7,text='b).Green',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='c).Yellow',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)
    Button(frame,width=29,pady=7,text='d).Violet',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)

    Button(frame,width=29,pady=7,text='e).All the above',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=270)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_s5).place(x=50,y=320)
def next_s5():
    eun=Frame(root)
    eun=Frame(root,width=2000,height=500,bg='white')
    eun.place(x=0,y=0)
    frame=Frame(eun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(eun,image=img8,bg='lightblue').place(x=0,y=0)
    
    label=Label(frame,text="5.An air bubble in glass slab of refractiveindex 1.5 (near normal incidence)\n is 5 cm deep when viewed from one surfaceand 3 cm deep\n when viewed from the opposite face. The thickness of the slab is,",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).8cm',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).10cm',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).20cm',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).15cm',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=sci_).place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).30cm',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Finish',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=sent).place(x=70,y=360)
#-------------------------sci

#-----------------------cscdt
def csc_():
    import sqlite3
    conn=sqlite3.connect("sab1.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rog1
                    (name TEXT,m INTEGER,m1 INTEGER,m2 INTEGER,m3 INTEGER,m4 INTEGER,m5 INTEGER,Phone_number INTEGER)''')
    cursor.execute("INSERT INTO rog1 (m2) VALUES ('1')")
    cursor.execute("SELECT name,COUNT(m2) FROM rog1 Order By m2")
    rows = cursor.fetchall()
    print(rows)
    conn.commit()


    import sqlite3
    import io
    import csv
    d=open('C:\\Users\\Admin\\Documents\\58.csv','w')
    c=csv.writer(d)
    connection=sqlite3.connect("sab1.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM rog1")
    co=[i[0]for i in cursor.description]
    c.writerow(co)
    data=cursor.fetchall()
    for item in data:
        c.writerow(item)
    d.close()
    

    
                
    
    with open('C:\\Users\\Admin\\Documents\\58.csv',"r",newline=None)as fd:
        r=csv.reader(fd)
        for line in fd:
            line=line.replace("\n","")
            print(line)
    for i in range( len(rows)):
        for j in range (len(rows)):
            if(rows[j][1]>=5):
                import pywhatkit
                a=pywhatkit.sendwhatmsg("+7418014335","YOU HAVE GOT ANOTHER FREE COURSE",now.hour,now.minute+2)
                print(a)

    cursor.close()
    connection.close()
#-------------------------------cscdt


def csc_yu():
    webbrowser.open("https://www.youtube.com/results?search_query=jenneys+lecture+c")
    
def yu_csc_st():
    un=Frame(root)
    un=Frame(root,width=2000,height=500,bg='white')
    un.place(x=0,y=0)
        
    frame=Frame(un,width=4200,height=4500,bg='pink').place(x=-100,y=-100)
    Label(un,image=img10,bg='pink').place(x=0,y=0)
    
    label=Label(frame,text="Computer science!",fg='black',bg='lightpink',font=('Times New Roman',40)).place(x=400,y=0)


    Button(frame,width=27,pady=7,text='Test',bg='green',font=('Times New Roman',20,'bold'),fg='white',command=disc_csc).place(x=300,y=270)
    Button(frame,width=27,pady=7,text='Videos',bg='green',font=('Times New Roman',20,'bold'),fg='white',command=csc_yu).place(x=300,y=340)
    Button(frame,width=27,pady=7,text='Back',bg='red',font=('Times New Roman',20,'bold'),fg='white',command=back).place(x=300,y=400)
    
    
def disc_csc():
    un=Frame(root)
    un=Frame(root,width=2000,height=500,bg='white')
    un.place(x=0,y=0)
    
    
    frame=Frame(un,width=4200,height=4500,bg='pink').place(x=-100,y=-100)
    Label(un,image=img11,bg='pink').place(x=0,y=0)
    
    Button(frame,width=15,pady=7,text='Lets start the test!',bg='pink',font=('Times New Roman',15,'bold'),fg='black',command=csc).place(x=100,y=450)
#------------------------endcsc    

#-------------------------csc
def csc():
    xun=Frame(root)
    xun=Frame(root,width=2000,height=500,bg='white')
    xun.place(x=0,y=0)
    frame=Frame(xun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(xun,image=img9,bg='lightblue').place(x=0,y=0)
    
    Button(frame,text='\t\tLets move on to the question!',font=('Times New Roman',25)).place(x=10,y=10)


    label=Label(frame,text="1.What error occurs when you execute the following Python code snippet? apple = mango",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Syntaxerror',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Nameerror',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=csc_).place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).Valueerror',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Typeerror',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).All the above',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_cs1).place(x=70,y=360)

def next_cs1():
    oun=Frame(root)
    oun=Frame(root,width=2000,height=500,bg='white')
    oun.place(x=0,y=0)
    frame=Frame(oun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(oun,image=img9,bg='lightblue').place(x=0,y=0)
    
    label=Label(frame,text="2.Which of the following can be used as valid variable identifier(s) in Python?",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Total',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).7salute',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).question',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Typeerror',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=csc_).place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).global',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_cs2).place(x=70,y=360)

    
def next_cs2():
    lun=Frame(root)
    lun=Frame(root,width=2000,height=500,bg='white')
    lun.place(x=0,y=0)
    frame=Frame(lun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(lun,image=img9,bg='lightblue').place(x=0,y=0)
    
    label=Label(frame,text="3.Which of the following forces an expression to be converted into specific type?",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Implicit type casting ',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Mutable type casting',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).Immutable type casting',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Explicit type casting',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).All the above',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=csc_).place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_cs3).place(x=70,y=360)

def next_cs3():
    xun=Frame(root)
    xun=Frame(root,width=2000,height=500,bg='white')
    xun.place(x=0,y=0)
    frame=Frame(xun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(xun,image=img9,bg='lightblue').place(x=0,y=0)
    label=Label(frame,text="4.Which point can be considered as difference between string and list?",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Length',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Mutability',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).Index and slicing',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=csc_).place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Acessing indidual elements',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).None',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_cs4).place(x=70,y=360)

def next_cs4():
    sn=Frame(root)
    sn=Frame(root,width=2000,height=500,bg='white')
    sn.place(x=0,y=0)
    frame=Frame(sn,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(sn,image=img9,bg='lightblue').place(x=0,y=0)
    label=Label(frame,text="5.The variable declared inside the function is called a variable",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Global',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Local',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).External',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Built in',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).None',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=csc_).place(x=20,y=290)
    
    Button(frame,width=29,pady=7,text='Finish',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=end).place(x=70,y=360)
#--------------------------------cs
#------------------------------mathdt
def math_():
    import sqlite3
    conn=sqlite3.connect("sab1.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rog1
                    (name TEXT,m INTEGER,m1 INTEGER,m2 INTEGER,m3 INTEGER,m4 INTEGER,m5 INTEGER,Phone_number INTEGER)''')
    cursor.execute("INSERT INTO rog1 (m3) VALUES ('1')")
    cursor.execute("SELECT name,COUNT(m3) FROM rog1 Order By m3")
    rows = cursor.fetchall()
    print(rows)
    conn.commit()


    import sqlite3
    import io
    import csv
    d=open('C:\\Users\\Admin\\Documents\\58.csv','w')
    c=csv.writer(d)
    connection=sqlite3.connect("sab1.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM rog1")
    co=[i[0]for i in cursor.description]
    c.writerow(co)
    data=cursor.fetchall()
    for item in data:
        c.writerow(item)
    d.close()
    

    
                
    
    with open('C:\\Users\\Admin\\Documents\\58.csv',"r",newline=None)as fd:
        r=csv.reader(fd)
        for line in fd:
            line=line.replace("\n","")
            print(line)
    for i in range( len(rows)):
        for j in range (len(rows)):
            if(rows[j][1]>=5):
                import pywhatkit
                a=pywhatkit.sendwhatmsg("+7418014335","YOU HAVE GOT ANOTHER FREE COURSE",now.hour,now.minute+2)
                print(a)

    cursor.close()
    connection.close()
#--------------------------------matdtend
#--------------------------------matyu
def mat_yu():
    webbrowser.open("https://www.youtube.com/results?search_query=ram+maths")
    
def yu_mat_st():
    mm=Frame(root)
    mm=Frame(root,width=2000,height=500,bg='white')
    mm.place(x=0,y=0)
        
    frame=Frame(mm,width=4200,height=4500,bg='pink').place(x=-100,y=-100)
    Label(mm,image=img10,bg='pink').place(x=0,y=0)
    
    label=Label(frame,text="Maths!",fg='black',bg='lightpink',font=('Times New Roman',40)).place(x=400,y=0)

    Button(frame,width=27,pady=7,text='Test',bg='green',font=('Times New Roman',20,'bold'),fg='white',command=disc_mat).place(x=300,y=270)
    Button(frame,width=27,pady=7,text='Videos',bg='green',font=('Times New Roman',20,'bold'),fg='white',command=mat_yu).place(x=300,y=340)
    
def disc_mat():
    mm=Frame(root)
    mm=Frame(root,width=2000,height=500,bg='white')
    mm.place(x=0,y=0)
        
    frame=Frame(mm,width=4200,height=4500,bg='pink').place(x=-100,y=-100)
    Label(mm,image=img11,bg='pink').place(x=0,y=0)
    
    Button(frame,width=15,pady=7,text='Lets start the test!',bg='pink',font=('Times New Roman',15,'bold'),fg='black',command=math).place(x=100,y=450)
#--------------------------matendyu
    
#--------------------------maths
def math():
    cun=Frame(root)
    cun=Frame(root,width=2000,height=500,bg='white')
    cun.place(x=0,y=0)
    frame=Frame(cun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(cun,image=img6,bg='lightblue').place(x=0,y=0)
    
    Button(frame,text='\t\tLets move on to the question!',font=('Times New Roman',25)).place(x=10,y=10)


    label=Label(frame,text="1.A relation R in a set A is called ___, if (a1, a2) ∈ R implies (a2, a1) ∈ R, for all a1, a2 ∈ A.",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Symmetric',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=math_).place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Transitive',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).Equivalence',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Non_symmetric',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).All the above',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_m1).place(x=70,y=360)

def next_m1():
    nun=Frame(root)
    nun=Frame(root,width=2000,height=500,bg='white')
    nun.place(x=0,y=0)
    frame=Frame(nun,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(nun,image=img6,bg='lightblue').place(x=0,y=0)
    
    label=Label(frame,text="2.Let R be a relation on the set N of natural numbers defined by nRm if n divides m. Then R is ",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Reflexive and symmetric',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Transitive and symmetric',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=math_).place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).Equivalence',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Reflexive, transitive but not symmetric',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).None',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_m2).place(x=70,y=360)


def next_m2():
    cum=Frame(root)
    cum=Frame(root,width=2000,height=500,bg='white')
    cum.place(x=0,y=0)
    frame=Frame(cum,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(cum,image=img6,bg='lightblue').place(x=0,y=0)
    
    label=Label(frame,text="3.The maximum number of equivalence relations on the set A = {1, 2, 3} are",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).1',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).2',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).3',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=math_).place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).5',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).All the above',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_m3).place(x=70,y=360)
def next_m3():
    cuy=Frame(root)
    cuy=Frame(root,width=2000,height=500,bg='white')
    cuy.place(x=0,y=0)
    frame=Frame(cuy,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(cuy,image=img6,bg='lightblue').place(x=0,y=0)
    
    label=Label(frame,text="4.If set A contains 5 elements and the set B contains 6 elements, then the number of one-one and onto mappings from A to B is",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).720',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).120',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).0',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).100',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).None',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=math_).place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_m4).place(x=70,y=360)


def next_m4():
    cuz=Frame(root)
    cuz=Frame(root,width=2000,height=500,bg='white')
    cuz.place(x=0,y=0)
    frame=Frame(cuz,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(cuz,image=img6,bg='lightblue').place(x=0,y=0)
    
    
    label=Label(frame,text="5.Let f : [2, ∞) → R be the function defined by f(x) = x2 – 4x + 5, then the range of f is",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).[1, ∞)',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).[4, ∞)',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).R',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).[5, ∞)',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).[9, ∞)',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=math_).place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Finish',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=sent).place(x=70,y=360)

#------------------------math
#------------------------jeedtst
def jee_():
    import sqlite3
    conn=sqlite3.connect("sab1.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rog1
                    (name TEXT,m INTEGER,m1 INTEGER,m2 INTEGER,m3 INTEGER,m4 INTEGER,m5 INTEGER,Phone_number INTEGER)''')
    cursor.execute("INSERT INTO rog1 (m4) VALUES ('1')")
    cursor.execute("SELECT name,COUNT(m4) FROM rog1 Order By m4")
    rows = cursor.fetchall()
    print(rows)
    conn.commit()


    import sqlite3
    import io
    import csv
    d=open('C:\\Users\\Admin\\Documents\\58.csv','w')
    c=csv.writer(d)
    connection=sqlite3.connect("sab1.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM rog1")
    co=[i[0]for i in cursor.description]
    c.writerow(co)
    data=cursor.fetchall()
    for item in data:
        c.writerow(item)
    d.close()
    

    
                
    
    with open('C:\\Users\\Admin\\Documents\\58.csv',"r",newline=None)as fd:
        r=csv.reader(fd)
        for line in fd:
            line=line.replace("\n","")
            print(line)
    for i in range( len(rows)):
        for j in range (len(rows)):
            if(rows[j][1]>=5):
                import pywhatkit
                a=pywhatkit.sendwhatmsg("+7418014335","YOU HAVE GOT ANOTHER FREE COURSE",now.hour,now.minute+2)
                print(a)

    cursor.close()
    connection.close()
#-----------------------jeedtend
#------------------------jeeyu
def jee_yu():
    webbrowser.open("https://www.youtube.com/@AmanDhattarwal")
    
def yu_jee_st():
    nn=Frame(root)
    nn=Frame(root,width=2000,height=500,bg='white')
    nn.place(x=0,y=0)
    
    
    frame=Frame(nn,width=4200,height=4500,bg='pink').place(x=-100,y=-100)
    Label(nn,image=img10,bg='pink').place(x=0,y=0)
    
    label=Label(frame,text="JEE!",fg='black',bg='lightpink',font=('Times New Roman',40)).place(x=400,y=0)


    Button(frame,width=27,pady=7,text='Test',bg='green',font=('Times New Roman',20,'bold'),fg='white',command=disc_jee).place(x=300,y=270)
    Button(frame,width=27,pady=7,text='Videos',bg='green',font=('Times New Roman',20,'bold'),fg='white',command=jee_yu).place(x=300,y=340)
    Button(frame,width=27,pady=7,text='Back',bg='red',font=('Times New Roman',20,'bold'),fg='white',command=back).place(x=300,y=400)
    
    
def disc_jee():
    nn=Frame(root)
    nn=Frame(root,width=2000,height=500,bg='white')
    nn.place(x=0,y=0)
    
    
    frame=Frame(nn,width=4200,height=4500,bg='pink').place(x=-100,y=-100)
    Label(nn,image=img11,bg='pink').place(x=0,y=0)
    
    Button(frame,width=15,pady=7,text='Lets start the test!',bg='pink',font=('Times New Roman',15,'bold'),fg='black',command=JEE).place(x=100,y=450)
    
#------------------------jeeyuend

#------------------------jee
def JEE():
    we=Frame(root)
    we=Frame(root,width=2000,height=500,bg='white')
    we.place(x=0,y=0)
    frame=Frame(we,width=4200,height=4500,bg='blue').place(x=-100,y=-100)
    
    Button(frame,text='\t\tLets move on to the question!',font=('Times New Roman',25)).place(x=10,y=10)
    Label(we,image=img7,bg='lightblue').place(x=0,y=0)


    #Button(Frame,text='\t\tLets move on to the question!',font=('Times New Roman',25)).grid(row=0,column=0,pady=10,padx=0)

    label=Label(frame,text="1.What error occurs when you execute the following Python code snippet? apple = mango",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Syntaxerror',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=jee_).place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Nameerror',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).Valueerror',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).All the above',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).Typeerror',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_j1).place(x=70,y=360)

def  next_j1():
    er=Frame(root)
    er=Frame(root,width=2000,height=500,bg='white')
    er.place(x=0,y=0)
    frame=Frame(er,width=4200,height=4500,bg='blue').place(x=-100,y=-100)
    Label(er,image=img7,bg='lightblue').place(x=0,y=0)
    label=Label(frame,text="2.Which of the following can be used as valid variable identifier(s) in Python?",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Total',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).7salute',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).Question',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=jee_).place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Global',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).None',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_j2).place(x=70,y=360)

def  next_j2():
    cuv=Frame(root)
    cuv=Frame(root,width=2000,height=500,bg='white')
    cuv.place(x=0,y=0)
    frame=Frame(cuv,width=4200,height=4500,bg='blue').place(x=-100,y=-100)
    Label(cuv,image=img7,bg='lightblue').place(x=0,y=0)
    label=Label(frame,text="3.Which of the following forces an expression to be converted into specific type?",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a) Implicit type casting',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Mutable type casting',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).Immutable type casting',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=jee_).place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Explicit type casting',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).All the above',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_j3).place(x=70,y=360)

def  next_j3():
    cuu=Frame(root)
    cuu=Frame(root,width=2000,height=500,bg='white')
    cuu.place(x=0,y=0)
    frame=Frame(cuu,width=4200,height=4500,bg='blue').place(x=-100,y=-100)
    Label(cuu,image=img7,bg='lightblue').place(x=0,y=0)
    label=Label(frame,text="4.Which point can be considered as difference between string and list?",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Length',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Mutability',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).Index and slicing',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Acessing indidual elements',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).None',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=jee_).place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_j4).place(x=70,y=360)

def next_j4():
    cut=Frame(root)
    cut=Frame(root,width=2000,height=500,bg='white')
    cut.place(x=0,y=0)
    frame=Frame(cut,width=4200,height=4500,bg='blue').place(x=-100,y=-100)
    Label(cut,image=img7,bg='lightblue').place(x=0,y=0)
    label=Label(frame,text="5.The variable declared inside the function is called a variable",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Global',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Local',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).External',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Built in',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=jee_).place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).None',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=sent).place(x=70,y=360)  

#-------------------------------jeeend
#-------------------------------neetdtst
def neet_():
    import sqlite3
    conn=sqlite3.connect("sab1.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rog1
                    (name TEXT,m INTEGER,m1 INTEGER,m2 INTEGER,m3 INTEGER,m4 INTEGER,m5 INTEGER,Phone_number INTEGER)''')
    cursor.execute("INSERT INTO rog1 (m5) VALUES ('1')")
    cursor.execute("SELECT name,COUNT(m5) FROM rog1 Order By m5")
    rows = cursor.fetchall()
    print(rows)
    conn.commit()


    import sqlite3
    import io
    import csv
    d=open('C:\\Users\\Admin\\Documents\\58.csv','w')
    c=csv.writer(d)
    connection=sqlite3.connect("sab1.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM rog1")
    co=[i[0]for i in cursor.description]
    c.writerow(co)
    data=cursor.fetchall()
    for item in data:
        c.writerow(item)
    d.close()
    

    
                
    
    with open('C:\\Users\\Admin\\Documents\\58.csv',"r",newline=None)as fd:
        r=csv.reader(fd)
        for line in fd:
            line=line.replace("\n","")
            print(line)
    for i in range( len(rows)):
        for j in range (len(rows)):
            if(rows[j][1]>=5):
                import pywhatkit
                a=pywhatkit.sendwhatmsg("+7418014335","YOU HAVE GOT ANOTHER FREE COURSE",now.hour,now.minute+2)
                print(a)

    cursor.close()
    connection.close()

#-----------------------------neetdtend

def neet_yu():
    webbrowser.open("https://www.youtube.com/watch?v=WeJtc2EPW_0")
    
def yu_neet_st():
    er=Frame(root)
    er=Frame(root,width=2000,height=500,bg='white')
    er.place(x=0,y=0)
    
    
    frame=Frame(er,width=4200,height=4500,bg='pink').place(x=-100,y=-100)
    Label(er,image=img10,bg='pink').place(x=0,y=0)
    
    label=Label(frame,text="NEET!",fg='black',bg='lightpink',font=('Times New Roman',40)).place(x=400,y=0)


    Button(frame,width=27,pady=7,text='Test',bg='green',font=('Times New Roman',20,'bold'),fg='white',command=disc_neet).place(x=300,y=270)
    Button(frame,width=27,pady=7,text='Videos',bg='green',font=('Times New Roman',20,'bold'),fg='white',command=neet_yu).place(x=300,y=340)
    Button(frame,width=27,pady=7,text='Back',bg='red',font=('Times New Roman',20,'bold'),fg='white',command=back).place(x=300,y=400)
    
def disc_neet():
    er=Frame(root)
    er=Frame(root,width=2000,height=500,bg='white')
    er.place(x=0,y=0)
    
    
    frame=Frame(er,width=4200,height=4500,bg='pink').place(x=-100,y=-100)
    Label(er,image=img11,bg='pink').place(x=0,y=0)
    
    Button(frame,width=15,pady=7,text='Lets start the test!',bg='pink',font=('Times New Roman',15,'bold'),fg='black',command=NEET).place(x=100,y=450)
    

#-------------------------------neet
def NEET():
    o=Frame(root)
    o=Frame(root,width=2000,height=500,bg='white')
    o.place(x=0,y=0)
    frame=Frame(o,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    
    frame=Frame(o,width=4200,height=4500,bg='lightblue').place(x=-100,y=-100)
    Label(o,image=img5,bg='lightblue').place(x=0,y=0)
    
    Button(frame,text='\t\tLets move on to the question!',font=('Times New Roman',25)).place(x=10,y=10)

    
    label=Label(frame,text="1.Alternative forms of a gene are called ____",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text='a).Loci',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Multiples',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=neet_).place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).Chromosomes',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Single',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='All the above',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_n1).place(x=70,y=360)  

def next_n1():
    cur=Frame(root)
    cur=Frame(root,width=2000,height=500,bg='white')
    cur.place(x=0,y=0)
    frame=Frame(cur,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(cur,image=img5,bg='lightblue').place(x=0,y=0)
    
    #Button(frame,text='\t\tLets move on to the question!',font=('Times New Roman',25)).grid(row=0,column=0,pady=10,padx=0)

    label=Label(frame,text="2. Heredity or inheritance of specific traits became clearer due to",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text="a).Lamarck's",bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Harwinism',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text='c).Darwinism',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Neo-Darwinism',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).None',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=neet_).place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_n2).place(x=70,y=360)  

def next_n2():
    cuq=Frame(root)
    cuq=Frame(root,width=2000,height=500,bg='white')
    cuq.place(x=0,y=0)
    frame=Frame(cuq,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(cuq,image=img5,bg='lightblue').place(x=0,y=0)
    
    #Button(frame,text='\t\tLets move on to the question!',font=('Times New Roman',25)).grid(row=0,column=0,pady=10,padx=0)

    label=Label(frame,text="3.Which of the following sentences is true about the evolutionary process?",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text="a).There is no real 'progress' in the idea of evolution",bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Humans are unique, a totally new type of organism.',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=neet_).place(x=20,y=200)

    Button(frame,width=29,pady=7,text="c).Progress is nature 's religion",bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Evolution of life forms was rapid in the beginning ages. ',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).Similarities in organ structure.',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_n3).place(x=70,y=360)  

def next_n3():
    cuo=Frame(root)
    cuo=Frame(root,width=2000,height=500,bg='white')
    cuo.place(x=0,y=0)
    frame=Frame(cuo,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    #Button(frame,text='\t\tLets move on to the question!',font=('Times New Roman',25)).grid(row=0,column=0,pady=10,padx=0)
    Label(cuo,image=img5,bg='lightblue').place(x=0,y=0)
    

    label=Label(frame,text="4.Microevolution takes place due to ",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text="a).Somatogenic variation",bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Blastogenic variation ',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=200)

    Button(frame,width=29,pady=7,text="c).Index and slicing",bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=neet_).place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).Acessing indidual elements',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).None',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Next',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=next_n4).place(x=70,y=360)  
def next_n4():
    cup=Frame(root)
    cup=Frame(root,width=2000,height=500,bg='white')
    cup.place(x=0,y=0)
    frame=Frame(cup,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    Label(cup,image=img5,bg='lightblue').place(x=0,y=0)
    
    #Button(frame,text='\t\tLets move on to the question!',font=('Times New Roman',25)).grid(row=0,column=0,pady=10,padx=0)

    label=Label(frame,text="5.The difference between Homo sapiens and the Homo erectus was __.",fg='black',bg='white',font=('Times New Roman',18)).place(x=20,y=80)


    Button(frame,width=29,pady=7,text="a).Homo sapiens originated in Africa while Homo erectus was in Asia",bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=170)

    Button(frame,width=29,pady=7,text='b).Homo erectus were much smaller in size than homo sapiens.',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white',command=neet_).place(x=20,y=200)

    Button(frame,width=29,pady=7,text="c).Homo erectus stayed in Africa while Homo sapiens did not.",bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=230)
    Button(frame,width=29,pady=7,text='d).The size of their brain of Homo eructus was smaller to homo sapiens',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=260)

    Button(frame,width=29,pady=7,text='e).None',bg='#57a1f8',font=('Times New Roman',10,'bold'),fg='white').place(x=20,y=290)
    Button(frame,width=29,pady=7,text='Finish',bg='red',font=('Times New Roman',10,'bold'),fg='white',command=sent).place(x=70,y=360)



    
def sent():
    wee=Frame(root)
    wee=Frame(root,width=2000,height=500,bg='white')
    wee.place(x=0,y=0)
    frame=Frame(wee,width=4200,height=4500,bg='white').place(x=-100,y=-100)
    #Label(wee,image=img5,bg='lightblue').place(x=0,y=0)
    Label(wee,image=img9,bg='lightblue').place(x=0,y=0)
    
    label=Label(wee,text="Your message successfully sent !!",fg='black',bg='lightblue',font=('Times New Roman',30)).place(x=200,y=170)
    Button(frame,width=29,pady=7,text='Back',bg='pink',font=('Times New Roman',10,'bold'),fg='black',command=back).place(x=250,y=240)

    
    

    
    
    
 

def indicate(lb,page):
    hide_indicators()
    lb.config(bg="blue")
    dey()
    page()
    #root.mainloop()
