import csv
from datetime import datetime
from time import time, sleep
import pandas as pd
from csv import reader


studentName = "test"

studentOut = False


##create name data list
names_data = []

##create destination data list
destination_data = []

##create time data list
time_out_data = []
time_in_data = []

def check_id():
  student_id = input("Enter the student id number:  ")
  if str(student_id) == "0":
    return 0
  else:
    df = pd.read_csv ('students.csv', header=None, sep=",")
    ##print(df)
    ##print("length = " + str(len(df)))
    student_num = int(student_id)
    print("The student is: ")
    nameString = df.loc[student_num,0]
    global studentName
    studentName = nameString
    print(studentName)
    hallPass = input("Would you like a hall pass? y/n ")
    if hallPass == "y" or "yes":
      destination = input("\nWhere is your destination?\n1. bathroom\n2. water fountain\n3. main office\n4. nurse\n5. guidance\n6. locker\n\n")
      print 
      if destination == "1":
        destination = "bathroom"
      if destination == "2":
        destination = "water fountain"
      if destination == "3":
        destination = "main office"
      if destination == "4":
        destination = "nurse" 
      if destination == "5":
        destination = "guidance office" 
      if destination == "6":
        destination = "locker" 
  
      timeStamp= datetime.now()
      names_data.append(studentName)
      destination_data.append(destination)
      time_out_data.append(timeStamp)
      studentOut = True
    if studentOut == True:
      print(studentName + " is out and left the room at " + str(timeStamp))
      returnStudent = input("Enter 'r' when the student returns ")
      if returnStudent == 'r':
        studentOut = False
        timeStamp= datetime.now()
        time_in_data.append(timeStamp)
        print(studentName + " has returned at " + str(timeStamp))
        check_id()
      else:
        print(studentName + " is out and left the room at " + str(timeStamp))
    else:
      check_id()
    if hallPass == "n":
      print("Saving data and closing session")
      exitLoop = 1
      return 0
  
def checkTime():
  timeStamp= datetime.now()
  print(timeStamp)
  return timeStamp


check_id()


timeStamp= datetime.now()
fileName = "hallPass_" + str(timeStamp) + ".csv"

with open(fileName, 'w', newline='') as f:
  writer = csv.writer(f)
  ##write headers
  writer.writerow(["name", "destination", "time_out", "time_in"])
  for w in range(len(time_out_data)):
    writer.writerow([names_data[w], destination_data[w], time_out_data[w], time_in_data[w]])