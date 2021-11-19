import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)

args = parser.parse_args()


def differential():
    P = args.principal  # Loan Principal
    IR = args.interest  # Interest Rate
    n = args.periods  # number of payments

    i = IR / 1200  # interest rate
    m = [x for x in range(1, n + 1)]  # List of months
    total_paid = 0
    overpayment = 0

    for M in m:
        Dm = math.ceil(P / n + (i * (P - (P * (M - 1)) / n)))
        print(f'Month {M}: payment is {Dm}')
        total_paid += Dm
        overpayment = total_paid - P
    print(f'Overpayment = {overpayment}')


def annuity_monthly_a():
    P = args.principal
    n = args.periods
    IR = args.interest  # Input Interest Rate

    i = IR / 1200
    MP = math.ceil(((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)) * P)

    print(f'Your monthly payment = {MP}!')
    total_paid = MP * n
    overpayment = total_paid - P
    print(f'Overpayment = {overpayment}')


def loan_principal():
    IR = args.interest  # Interest Rate
    n = args.periods  # number of payments
    MP = args.payment  # monthly payment

    i = IR / 1200  # interest rate
    P = math.floor(MP / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)))

    print(f'Your loan principal = {P}')
    total_paid = MP * n
    overpayment = total_paid - P
    print(f'Overpayment = {overpayment}')


def by_month():
    month_word = ''
    year_word = ''
    P = 500000
    IR = 7.8  # Input Interest Rate
    MP = 23000  # monthly payment

    i = IR / 1200  # interest rate
    n = math.log((MP / (MP - (i * P))), (1 + i))
    n = math.ceil(n)  # total months
    y = math.floor(n / 12)  # years
    rn = n - (y * 12)  # rest months

    if n == 1:
        print('It will take 1 month to repay the loan')
    elif n < 12:
        month_word = "months"
        print(f'It will take {n} {month_word} to repay the loan')
    elif y == 1 and rn == 0:
        year_word = "year"
        print(f'It will take {y} {year_word} to repay the loan')
    elif y == 1 and rn == 1:
        year_word = "year"
        month_word = "month"
        print(f'It will take {y} {year_word} and {rn} {month_word} to repay the loan')
    elif y == 1 and rn > 1:
        year_word = "year"
        month_word = "months"
        print(f'It will take {y} {year_word} and {rn} {month_word} to repay the loan')
    elif y > 1 and rn == 0:
        year_word = "years"
        print(f'It will take {y} {year_word} to repay the loan')
    elif y == 1 and rn > 1:
        year_word = "year"
        month_word = "months"
        print(f'It will take {y} {year_word} and {rn} {month_word} to repay the loan')
    elif y > 1 and rn > 1:
        year_word = "years"
        month_word = "months"
        print(f'It will take {y} {year_word} and {rn} {month_word} to repay the loan')
    overpayment = (n * MP) - P
    print(f'Overpayment = {overpayment}')

if args.type:
    if args.type == "diff":
        if args.principal and args.interest and args.periods:
            differential()
        else:
            print("Incorrect parameters")
    elif args.type == "annuity":
        if args.principal and args.periods and args.interest:
            annuity_monthly_a()
        elif args.periods and args.interest and args.payment:
            loan_principal()
        elif args.principal and args.interest and args.payment:
            by_month()
        else:
            print("Incorrect parameters")
else:
    print("Incorrect parameters")

