num1 = int(input("please input an integer: "))
num2 = int(input("please input another integer: "))
num3 = int(input("please input another integer: "))

minimum = num1*(num1<=num2 and num1<=num3)+num2*(num2<num1 and num2<num3)+num3*(num3<num2 and num3<num1)
max = num1*(num1>=num2 and num1>=num3)+num2*(num2>num1 and num2>num3)+num3*(num3>num2 and num3>num1)
middle = (num1 + num2 + num3 - minimum - max)

print(minimum)
print(middle)
print(max)