seconds = int(input("please enter the amount of seconds that has passed: "))
sec = seconds % 60
minutes = (seconds//60)%60
hour = (minutes//60)//60
print({hour},":",{minutes},":",{sec})