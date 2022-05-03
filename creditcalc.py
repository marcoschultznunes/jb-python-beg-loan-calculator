from Loan import Loan
from utils.Utils import Utils
import argparse

arg_parser = argparse.ArgumentParser(description="Program calculates loan variables")
arg_parser.add_argument("--type", choices=["annuity", "diff"])
arg_parser.add_argument("--principal", type=float)
arg_parser.add_argument("--periods", type=int)
arg_parser.add_argument("--interest", type=float)
arg_parser.add_argument("--payment", type=float)
args = arg_parser.parse_args()


def no_params():
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


def with_params():
    global args

    if args.type == "annuity":
        if not args.principal:
            curr_loan = Loan(annuity=args.payment, periods=args.periods, interest=args.interest)
            principal = curr_loan.calculate_principal()
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {curr_loan.calculate_overpayment()}")
        elif not args.payment:
            curr_loan = Loan(principal=args.principal, periods=args.periods, interest=args.interest)
            annuity = curr_loan.calculate_annuity()
            print(f"Your loan annuity = {annuity}!")
            print(f"Overpayment = {curr_loan.calculate_overpayment()}")
        elif not args.periods:
            curr_loan = Loan(principal=args.principal, annuity=args.payment, interest=args.interest)
            periods = curr_loan.calculate_months_w_interest()
            print(f"Your loan periods = {Utils.months_to_extended(periods)}!")
            print(f"Overpayment = {curr_loan.calculate_overpayment()}")
    elif args.type == "diff":
        curr_loan = Loan(principal=args.principal, periods=args.periods, interest=args.interest)
        months = curr_loan.calculate_diff_monthly()
        for i, pay in enumerate(months):
            print(f"Month {i + 1}: payment is {pay}")
        print(f"Overpayment = {curr_loan.calculate_diff_overpayment()}")


def main():
    global args

    if any(vars(args).values()):
        if not args.interest:
            print("Incorrect parameters")
        else:
            with_params()
    else:
        no_params()


main()
