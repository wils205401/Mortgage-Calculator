# Implement a mortgage calculator
# Requirements:
# 1. Should be a program that runs on the terminal and interacts with the user through input()

# import packages
import pandas as pd
import numpy as np

x = 2

def mortage_payments(loam_amt, maturity, payments_per_year, interest, excel=0):

    # if excel == 1:
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
    InterestRate = float(input('Enter the annual interest rate on your loan: '))

    options = input('Please input the operation you wish to perform. 1 for ')


if __name__ == '__main__':
    main()