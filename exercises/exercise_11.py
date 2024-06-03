money = int(input(" please enter in an amount of cash: "))

money500 = money//500
money = money%500

money100 = money//100
money = money%100

money10 = money//10
money = money%10

money5 = money//5
money = money%5

print(money500,"(500)",money100,"(100)", money10,"(10)", money5,"(5)", money,"(1)")
