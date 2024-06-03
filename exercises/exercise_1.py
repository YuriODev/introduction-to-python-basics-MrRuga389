number = int(input("input a 5 digit number: "))

num1 = (number//10000)
num2 = (number//1000) % 10
num3 = (number//100) % 10
num4 = (number//10) % 10
num5 = (number % 10)
num6 = (num1+num3+num5)
num7 = (num2+num4)

print(f"{num6}{num7}")