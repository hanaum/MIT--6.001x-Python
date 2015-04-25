'''Paying the Minimum: calculates the credit card balance after one year if a person only 
        pays the minimum monthly payment required by the credit card company each month.

MIT-6.001x Python
Hana Um
'''

months = 0
loop = True

total_paid = 0
monthlyInterestRate = annualInterestRate/12.0
minMonthlyPay = monthlyPaymentRate * balance
monthlyUnpaidBalance = balance - minMonthlyPay
updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

while loop:
    minMonthlyPay = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minMonthlyPay
    updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    if months == 0:
        months += 1
        balance = updatedBalance
        total_paid += minMonthlyPay
        print "month: " + str(months)
        print "minimum monthly payment: " + str(round(minMonthlyPay, 2))
        print "Remaining balance: " + str(round(balance, 2))

    elif months > 0 and months < 12:
        months += 1
        balance = updatedBalance
        total_paid += minMonthlyPay
        print "month: " + str(months)
        print "minimum monthly payment: " + str(round(minMonthlyPay, 2))
        print "Remaining balance: " + str(round(balance, 2))

    else:
        loop = False

print "Total paid: " + str(round(total_paid, 2))
print "Remaining balance: " + str(round(balance, 2))
