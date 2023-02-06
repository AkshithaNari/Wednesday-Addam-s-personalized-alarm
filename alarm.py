import datetime
from playsound import playsound
alarmHour = int(input("Enter Hour: "))
alarmMin = int(input("Enter Minutes: "))
alarmAm = input("am / pm: ")

if alarmAm=="pm":
  alarmHour+=12

while True:
  if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
      print("Time's up Wednesday")
      playsound("bloody mary.mp3")
      break