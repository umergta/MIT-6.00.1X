#calculate minimum fixed monthly payment to pay off balance in 12 months
balance = 3329
annualInterestRate = 0.2
import math
#make an intelligent start guess: multiple of 10 close to the payment
start = int(math.ceil(balance/(12*10)))*10

for monthlyPayment in range(start, balance, 10):
    months = 12
    remainingBalance = balance
    while(months > 0):
        remainingBalance = (remainingBalance - monthlyPayment)
        remainingBalance = remainingBalance + (remainingBalance * annualInterestRate/12.0)
        months -= 1
    print(monthlyPayment)
    if(remainingBalance <= 0):
        print("Lowest Payment: ", monthlyPayment)
        break


    