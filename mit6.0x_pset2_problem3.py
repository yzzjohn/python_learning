#! Python3
# a script to count lowest payment for a month to pay off a credit card
# by biosection search
#
# problem 2 in pset3 of mit6.0x on edx.org


# calculate remain balance
def remain_balance(b, a_rate, m_rate , m_payment):
    # initialize remain balance
    remainBalance = b

    for month in range(0, 12):
        remainBalance = (1 + m_rate) * (remainBalance - m_payment)
        month += 1

    return remainBalance

# use biosection search to find out the lowest payment
def lowest_payment(b, a_rate, m_rate, l_bound, u_bound):
    # choose the middle as potential
    lowestPayment = round((l_bound + u_bound) / 2, 2)

    # set 0.1 as epsilon to avoid infinit loop
    if abs(remain_balance(b, a_rate, m_rate, lowestPayment)) < 0.1:
        return lowestPayment
    else:
        if remain_balance(b, a_rate, m_rate, lowestPayment) > 0:
            l_bound = lowestPayment
            return lowest_payment(b, a_rate, m_rate, l_bound, u_bound)
        else:
            u_bound = lowestPayment
            return lowest_payment(b, a_rate, m_rate, l_bound, u_bound)

# initialize bounds
lower_bound = round(balance / 12, 2)
upper_bound = round(balance * (1 + annualInterestRate / 12.0) ** 12 / 12.0, 0)
# montly interest rate
monthlyInterestRate = annualInterestRate / 12.0

print('Lowest Payment: ' + str(lowest_payment(balance, annualInterestRate, monthlyInterestRate, lower_bound, upper_bound)))
