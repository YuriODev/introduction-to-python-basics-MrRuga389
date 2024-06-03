number = int(input("please enter in a 4 digit number: "))

num1 = number//1000
num2 = (number//100)%10
num3 = (number//10)%10
num4 = (number%10)
output = num1+num2+num3+num4
print(output)