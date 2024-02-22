#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:38:41 2024

@author: chloebright
"""

def main():
    myTasks= {}
    cont = 'y'
    while cont == 'y':
        if len(myTasks)==0: 
            print("Welcome to your to-do list. It is currently empty. Enter a task to begin.")
            myTasks = addTask(myTasks)
            print("Here is your current to-do list: ", viewTasks(myTasks))
            cont = input("Would you like to continue? Enter y for yes, n for no:   ")
        else:
            choice = input(""" Enter the appropriate character for the action you would like to complete:
    a to add a task
    d to delete a task
    v to view your tasks
    c to mark a task as complete:\n
                       """)
            if choice == 'a':
                addTask(myTasks)
                print("Here is your updated to-do list: ", viewTasks(myTasks))
            elif choice == 'd':
                deleteTask(myTasks)
                print("Here is your updated to-do list: ", viewTasks(myTasks))
            elif choice == 'v':
                print("Here is your current to-do list: ", viewTasks(myTasks))
            elif choice == 'c':
                markComplete(myTasks)
                print("Here is your updated to-do list: ", viewTasks(myTasks))
            cont = input("Would you like to continue? Enter y for yes, n for no:   ")
    print("Thank you for using your to-do list. Here is your final list of tasks: \n", viewTasks(myTasks))
    
        
    
    
def addTask(tasks):
    newTask = input("Enter your task here:   ")
    tempdic = {newTask : "incomplete"}
    tasks.update(tempdic)
    return tasks

def deleteTask(tasks):
    badTask = input("Enter the task you would like to remove:   ")
    tasks.pop(badTask)
    return tasks

def viewTasks(tasks):
    return tasks

def markComplete(tasks):
    completeTask = input("Enter the task that you would like to mark as complete:   ")
    tempdic = {completeTask:"complete"}
    tasks.update(tempdic)
main()