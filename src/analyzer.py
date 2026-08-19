def get_dataset_summary(df):

    summary = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Column Names": list(df.columns),
        "Missing Values": df.isnull().sum().to_dict(),
        "Data Types": df.dtypes.astype(str).to_dict()
    }

    return summary


def get_statistics(df):

    return df.describe(include="all")