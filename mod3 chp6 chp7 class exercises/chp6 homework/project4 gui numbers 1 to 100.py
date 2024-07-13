import tkinter as tk                #import the gui interface controls 
from tkinter import messagebox      #imports the message box display 

win = tk.Tk()                       #create the window interface 
win.geometry("300x200")             #width x height in pixels
win.title ("Import the Numbers")    #label for the title 


lblNum1 = tk.Label(win,text = "list of numbers").grid(column = 0, row = 0)   #label widget



#the program reads the contents of the philosphers.txt file one line at a time 
def main():
    #open a file anme philosophers.txt
    infile = open ('numbers.txt', 'r')

    #read threee line from the file. 
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()
    line6 = infile.readline()
    line7 = infile.readline()
    line8 = infile.readline()
    line9 = infile.readline()
    line10 = infile.readline()
    

    #close the file
    infile.close()
    messagebox.showinfo("information", "Data Recorded")

def quit():
    messagebox.showinfo("information", "Thank you....")
    win.destroy()                   #close the interface

def submit():                       #function name 
    messagebox.showinfo("information", "entered :" + N1.get()

N1 = tk.StringVar()                  #the StringVar manages the Enetry Widget 
txtNumber1 = tk.Entry(win, width = 12, textvariable = N1). grid(column =1, row = 0) #text entry widget


btnQuit = tk.Button(win, text = "quit", command = quit). grid(column =1, row =8) #button widget 


#call the main function
main()
submit()
