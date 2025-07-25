def get_summary_stats(df):
    return {
        "shape": df.shape,
        "dtypes": df.dtypes,
        "missing": df.isnull().sum(),
        "describe": df.describe()
    }
