# Implement a mortgage calculator
# Requirements:
# 1. Should be a program that runs on the terminal and interacts with the user through input()

# import packages
import pandas as pd
import numpy as np
import datetime

def mortgage_payments(loan_amt, maturity, payments_per_year, interest, option=1, start_date=None):
    '''
    Function that implements a mortgage calculator
    :param loan_amt: Size of mortgage loan
    :param maturity: Number of years until the final mortgage payment date, typically 30
    :param payments_per_year: Number of payments per year
    :param interest: Stated annual interest rate
    :param option: 1 to get payment per period, 2 to get whole payment schedule
    :param start_date: the day you got the mortgage (first payment occurs next month)
    :return: payment per period or whole payment schedule depending on 'option'
    '''
    interest_per_period = interest / payments_per_year
    number_of_payments = payments_per_year * maturity

    # Formula for Payment per Period (e.g. monthly payments)
    payments_per_period = (interest_per_period*loan_amt) / (1-(1+interest_per_period)**(-1*number_of_payments))

    if option == 1:
        return payments_per_period

    else:
        # start date is a string, convert to datetime
        start_date = datetime.datetime.strptime(start_date, '%Y/%m/%d').date()

        if payments_per_year == 12: # monthly payments
            date_range = pd.date_range(start=start_date, periods=maturity * payments_per_year, freq='MS')

        elif payments_per_year == 24: # semi-monthly payments
            date_range = pd.date_range(start=start_date, periods=maturity*payments_per_year, freq='SMS')

        else:
            raise ValueError('Valid payments per year are 12 (monthly) or 24 (semi-monthly/bi-weekly)')

        date_range.name = 'Payment Date'
        df = pd.DataFrame(index=date_range, columns = ['Payment', 'Principal Paid', 'Interest Paid', 'Ending Balance'],
                          dtype = 'float')
        df.reset_index(inplace=True)
        df.index += 1
        df.index.name = 'Period'

        df['Payment'] = round(payments_per_period, 2)
        df.loc[1, 'Interest Paid'] = round(interest_per_period * loan_amt, 2)
        df.loc[1, 'Principal Paid'] = round(payments_per_period - df.loc[1, 'Interest Paid'], 2)
        df.loc[1, 'Ending Balance'] = round(loan_amt - df.loc[1, 'Principal Paid'], 2)

        for k in range(2, len(df) + 1):
            df.loc[k, 'Interest Paid'] = round(interest_per_period * df.loc[k-1, 'Ending Balance'], 2)
            df.loc[k, 'Principal Paid'] = round(df.loc[k, 'Payment'] - df.loc[k, 'Interest Paid'], 2)
            df.loc[k, 'Ending Balance'] = round(df.loc[k-1, 'Ending Balance'] - df.loc[k, 'Principal Paid'], 2)

        return df



def main():
    print('-----Mortgage Calculator-----')
    ### User inputs
    # loan size
    LoanAmount = float(input('Enter the mortgage/loan amount: '))
    # maturity of loan
    Maturity = float(input('Enter the maturity of the loan (years): '))
    # payment frequency, most commonly 12 or 24 (monthly or semi-monthly)
    PaymentsPerYear = float(input('Enter the number of payments per year: '))
    # interest rate
    InterestRate = float(input('Enter the annual interest rate on your loan (decimals): '))
    print('-----------------------------')
    Options = int(input('''Please input the operation you wish to perform.
(1) Calculate your payment per period
(2) Get a detailed summary of your payment schedule
(3) Get a detailed summary of your payment schedule and save it as an Excel file
Enter (1/2/3): '''))

    if Options == 1:
        PaymentPerPeriod = mortgage_payments(LoanAmount, Maturity, PaymentsPerYear, InterestRate, Options)
        print(f"${round(PaymentPerPeriod, 2)}")
    elif Options == 2:
        start_date = input('Enter the start date of mortgage (YYYY/MM/DD): ')
        print('NB: The payment schedule assumes that the payment takes place on the 1st of each month for monthly payments, and on the 1st and 15th for semi-monthly payments.')
        PaymentSchedule = mortgage_payments(LoanAmount, Maturity, PaymentsPerYear, InterestRate, Options, start_date)
        print(PaymentSchedule)
        SaveAsCSV = input('Would you like to save the payment schedule as an Excel file? (Y/N)')
        if SaveAsCSV.upper() == 'Y':
            PaymentSchedule.to_csv('mortgage_payments.csv')
        elif SaveAsCSV.upper() == 'N':
            return None
        else:
            raise ValueError('Please enter a valid option (Y/N).')

    else:
        raise ValueError('Please enter a valid number (1/2/3).')


if __name__ == '__main__':
    main()


# unit tests to validate correct calculations
# answers are obtained from other online mortgage calculators