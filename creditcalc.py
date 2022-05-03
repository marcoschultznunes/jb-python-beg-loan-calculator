from Loan import Loan


loan_principal = float(input("Enter the loan principal:\n"))
curr_loan = Loan(loan_principal)

print("What do you want to calculate?")
print('type "m" - for number of monthly payments,')
print('type "p" - for the monthly payment:')
opt = input()

if opt == "m":
    m_pay = float(input("Enter the monthly payment:\n"))
    months = curr_loan.calculate_months(m_pay)
    print(f"\nIt will take {months} month{'s' if months > 1 else '' } to repay the loan")
elif opt == "p":
    months = int(input("Enter the number of months:\n"))
    m_pay, last_pay = curr_loan.calculate_monthly_pay(months)
    print(f"\nYour monthly payment = {m_pay} and the last payment = {last_pay}")
