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
    colnames = ['Country', 'CountryCode', 'DataName', 'DataName2', 'yr1960', 'yr1961', 'yr1962', 'yr1963']

    # Read data from file
    data = pandas.read_csv('test.csv', names=colnames)

    # Convert data into lists
    names = data.Country.tolist()
    year1 = data.yr1960.tolist()
    year2 = data.yr1961.tolist()
    year3 = data.yr1962.tolist()
    year4 = data.yr1963.tolist()



def coefficients_calc():
    """ Calculates a coefficient for each country based on weights given by JS
    sliders and dropdown menus (This might be best calculated in the javascript itself)

    """
    pass

data_extraction()
