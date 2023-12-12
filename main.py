"""
Program: GUI project, Body Mass Index (BMI) calculator
Author: Carlos Lizarazu
Date: 12/07/2023
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
#create the window
indexwindow = Tk()
indexwindow.title("Index")
indexwindow.geometry("400x500")
indexwindow.config(bg="#07EC53")
#create a global function
def callback(input):
  if input.isdigit():
    return "number"
  else:
    return "empty"

#create another global function
def findage(edad):
  if edad <= 25:
    return "young"
  elif edad >= 26 and edad<=44:
    return "adult"
  else:
    return "senior"

#function for kg and cm
def calculatekgcm(weightkg,heightcm):
  metros=heightcm*(1/100)
  bmikg = weightkg/(metros**2)
  bmikg = round(bmikg,2)
  return bmikg

#function for lb and in
def calculatelbin(weightlb,feet, inches):
  heightin= (feet*12) + inches 
  bmilb = (weightlb*703)/(heightin**2)
  bmilb = round(bmilb,2) 
  return bmilb
""" This session is for the frames"""
#This frame is for the logo
logoframe = Frame(indexwindow)
logoframe.grid(row=0,column=5, rowspan=10, columnspan=5)
logoframe.config(bg="#07EC53")

#add the Image
img = ImageTk.PhotoImage(Image.open("logo.png"))
logo = Label(logoframe, image=img)
logo.grid(row=0, column=5, padx=30)

#This frame is for the info
infoframe = Frame(indexwindow)
infoframe.grid(row=12, column=5)
infoframe.config(bg="#07EC53")

#add the label name
name = Label(infoframe, text="Welcome to the Health & Happy app")
name.grid(row=0, column=2, pady=10, padx=10)
name.config(bg="#07EC53")

#add the label age
age = Label(infoframe, text="Age" )
age.grid(row=3, column=0, pady=10, padx=15)
age.config(bg="#07EC53")
#add the box age
enterage = Entry(infoframe, width=25)
enterage.grid(row=3, column=2)
enterage.config(bg='white')

#This frame is for the buttons
buttonframe = Frame(indexwindow)
buttonframe.grid(row=14, column=5)
buttonframe.config(bg="#07EC53")

"""We are going to create new windows"""

#function for the kilo and centimeter window
def kgwindow():
  agevalidation= callback(enterage.get())
  if agevalidation!="number" or agevalidation=="empty":
    messagebox.showinfo("Warning", "Age cannot be empty or must be a number")
  else:
    window1= Toplevel()
    window1.title("Kg/cm")
    window1.config(bg="#1FFFEE") 

    
    #This frame is for the img
    frameimg1 = Frame(window1)
    frameimg1.grid(row=7,column=5, rowspan=10, columnspan=5)
    frameimg1.config(bg="#1FFFEE")
    #add the label img
    picture1 = ImageTk.PhotoImage(Image.open("gym.jpg"))
    gym1 = Label(frameimg1, image=picture1)
    gym1.image = picture1
    gym1.grid(row=0, column=5, padx=40)
    #add the button for back
    backb = Button(frameimg1, text="BACK", bg="#17008B", fg="White",
                   command=window1.destroy)
    backb.grid(row=0, column=6)
  
    #This frame is for the info
    infoframe1 = Frame(window1)
    infoframe1.grid(row=20, column=7)
    infoframe1.config(bg="#1FFFEE")
    #add the label weight
    weightkg = Label(infoframe1, text="Weight (kg)")
    weightkg.grid(row=0, column=0, pady=10, padx=20)
    weightkg.config(bg="#1FFFEE")
    #add the box weight
    enterweightkg = Entry(infoframe1, width=10)
    enterweightkg.grid(row=0, column=2, padx=20)
    enterweightkg.config(bg='white')
  
    #add the label height
    heightcm = Label(infoframe1, text="Height (cm)" )
    heightcm.grid(row=3, column=0, pady=10)
    heightcm.config(bg="#1FFFEE")
    #add the box height
    enterheightcm = Entry(infoframe1, width=10)
    enterheightcm.grid(row=3, column=2, padx=20)
    enterheightcm.config(bg='white')
    
  
    """This seccion is for the buttons"""
  
    #This frame is fort the last button
    lastframe= Frame(window1)
    lastframe.grid(column=5, rowspan=40, columnspan=40)
    lastframe.config(bg="#1FFFEE")
  
    # create de function
    def validation1():
      weightvalidation = callback(enterweightkg.get())
      heightvalidation = callback(enterheightcm.get())
      if weightvalidation=="empty" or heightvalidation=="empty":
        messagebox.showinfo("Warning", "You need fill out all the boxes")
      elif weightvalidation!="number" or heightvalidation!="number":
        messagebox.showinfo("Warning", "You need to imput a number in weight and height")
      else:
        bmikg = calculatekgcm(int(enterweightkg.get()),int(enterheightcm.get()))
        text = Label(lastframe, text="Your Body Mass Index is: ")
        text.grid(row=0, column= 2, padx=10)
        text.config(bg="#1FFFEE", fg="black")
        resultkg = Label(lastframe, text= bmikg)
        resultkg.grid(row=0, column= 4, padx=10)
        resultkg.config(bg="#1FFFEE", fg="black")
    #Button to calculate de BMI
    calcbutton= Button(lastframe, text="Calculate your BMI", command=validation1,
                       bg="#17008B", fg="White")
    calcbutton.grid(row=0, column=0, pady=20)
    
    """Functions over/under weight or regular"""

    #def weight function
    def ourkg():
      weightvalidation = callback(enterweightkg.get())
      heightvalidation = callback(enterheightcm.get())
      if weightvalidation=="empty" or heightvalidation=="empty":
        messagebox.showinfo("Warning", "You need fill out all the boxes")
      elif weightvalidation!="number" or heightvalidation!="number":
        messagebox.showinfo("Warning", "You need to imput a number in weight and height")
      else:
        bmiourkg = calculatekgcm(int(enterweightkg.get()),int(enterheightcm.get()))
        fage1 = findage(int(enterage.get()))
        if fage1 == "young":
          if bmiourkg <= 20:
            resultourkg = Label(lastframe, text= "You are underweight",bg="#1FFFEE", fg="black")
            resultourkg.grid(row=2, column= 2, padx=10)
          elif bmiourkg >= 25:
            resultourkg = Label(lastframe, text= "You are overweight",bg="#1FFFEE", fg="black")
            resultourkg.grid(row=2, column= 2, padx=10)
          else:
            resultourkg = Label(lastframe, text= "You are regular",bg="#1FFFEE", fg="black")
            resultourkg.grid(row=2, column= 2, padx=10)
        elif fage1 == "adult":
          if bmiourkg <= 21:
            resultourkg = Label(lastframe, text= "You are underweight",bg="#1FFFEE", fg="black")
            resultourkg.grid(row=2, column= 2, padx=10)
          elif bmiourkg >= 26:
            resultourkg = Label(lastframe, text= "You are overweight",bg="#1FFFEE", fg="black")
            resultourkg.grid(row=2, column= 2, padx=10)
          else:
            resultourkg = Label(lastframe, text= "You are regular",bg="#1FFFEE", fg="black")
            resultourkg.grid(row=2, column= 2, padx=10)
        else:
          if bmiourkg <= 22:
            resultourkg = Label(lastframe, text= "You are underweight",bg="#1FFFEE", fg="black")
            resultourkg.grid(row=2, column= 2, padx=10)
          elif bmiourkg >= 27:
            resultourkg = Label(lastframe, text= "You are overweight",bg="#1FFFEE", fg="black")
            resultourkg.grid(row=2, column= 2, padx=10)
          else:
            resultourkg = Label(lastframe, text= "You are regular",bg="#1FFFEE", fg="black")
            resultourkg.grid(row=2, column= 2, padx=10)
    #this Botton will tell you if you're overweight
    overbutton= Button(lastframe, text="Am I overweight/underweight/regular?", 
                       command=ourkg, bg="#17008B", fg="White")
    overbutton.grid(row=2, column=0, pady=5)


#add the button for kg and cm
kgcm = Button(buttonframe, text="Kg/cm", bg="#17008B", fg="White", command=kgwindow)
kgcm.grid(row=0, column=0, padx=30)

"""New window for pounds and inches"""
def lbwindow():
  agevalidation= callback(enterage.get())
  if agevalidation!="number" or agevalidation=="empty":
    messagebox.showinfo("Warning", "Age cannot be empty or must be a number")
  else:
    window2= Toplevel()
    window2.title("lb/in")
    window2.config(bg="#1FFFEE")

    #This frame is for the img
    frameimg2 = Frame(window2)
    frameimg2.grid(row=7,column=5, rowspan=10, columnspan=5)
    frameimg2.config(bg="#1FFFEE")
    #add the label img
    picture1 = ImageTk.PhotoImage(Image.open("gym.jpg"))
    gym1 = Label(frameimg2, image=picture1)
    gym1.image = picture1
    gym1.grid(row=0, column=5, padx=40)
    #add the button for back
    backb = Button(frameimg2, text="BACK", bg="#17008B", fg="White",
                   command=window2.destroy)
    backb.grid(row=0, column=6)

    #This frame is for the info
    infoframe2 = Frame(window2)
    infoframe2.grid(row=20, column=7)
    infoframe2.config(bg="#1FFFEE")
    #add the label weight
    weightlb = Label(infoframe2, text="Weight (pounds)")
    weightlb.grid(row=0, column=0, pady=10, padx=20)
    weightlb.config(bg="#1FFFEE")
    #add the box height
    enterweightlb = Entry(infoframe2, width=10)
    enterweightlb.grid(row=0, column=2, padx=20)
    enterweightlb.config(bg='white')

    #add the label height ft
    heightft = Label(infoframe2, text="Height (ft)" )
    heightft.grid(row=3, column=0, pady=10)
    heightft.config(bg="#1FFFEE")
    #add the box height
    enterheightft = Entry(infoframe2, width=10)
    enterheightft.grid(row=3, column=2, padx=20)
    enterheightft.config(bg='white')
    
    #add the label height in
    heightin = Label(infoframe2, text="Height (in)" )
    heightin.grid(row=5, column=0, pady=10)
    heightin.config(bg="#1FFFEE")
    #add the box height
    enterheightin = Entry(infoframe2, width=10)
    enterheightin.grid(row=5, column=2, padx=20)
    enterheightin.config(bg='white') 

    """This seccion is for the buttons"""

    #This frame is fort the last button
    lastframe2= Frame(window2)
    lastframe2.grid(column=5, rowspan=40, columnspan=40)
    lastframe2.config(bg="#1FFFEE")
    
    """This secction is fot the last buttons"""
    #funtion of the calculate button
    def validation2():
      weightvalidation = callback(enterweightlb.get())
      heightftvalidation = callback(enterheightft.get())
      heightinvalidation = callback(enterheightin.get())
      if weightvalidation=="empty" or heightftvalidation=="empty" or heightinvalidation=="empty":
          messagebox.showinfo("Warning", "You need fill out all the boxes")
      elif weightvalidation!="number" or heightftvalidation!="number" or heightinvalidation !="number":
        messagebox.showinfo("Warning", "You need to imput a number in weight and height")
      else:
        bmilb =calculatelbin(int(enterweightlb.get()),int(enterheightft.get()),
                             int(enterheightin.get())) 
        text = Label(lastframe2, text="Your Body Mass Index is: ")
        text.grid(row=0, column= 2, padx=10)
        text.config(bg="#1FFFEE", fg="black")
        resultkg = Label(lastframe2, text= bmilb)
        resultkg.grid(row=0, column= 4, padx=10)
        resultkg.config(bg="#1FFFEE", fg="black")
    #Button to calculate de BMI
    calcbutton= Button(lastframe2, text="Calculate your BMI", command=validation2,
                       bg="#17008B", fg="White")
    calcbutton.grid(row=0, column=0, pady=20)
    calcbutton.config(bg="#17008B" )


    #def weight function
    def ourlb():
      weightvalidation = callback(enterweightlb.get())
      heightftvalidation = callback(enterheightft.get())
      heightinvalidation = callback(enterheightin.get())
      if weightvalidation=="empty" or heightftvalidation=="empty" or heightinvalidation=="empty":
          messagebox.showinfo("Warning", "You need fill out all the boxes")
      elif weightvalidation!="number" or heightftvalidation!="number" or heightinvalidation !="number":
        messagebox.showinfo("Warning", "You need to imput a number in weight and height")
      else:
        bmiourlb = calculatelbin(int(enterweightlb.get()),int(enterheightft.get()),
                                 int(enterheightin.get())) 
        fage1 = findage(int(enterage.get()))
        if fage1 == "young":
          if bmiourlb <=20:
            resultourlb = Label(lastframe2, text= "You are underweight",bg="#1FFFEE", fg="black")
            resultourlb.grid(row=2, column= 2, padx=10)
          elif bmiourlb >= 25:
            resultourlb = Label(lastframe2, text= "You are overweight",bg="#1FFFEE", fg="black")
            resultourlb.grid(row=2, column= 2, padx=10)
          else:
            resultourlb = Label(lastframe2, text= "You are regular",bg="#1FFFEE", fg="black")
            resultourlb.grid(row=2, column= 2, padx=10)
        elif fage1 == "adult":
          if bmiourlb <= 21:
            resultourlb = Label(lastframe2, text= "You are underweight",bg="#1FFFEE", fg="black")
            resultourlb.grid(row=2, column= 2, padx=10)
          elif bmiourlb >= 26:
            resultourlb = Label(lastframe2, text= "You are overweight",bg="#1FFFEE", fg="black")
            resultourlb.grid(row=2, column= 2, padx=10)
          else:
            resultourlb = Label(lastframe2, text= "You are regular",bg="#1FFFEE", fg="black")
            resultourlb.grid(row=2, column= 2, padx=10)
        else:
          if bmiourlb <= 22:
            resultourlb = Label(lastframe2, text= "You are underweight",bg="#1FFFEE", fg="black")
            resultourlb.grid(row=2, column= 2, padx=10)
          elif bmiourlb >= 27:
            resultourlb = Label(lastframe2, text= "You are overweight",bg="#1FFFEE", fg="black")
            resultourlb.grid(row=2, column= 2, padx=10)
          else:
            resultourlb = Label(lastframe2, text= "You are regular",bg="#1FFFEE", fg="black")
            resultourlb.grid(row=2, column= 2, padx=10)
    #this Botton will tell you if you're overweight
    overbutton= Button(lastframe2, text="Am I overweight/underweight/regular?", 
                       bg="#17008B", fg="White", command=ourlb)
    overbutton.grid(row=2, column=0, pady=5)
#add the button for lb and in
lbin = Button(buttonframe, text="Lb/in", bg="#17008B", fg="White", command=lbwindow)
lbin.grid(row=0, column=3, padx=30)
indexwindow.mainloop()  #continous looping of main window