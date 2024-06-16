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


def f_histogram(
    xaxis, bins=20, kde=False, figsize=(6, 4), label=None, xlabel=None, title=None
):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=figsize)
    sns.histplot(x=xaxis, bins=bins, label=label, kde=kde)
    plt.xlabel(xlabel)
    plt.title(title, size=14, fontweight="bold", ha="center")
    plt.legend()

    return plt.show()


def f_boxplot(xaxis, figsize=(6, 4), xlabel=None, title=None):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=figsize)
    sns.set_palette("crest")
    ax = xaxis.plot(kind="bar", width=0.8)
    for container in ax.containers:
        ax.bar_label(container)
    ax.axes.get_yaxis().set_visible(False)
    ax.axes.get_xaxis().set_visible(True)
    ax.set_frame_on(False)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.xlabel(xlabel)
    plt.title(title, size=14, fontweight="bold", ha="center")
    plt.legend()

    return plt.show()
