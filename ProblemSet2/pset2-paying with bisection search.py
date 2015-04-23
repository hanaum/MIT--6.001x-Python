balance = 320000
original_balance = balance
annualInterestRate = 0.2

monthlyInterestRate = (annualInterestRate) / 12.0
low = balance / 12.0
high = (balance * (1 + monthlyInterestRate)**12.0) / 12.0
monthly_pay = (low + high) / 2.0

while abs(balance) >  0.01:
    monthly_pay = (low+high) / 2.0
    balance = original_balance
    for months in range(1, 13):
        balance  -= monthly_pay
        balance = round( (balance * (1 + monthlyInterestRate) ), 2)

    if balance > 0: # too low
        low = monthly_pay

    elif balance < 0: # too high
        high = monthly_pay


print "Lowest payment: ", round(monthly_pay, 2)
