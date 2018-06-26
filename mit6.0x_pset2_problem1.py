#! Python3
# a script to count lowest payment for a month to pay off a credit card
#
# problem 1 in pset2 of mit6.0x on edx.org

# calculate remain balance
def remain_balance(b, a_i_rate, m_p_rate):
    # define montly interest rate
    m_i_rate = a_i_rate / 12.0
    # initialize remain balance
    remainBalance = b
    # calculate each month's remain balance
    for month in range(0, 12):
        remainBalance = remainBalance * (1 + m_i_rate) * (1 - m_p_rate)
        month += 1
    return remainBalance

# print out the remain balance with 2 decimal digits of accuracy
print('Remaining balance: ' + str(round(remain_balance(balance, annualInterestRate, monthlyPaymentRate), 2)))
