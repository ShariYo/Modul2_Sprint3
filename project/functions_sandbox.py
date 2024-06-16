def cleaner(df, info=True):
    df = df.copy()
    df.columns = df.columns.str.strip()
    df.rename(columns=lambda x: x.lower(), inplace=True)
    df_duplicates = df.duplicated().any()
    df_nan = df.isna().any().any()
    df_empty = (df == "").any().any()

    if info:
        print("All columns empty spaces have been stripped.")
        print("All columns names have been converted to lowercase.\n")
        print(f"Is there any duplicates?: {df_duplicates}")
        print(f"Is there any NaN numbers?: {df_nan}")
        print(f"Is there any empty cells?: {df_empty}")

    return df


def f_histogram(xaxis, bins=20, kde=False, figsize=(6, 4), xlabel=None, title=None):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=figsize)
    sns.histplot(x=xaxis, bins=bins, kde=kde)
    plt.xlabel(xlabel)
    plt.title(title, size=14, fontweight="bold", ha="center")
    plt.legend()

    return plt.show()
