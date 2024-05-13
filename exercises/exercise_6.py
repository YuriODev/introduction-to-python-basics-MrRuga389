x = int(input("input a number: "))
y = int(input("input another number: "))

condition1 = (x % y)>0
condition2 = (x % y) == 0

output = condition1 * "NO" or "YES"
print(output)