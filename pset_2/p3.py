#use bisection search to find the min monthly payment to the cent!
balance = 999999
annualInterestRate = 0.18
#make an intelligent start guess: 
start = balance/12.0
#make an intelligent end:
end = (balance * ((1 + annualInterestRate)**12))/12.0
monthlyPayment = (start + end)/2.0

while (monthlyPayment >= start and monthlyPayment <= end):
    months = 12
    remainingBalance = balance
    while(months > 0):
        remainingBalance = (remainingBalance - monthlyPayment)
        remainingBalance = remainingBalance + (remainingBalance * annualInterestRate/12.0)
        months -= 1
    if(remainingBalance < -0.05):
        #guess is too big
        end = monthlyPayment
        monthlyPayment = (start + end)/2.0
    elif(remainingBalance > 0.05):
        #guess is too small
        start = monthlyPayment
        monthlyPayment = (start + end)/2.0
    else:
        break
   
print("Lowest Payment: ", round(monthlyPayment, 2))