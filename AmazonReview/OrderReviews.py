def convert_to_numeric(df, column_name):

    # Remove all $ from the column
    df[column_name] = df[column_name].str.replace("$", "")

    # Convert the passed series to numeric
    df[column_name] = pd.to_numeric(df[column_name])

    # about df_column name
    #about_series(df[column_name])