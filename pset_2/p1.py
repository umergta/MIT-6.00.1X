#write program to calculate balance after 1 year 
# if person only pays minimum each month
#prints the remaining balance after 12 months

#variables:
# balance, annualInterestRate, monthlyPaymentRate

balance = 484
anualInterestRate = 0.2
monthlyPaymentRate = 0.04

remainingMonths = 12
while(remainingMonths > 0):
    #payment made
    balance = balance - balance * monthlyPaymentRate
    #interest charged
    balance =  balance + balance * anualInterestRate/12.0
    remainingMonths -= 1

print("remaining balance:", round(balance, 2))