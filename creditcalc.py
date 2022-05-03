from Loan import Loan
from utils.Utils import Utils


print("What do you want to calculate?")
print('type "n" - for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
opt = input()


if opt == "n":
    loan_principal = float(input("Enter the loan principal:\n"))
    m_pay = float(input("Enter the monthly payment:\n"))
    interest = float(input("Enter the loan interest:\n"))
    curr_loan = Loan(principal=loan_principal, annuity=m_pay, interest=interest)
    months = curr_loan.calculate_months_w_interest()
    print(f"\nIt will take {Utils.months_to_extended(months)} to repay this loan!")

elif opt == "a":
    loan_principal = float(input("Enter the loan principal:\n"))
    periods = int(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    curr_loan = Loan(principal=loan_principal, periods=periods, interest=interest)
    m_pay = curr_loan.calculate_annuity()
    print(f"\nYour monthly payment = {m_pay}!")

elif opt == "p":
    annuity = float(input("Enter the annuity payment:\n"))
    periods = int(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    curr_loan = Loan(annuity=annuity, periods=periods, interest=interest)
    principal = curr_loan.calculate_principal()
    print(f"\nYour loan principal = {principal}!")
