## Author: Francisco Bumanglag
## Project: Things.txt Read File
## Assignment: Module 3 Project 2
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 26, 2023


def read():

    infile = open("things.txt", "r")                    #variable / open 
    filecontents = infile.read()                        #variable / read
    infile.close()                                      #cloase close 
    print(filecontents)                                 #print file contents
    print("Reading data entered completed.")            #confirmation

read() 
