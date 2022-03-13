from tkinter import *
import random
#these are the questions
questions = [
    "Question. \n\nWhen does India celebrate Independence Day?",
    "Question. \n\nNobel prize is awarded for which of the following disciplines?",
    "Question. \n\nAt the end of March 2019, what was the amount of India's external debt?",
    "Question. \n\nIn which year was Sports Authority of India established",
    "Question. \n\nGuru Gopi Krishna is popular for which form of Indian dance?",
    "Question. \n\nThe Indian, who holds the pride of beating the computers in mathematical wizard is?",
    "Question. \n\nThe control of which state was handed over to british after marriage of King Charles 2 with portuguese princess in 1661?",                  
    "Question. \n\nIn a Database Management System(DBMS) the content and the location of data is identified by ?",
    "Question. \n\nWhich is the first search engine of the internet?",
    "Question. \n\nThe Government of which state has instituted the 'Tansen Samman'?",
    "Question. \n\nIndian player Jude Felix is popular for which sports?",
    "Question. \n\nWho is the father of geometry?",
    "Question. \n\nEntomology studies what?",
    "Question. \n\nThe Federal System in India is based on the model of which country?",
    "Question. \n\nWhat is the minimum age for becoming a member of the State Legislative Council?"
    ]
#these are options
answer_choice= [
    ["A. 15th August",
	"B. 2nd October" ,
	"C. 26th January", 
	"D. 4th July"],
    ["A. Literature, peace and economics", 
	"B. Medicine or Physiology", 
	"C. Chemistry and Physics", 
	"D. All the above"],
    ["A. US $ 540 billion", 
	"B. US $ 543 billion", 
	"C. US $ 547 billion", 
	"D. US $ 541 billion"],
    ["A. 1952", 
	"B. 1967", 
	"C. 1993",                                                                                                
	"D. 1982"],
    ["A. Bharatanatyam",
	"B. Kuchipudi",
	"C. Kathak",
	"D. Manipuri"],
    ["A. Shakuntala Devi",
	"B. Raja Ramanna",
	"C. Ramanujam",
	"D. Rina Panigrahi"],
    ["A. Cochin",
	"B. Bombay",
	"C. Surat",
	"D. Madras"],
    ["A. Subdata",
	"B. Sequence Data",
	"C. Beta Data",
	"D. Meta Data"],
    ["A. Yahoo",
	"B. Wais",
	"C. Archie",
	"D. Mozilla"],
    ["A. West Bengal",
	"B. Madhya Pradesh",
	"C. Bihar",
	"D. Gujrat"],
    ["A. Volleyball",
	"B. Football",
	"C. Hockey",
	"D. Tennis"],
    ["A. Aristotle",
	"B. Euclid",
	"C. Pythagoras",
	"D. Kepler"],
    ["A. Behavior of human beings",
	"B. Insects",
	"C. The origin and history of technical and scientific terms",
	"D. The formation of rocks"],
     ["A. Canada",
	"B. Uk",
	"C. America",
	"D. Japan"],
    ["A. 18 years",
	"B. 21 years",
	"C. 25 years",
	"D. 30 years"],
    ]
answers = [0,3,1,3,1,0,1,3,2,1,2,1,1,0,3]

user_sel = []

indexes =[]

def gen():
    global indexes
    while(len(indexes)<15):
        # creating random indexes
        x=random.randint(0,14)   
        if x in indexes:
             # checking for duplicates
            continue           
        else:
            # adding the indexes to the array
            indexes.append(x)

    

def start():
    global text
     # entering the name in the text file
    with open("users.txt", "a") as f:     
        f.write("\n"+text)
        
       
       
    global btnimage
     # creating frame 
    bg=Frame(root,bg="white")           
    bg.place(x=0,y=0,relwidth=1,relheight=1)
    frame_rules=Frame(root,bg="#00ace6")
    frame_rules.place(x=200,y=70,height=450,width=700)
    title=Label(frame_rules,text="Rules",font=("Ink free",35,"bold" ),bg="#00ace6",fg="white").place(x=80,y=30)
    # placing rules on frame
    title=Label(frame_rules,text="1. Quiz will be having 15 questions.\n"
                                  "2. For each correct answer you will be awarded 5 marks.\n"                       
                                  "4. Choose the correct answer from the four options.\n"
                                  "5. Press button to start the quiz.",

                                font=("Segoe print",15,"bold" ),bg="#00ace6",fg="white").place(x=80,y=100)
    #Calling gen method
    gen()
    #placing image on the button
    btnimage=PhotoImage(file="img1.png")
    btn=Button(frame_rules,image=btnimage,bg="#00ace6",activebackground='#00ace6',borderwidth=0,command=ques).place(x=310,y=320)
    #btn.image=photo

def showmarks(score):
    global text,bg
    #destroying the questions and options of last questions
    ques.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    back=Frame(root,bg="white")
    back.place(x=0,y=0,relwidth=1,relheight=1)
    #placing image in the last page
    bg=PhotoImage(file="congo.png")
    imglabel=Label(back,image=bg).pack()
    # displaying name
    label5=Label(back,text=text,font=("Ink Free",35),
                 bg='white',
                 fg='#00a2e8')
    label5.pack(pady=40)
    label4=Label(back,text="You Have Succefully Completed The QUIZBUZZ!!!\nYOUR SCORE",font=("Segoe print",20),
                 bg='white',
                 fg='#00a2e8')
    label4.pack()
    #displaying score
    label3=Label(
        back,
        font=("Ink free",35),
        bg='white',
        fg='#00a2e8')
    label3.pack()
    label3.config(text=score)
    label4=Label(back,text="\nShare with your friends",font=("Segoe print",20),
        bg='white',
        fg='#00a2e8')
    label4.pack()


def calc():
     global indexes,user_sel,answers
     a=0
     score=0
     for i in indexes:
         #calculating score according to the selected options
         if user_sel[a]==answers[i]:
             score=score+5
         a+=1
    # calling showmarks() to display lastpage
     showmarks(score)

q = 1
def answer():
    global radiovar,user_sel,ques,r1,r2,r3,r4,q
    # taking the selected options
    a = radiovar.get()
    #adding it to the array
    user_sel.append(a)
    #clearing the previous selected options
    radiovar.set(-1)
    if q < 15:
        # displaying the next question and options
        ques.config(text= questions[indexes[q]])
        r1['text']=answer_choice[indexes[q]][0]
        r2['text']=answer_choice[indexes[q]][1]
        r3['text']=answer_choice[indexes[q]][2]
        r4['text']=answer_choice[indexes[q]][3]
        q+=1
    else:
        # after completion of questions
        # clling calc() to calculate the score

        calc()


def ques():
    global qu
    back=Frame(root,bg="#00ace6")
    back.place(x=0,y=0,relwidth=1,relheight=1)
    # displaying the background
    qu=PhotoImage(file="ques.png")
    qulabel=Label(back,image=qu).pack()
    ex=Frame(qulabel,)
    ex.place(x=50,y=125)
    global ques,r1,r2,r3,r4
    # displaying the question
    ques = Label(
        ex,
        text = questions[indexes[0]],
        font =("Consolas",24),
        bg="#00a2e8",
        fg="white",
        justify = "center",
        wraplength = 400,
        )
    ques.pack()
    # radiovar is used in other methods
    #so making it global 
    global radiovar
    #getting the selcted options
    radiovar =IntVar()
    #clearing the selected options
    radiovar.set(-1)
    
    op1=Frame(qulabel,)
    op1.place(x=600,y=155)
    #creating option 1
    #choosing it from the array of options
    #choosing the respected options of the question
    r1 = Radiobutton(
        op1,
        text=answer_choice[indexes[0]][0],
        font=("Times",14),
        bg="#00a2e8",
        fg="white",
        activebackground="#00a2e8",
        value=0,
        variable=radiovar,
        command=answer,
        )
    r1.pack()
    
    op2=Frame(qulabel,)
    op2.place(x=600,y=248)
    #creationg option 2
    r2 = Radiobutton(
        op2,
        text=answer_choice[indexes[0]][1],
        font=("Times",14),
        bg="#00a2e8",
        fg="white",
        activebackground="#00a2e8",
        value=1,
        variable=radiovar,
        command=answer,
        )
    r2.pack()

    op3=Frame(qulabel,)
    op3.place(x=600,y=338)
    # creating option 3
    r3 = Radiobutton(
        op3,
        text=answer_choice[indexes[0]][2],
        font=("Times",14),
        bg="#00a2e8",
        fg="white",
        activebackground="#00a2e8",
        wraplength = 300,
        value=2,
        variable=radiovar,
        command=answer,
        )
    r3.pack()

    op4=Frame(qulabel,)
    op4.place(x=600,y=434)
    #creating option 4
    r4 = Radiobutton(
        op4,
        text=answer_choice[indexes[0]][3],
        font=("Times",14),
        bg="#00a2e8",
        fg="white",
        activebackground="#00a2e8",
        value=3,
        variable=radiovar,
        command=answer,
        )
    r4.pack()

def con():
    global text
    #getting the entered name
    text = txt_name.get()
    if text=="":
        #reminder
        t3=Label(Frame_login,text="Enter your Name please!!",
                 bg="#00ace6",fg="Red",font=("Segoe print",14))
        t3.place(x=125,y=280)
    else:
        # starting next page
        start()


root=Tk()
# giving title
root.title("QuizBuzz") 
root.geometry("1080x607")
# making it not able to maximize
root.resizable(False,False)
root.config(background="white")

# crating background image
bg=PhotoImage(file="img3.png")
imglabel=Label(root,image=bg).pack()
#creating frame
Frame_login=Frame(root,bg="#00ace6")
Frame_login.place(x=520,y=230,height=340,width=500)
#Declaring string variable for entered text
text=StringVar()
t1=Label(Frame_login,text="QuizzBuzz!!",font=("Ink free",35,"bold" ),bg="#00ace6",fg="white").place(x=125,y=30)
t2=Label(Frame_login,text="Enter your name here...",font=("Segoe print",15,"bold" ),bg="#00ace6",fg="white").place(x=130,y=100)
txt_name=Entry(Frame_login,textvariable=text,font=("times new roman",15),bg="white")
txt_name.place(x=105,y=170,width=305,height=35)
#creating button image
btn=PhotoImage(file="img2.png")
button=Button(Frame_login,image=btn,bg="#00ace6",activebackground="#00ace6",borderwidth=0,command=con).place(x=240,y=230)


    


       
root.mainloop()
