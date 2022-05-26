import pandas as pd

def read_to_df(path):
    """
    Open the file and read it to a dataframe.
    """
    df = pd.read_csv(path)
    return df

def about_df(dataframe):
    """
    Helpful for getting info about the dataframe.
    """
    dataframe.info()

def about_series(srs):
    """
    Helpful for getting info about the series.
    """
    srs.info()

def total_spent(dataframe):
    #Return a string of sum all values for the item total column.
    return str(dataframe["Item Total"].sum(0))

def convert_to_numeric(df, column_name):

    # Remove all $ from the column
    df[column_name] = df[column_name].str.replace("$", "")

    # Convert the passed series to numeric
    df[column_name] = pd.to_numeric(df[column_name])

    # about df_column name
    #about_series(df[column_name])

if __name__ == '__main__':

    """
    Finds the amazon doc, looks for the item total, and prints the summed value of the item total.
    To function, the user must add the name of the CSV file, which can be gotten from Amazon.   
    """
    filepath = 'data/01-Jan-2021_to_27-Feb-2022.csv'

    #1. Get the CVS file
    working_df = read_to_df(filepath)

    #Ensure item total column is numeric
    convert_to_numeric(working_df,"Item Total")

    # sum all values in the item total column
    print("Total Spent: " + total_spent(working_df))