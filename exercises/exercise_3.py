seconds = int(input("please enter the amount of seconds that has passed: "))
sec = seconds % 60
minutes = (seconds//60)%60
hour = (seconds//3600)%24
print(f"{hour}:{minutes:02d}:{sec:02d}")