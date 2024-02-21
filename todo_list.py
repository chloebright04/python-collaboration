#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:38:41 2024

@author: chloebright
"""

def main():
    myTasks= {}
    
        
    
    
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