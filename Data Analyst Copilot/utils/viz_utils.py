import matplotlib.pyplot as plt
import seaborn as sns

def plot_outliers(df, column):
    fig, ax = plt.subplots()
    sns.boxplot(y=df[column], ax=ax)
    ax.set_title(f'Outlier Detection for {column}')
    return fig
