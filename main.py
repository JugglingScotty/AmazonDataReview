import pandas as pd
import numpy as np
import OrderReviews

def read_to_df(path):
    """
    Open the file and read it to a dataframe.
    """
    df = pd.read_csv(path)
    return df

def about_df(df):
    """
    Helpful for getting info about the dataframe.
    """
    df.info()

def about_series(srs):
    """
    Helpful for getting info about the series.
    """
    srs.info()

def total_spent(dataframe):
    #Return a string of sum all values for the item total column.
    return dataframe["Item Total"].sum(0)



def average_order_value(df):
    return np.average(df.loc[:, ['Item Total']])


if __name__ == '__main__':

    """
    Finds the amazon doc, looks for the item total, and prints the summed value of the item total.
    To function, the user must add the name of the CSV file, which can be gotten from Amazon.   
    """
    filepath = 'data/01-Jan-2021_to_27-Feb-2022.csv'

    #1. Get the CVS file
    working_df = read_to_df(filepath)

    #Ensure item total column is numeric
    OrderReviews.convert_to_numeric(working_df,"Item Total")

    # Statistics: Total Cost Spent, Average Order Value
    added_together = total_spent(working_df)
    print(f"Total Spent: ${added_together:.2f}.")

    average_order = average_order_value(working_df)
    print(f"Average Order Value: ${average_order:.2f}.")


    """
    Improvement Ideas:
    Other summary counts = Counts by currency, Taxes Paid, Carrier Used, 
    Display the money spent by day.
    Tracking Number Lookup
    """