# Implement a mortgage calculator
# Requirements:
# 1. Should be a program that runs on the terminal and interacts with the user through input()

# import packages
import pandas as pd
import numpy as np
import datetime

def mortgage_payments(loan_amt, maturity, payments_per_year, interest, option=1, start_date=None):
    interest_per_period = interest / payments_per_year
    number_of_payments = payments_per_year * maturity

    # Formula for Payment per Period (e.g. monthly payments)
    payments_per_period = (interest_per_period*loan_amt) / (1-(1+interest_per_period)**(-1*number_of_payments))

    if option == 1:
        return payments_per_period

    # start date is a string, convert to datetime
    start_date = datetime.datetime.strptime(start_date, '%Y/%m/%d').date()



    # if option == 3:
        # df.to_csv('mortgage_payments_schedule.csv')
    pass


def main():
    print('-----Mortgage Calculator-----')
    ### User inputs
    # loan size
    LoanAmount = float(input('Enter the mortgage/loan amount: '))
    # maturity of loan
    Maturity = float(input('Enter the maturity of the loan (years): '))
    # payment frequency
    PaymentsPerYear = float(input('Enter the number of payments per year: '))
    # interest rate
    InterestRate = float(input('Enter the annual interest rate on your loan (decimals): '))
    print('-----------------------------')
    options = int(input('''Please input the operation you wish to perform.
(1) Calculate your payment per period
(2) Get a detailed summary of your payment schedule
(3) Get a detailed summary of your payment schedule and save it as an Excel file
Enter (1/2/3): '''))

    if options == 1:
        payment_per_period = mortgage_payments(LoanAmount, Maturity, PaymentsPerYear, InterestRate, options)
        print(f"${round(payment_per_period, 2)}")
    elif options == 2:
        start_date = input('Enter the start date of mortgage (YYYY/MM/DD): ')
        pass

    elif options == 3:
        start_date = input('Enter the start date of mortgage (YYYY/MM/DD): ')
        pass

    else:
        raise ValueError('Please enter a valid number. (1/2/3)')


if __name__ == '__main__':
    main()


# unit tests to validate correct calculations
# answers are obtained from other online mortgage calculators