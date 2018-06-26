#! Python3
# a script to count lowest payment for a month to pay off a credit card
#
# problem 2 in pset2 of mit6.0x on edx.org


# calculate remain balance
def remain_balance(b, a_rate, monthly_p):
    # define montly interest rate
    m_rate = a_rate / 12.0
    # initialize remain balance
    remainBalance = b
    # calculate each month's remain balance
    for month in range(0, 12):
        remainBalance = (1 + m_rate) * (remainBalance - monthly_p)
        month += 1
    return remainBalance

# calculate lowest payment
def lowest_payment(b, a_rate):
    # initialize lowestPayment
    lowestPayment = 10
    # add $10 each time and break out loop when the remain balance is under 0
    while True:
        if remain_balance(b, a_rate, lowestPayment) <= 0:
            break
        else:
            lowestPayment += 10
    return lowestPayment

print('Lowest Payment: ' + str(lowest_payment(balance, annualInterestRate)))
