""" Extracts data from csv files to be displayed on the website along with
coefficients """

#import pygame
import pandas

__author__ = "Sara Ballantyne"
__version__ = '0.0.1'

def data_extraction():
    """Pulls data from csv columns as needed for website to pass into javascript --> html
    >>> data_extraction()

    """
    # First thing: extract headings for each column to pass into pandas
    # (As of now, hard coded)
    colnames = ['Country', 'CountryCode', 'DataName', 'DataName2']
    number_of_years = (1963-1960)
    x = 0

    while x in range(number_of_years):
        year = 1960 + x
        add_me = 'yr' + str(year)
        colnames = colnames + [add_me]
    #colnames = colnames + [ 'yr1960' , 'yr1961', 'yr1962', 'yr1963']

    # Read data from file
    data = pandas.read_csv('test.csv', names=colnames)

    # Convert data into lists
    names = data.Country.tolist()
    year1 = data.yr1960.tolist()
    year2 = data.yr1961.tolist()
    year3 = data.yr1962.tolist()
    year4 = data.yr1963.tolist()
    print(year4)


def coefficients_calc():
    """ Calculates a coefficient for each country based on weights given by JS
    sliders and dropdown menus (This might be best calculated in the javascript itself)

    """
    pass


data_extraction()



# Run if called from the command line
if __name__ == "__main__":
    # Setup code (if any) to call before test
    setup = "from __main__ import data_extraction, coefficients_calc, test = setup function goes here"
    ntrials = 1000

    # Run tests for 1000 executions each
    rc1_time = timeit.timeit("data_extraction(test)", setup=setup, number=ntrials)
    print("RC1 time:", rc1_time)

    rc2_time = timeit.timeit("coefficients_calc(test)", setup=setup, number=ntrials)
    print("RC1 time:", rc1_time)
