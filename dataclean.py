# Please note that this only work with Pandas Dataframe!
# I personally recommend to import it by "import dataclean as dc"

# Uppercases the first letter of every column name and changes underscore into spaces.
# So it would look more formal especially in making graphs.
def upcase(dataframe):
    dataframe.columns = dataframe.columns.str.title()
    dataframe.columns = dataframe.columns.str.replace('_', ' ')
    return dataframe


# Change data type. Example - "int64" to "float64".
def change_type(dataframe, from_type=None, to_type=None):
    data = dataframe.select_dtypes(include=[from_type])
    columns = list(data)
    dataframe[columns] = data.astype(to_type)
    return dataframe


# Replace Nan values with average values of its column (for numeric values only!).
# If you want to be specific, include a list of name(s) of the column in subset argument.
def replace_nan(dataframe, subset=None):
    if subset is not None:
        data = dataframe[subset]
        dataframe[subset] = data.fillna(data.mean(numeric_only=True))

    else:
        dataframe = dataframe.fillna(dataframe.mean(numeric_only=True))

    return dataframe


# Delete rows that has Nan values.
# If you want to be specific, include a list of name(s) of the column in subset argument.
def cleanrow(dataframe, subset=None):
    dataframe.dropna(inplace=True, subset=subset)
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


# Divide object type data and numerical data by column.
def type_sort(dataframe):
    categorical = dataframe.select_dtypes(include=["object"])
    numerical = dataframe.select_dtypes(exclude=["object"])
    dataframe = categorical.join(numerical)
    return dataframe


# Sort all row in accending or decending order according to a column.
# Note that object type is sorted in alphabetical order.
# Example - based="Price"
def rowsort(dataframe, based=None, ascending=True):
    dataframe.sort_values(by=based, axis=0, ascending=ascending, inplace=True)
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


# Change data type, replace Nan values and remove row with Nan values quickly by simply put in -> df = basicclean(df)
# If you want clean specific columns only, include a list of name(s) of the column in subset argument.
def basicclean(dataframe, from_type=None, to_type=None, replace=True, clean_row=True, subset=None):
    if from_type is None and to_type is None:
        dataframe = change_type(dataframe, from_type="int32", to_type="float32")
        dataframe = change_type(dataframe, from_type="int64", to_type="float64")
    else:
        dataframe = change_type(dataframe, from_type=from_type, to_type=to_type)

    if replace is True:
        dataframe = replace_nan(dataframe, subset=subset)

    if clean_row is True:
        dataframe = cleanrow(dataframe, subset=subset)

    return dataframe

# Ask question on twitter @nzmi___
