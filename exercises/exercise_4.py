number = int(input("please enter in a  digit number: "))

num1 = number//1000
num2 = (number//100)%10
num3 = (number//10)%10
num4 = (number%10)
if num1 == num4 and num2 == num3:
    print("1")
else:
    print("0")