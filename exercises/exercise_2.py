number = int(input("input an integer: "))

num1 = (number % 2)
num2 = (number//2)
if num1 == 1:
    num2 = num2*2+2
    print(f"{num2}")
else:
    print(number*2)