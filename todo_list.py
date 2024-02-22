#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:38:41 2024

@author: chloebright
"""

def main(): #the main function 
    myTasks= {} #empty dictionary to hold keys (the tasks) and their values (complete/incomplete)
    cont = 'y' #character that user will update periodically to either continue or terminate the program
    
    #while loop for while cont is y 
    while cont == 'y':
        if len(myTasks)==0: #when there are no entries in the dictionary
            print("Welcome to your to-do list. It is currently empty. Enter a task to begin.") #introduces the user to the program 
            myTasks = addTask(myTasks) #calls addTask function on the (currently) empty dictionary 
            print("Here is your current to-do list: ", viewTasks(myTasks)) #displays the curent dictionary with the newly added task
            cont = input("Would you like to continue? Enter y for yes, n for no:   ") #prompts user to enter whether they would like to continue or end the program 
        else: #when there are more than one entry in the dictionary 
            choice = input("""Enter the appropriate character for the action you would like to complete:
    a to add a task
    d to delete a task
    v to view your tasks
    c to mark a task as complete:\n
                       """) #asks user what they would like to do with their to-do list, giving them the characters to enter for each available action 
            if choice == 'a': #calls addTask on the dictionary of tasks if user enters a and displays the updated dictionary 
                addTask(myTasks)
                print("Here is your updated to-do list: ", viewTasks(myTasks))
            elif choice == 'd': #calls deleteTask on the dictionary of tasks if the user enters d and displays the updated dictionary 
                deleteTask(myTasks)
                print("Here is your updated to-do list: ", viewTasks(myTasks))
            elif choice == 'v': #calls viewTasks on the dict of tasks if user enters v and displays the updated dictionary 
                print("Here is your current to-do list: ", viewTasks(myTasks))
            elif choice == 'c':
                markComplete(myTasks)
                print("Here is your updated to-do list: ", viewTasks(myTasks))
            cont = input("Would you like to continue? Enter y for yes, n for no:   ") #asks user to enter whether they would like to continue or quit 
    print("Thank you for using your to-do list. Here is your final list of tasks: \n", viewTasks(myTasks)) #prints final to-do list once while loop ends 
    
        
    
    
def addTask(tasks):#takes in a dictionary 
    newTask = input("Enter your task here:   ") #prompts user to enter new task for their to do list 
    tempdic = {newTask : "incomplete"} # initializes a dictionary with the user entered task and assumes that the added task is incomplete
    tasks.update(tempdic) #updates the dictionary from the argument 
    return tasks #returns the updated dict

def deleteTask(tasks):#takes in a dictionary 
    badTask = input("Enter the task you would like to remove:   ") #prompts user to enter the task they would like to remove from their to do list 
    tasks.pop(badTask) #pops the entered task from the dictionary 
    return tasks #returns popped dictionary 

def viewTasks(tasks):#takes in a dictionary as its arguemnt 
    return tasks #returns the given dictionary 

def markComplete(tasks): # takes in a dictionary as its argument 
    completeTask = input("Enter the task that you would like to mark as complete:   ") #prompts user to enter the task that they would like to mark as complete
    tempdic = {completeTask:"complete"} #creates temp dictionary with the user entered task with 'complete' as its value, rather than 'incomplete'
    tasks.update(tempdic) #updates the dictionary from the argument
    return tasks #returns the updated dict 
    

main() #calls the main fucntion 