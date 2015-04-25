'''Paying Debt Off in a Year: calculates the minimum fixed monthly payment needed in order to
		pay off a credit card balance within 12 months. 

MIT-6.001x Python
Hana Um
'''

months = 0
fixedPay = 0
original_balance = balance
monthlyInterestRate = annualInterestRate/ 12.0
monthlyUnpaidBalance = balance - fixedPay
updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

while balance > 0:
    monthlyUnpaidBalance = balance - fixedPay
    updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    months += 1
    balance = round(updatedBalance, 2)

    if months > 12:
        fixedPay += 10
        months = 0
        balance = original_balance

print "Lowest Payment: " + str(fixedPay)
