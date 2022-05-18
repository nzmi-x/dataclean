def upcase(dataframe):
    dataframe = dataframe.str.title()
    return dataframe


def repltype(dataframe, from_type=None, to_type=None):
    data = dataframe.select_dtypes(include=[from_type])
    columns = list(data)
    dataframe[columns] = data.astype(to_type)
    return dataframe


def replnan(dataframe, subset=None):
    if subset is not None:
        data = dataframe[subset]
        dataframe[subset] = data.fillna(data.mean(numeric_only=True))

    else:
        dataframe = dataframe.fillna(dataframe.mean(numeric_only=True))

    return dataframe


def cleanrow(dataframe, subset=None):
    dataframe.dropna(inplace=True, subset=subset)
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


def colsort(dataframe):
    categorical = dataframe.select_dtypes(include=["object"])
    numerical = dataframe.select_dtypes(exclude=["object"])
    dataframe = categorical.join(numerical)
    return dataframe


def rowsort(dataframe, based=None, ascending=True):
    dataframe.sort_values(by=based, axis=0, ascending=ascending, inplace=True)
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


def basicclean(dataframe, from_type=None, to_type=None, replace=True, clean_row=True, subset=None):
    if from_type is None and to_type is None:
        dataframe = repltype(dataframe, from_type="int32", to_type="float32")
        dataframe = repltype(dataframe, from_type="int64", to_type="float64")
    else:
        dataframe = repltype(dataframe, from_type=from_type, to_type=to_type)

    if replace is not False:
        dataframe = replnan(dataframe, subset=subset)

    if clean_row is not False:
        dataframe = cleanrow(dataframe, subset=subset)

    return dataframe
