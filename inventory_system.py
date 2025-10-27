Skip to main content
Google Classroom
Classroom
2025 SE 5L
L
Home
Calendar
Gemini
Enrolled
To-do
D
DBMS Lab
H and L
C
Computer Network Security 2025
RR Campus
2
2025 SE 5L
L
U
UE23CS252B-1: CN
L
Archived classes
Settings
Assignment details
Lab 5: Static Code Analysis
Rajesh Banginwar FACULTY OF CSE ,PESU
•
12:08 PM
15 points
Due 1:15 PM
See the students handout for detailed instructions to complete the lab.
I will call few students randomly to come in the front and explain what they did and answer questions. So, avoid copying or using LLMs without understanding what you are submitting.

Lab_5_Static_code_analysis_Student_handout.docx
Microsoft Word

Lab 5 Submission
Google Forms

inventory_system.py
Text
Class comments
Your work
Assigned
Work cannot be turned in after the due date
Private comments
import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=[]):
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))

def removeItem(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except:
        pass

def getQty(item):
    return stock_data[item]

def loadData(file="inventory.json"):
    f = open(file, "r")
    global stock_data
    stock_data = json.loads(f.read())
    f.close()

def saveData(file="inventory.json"):
    f = open(file, "w")
    f.write(json.dumps(stock_data))
    f.close()

def printData():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def checkLowItems(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")  # invalid types, no check
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    eval("print('eval used')")  # dangerous

main()
inventory_system.py
Displaying inventory_system.py.Next