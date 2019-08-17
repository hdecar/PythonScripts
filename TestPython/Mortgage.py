# Simple Mortgage Calculator

import locale
locale.setlocale(locale.LC_ALL, '')

from mortgage import Loan

purchaseAmount = 550000
downPayment = 200000
interestRate = .043
termInYears = 15
pmiPercent = .2

amountFinanced = purchaseAmount-downPayment

loan = Loan(principal=amountFinanced, interest=interestRate, term=termInYears)

totalCost = loan.n_periods * termInYears * loan.monthly_payment
paymentAmount = loan.monthly_payment
loanToValue = round(amountFinanced/purchaseAmount, 2)

print()
print("Purchase Amount:", locale.currency(purchaseAmount))
print("Down Payment:", locale.currency(downPayment))
print("Interest Rate:", interestRate)
print("Term in Years:", termInYears)
print("-----------------------------------------------")
print()
print("Monthly P&I Amount:",locale.currency(loan.monthly_payment))
print()
print("Amount Financed:", locale.currency(amountFinanced))
print("Total Cost of Loan:", locale.currency(totalCost))
print("Total Interest:", locale.currency(totalCost - amountFinanced))
print("Loan to Value%:", loanToValue)
print("Number of Payments:", termInYears * loan.n_periods)
if loanToValue > .8:
    print ("Down payment is only", round(1-loanToValue, 2), "of purchase amount, so you may also need to pay PMI.")
else:
    print ("PMI will not be required for this loan.")
