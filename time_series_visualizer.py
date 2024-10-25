import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col=0, parse_dates=True)

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025))
    & (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 5))
    plt.plot(df)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year,df.index.month]).mean()
    df_bar.index.names = ['year', 'month']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    fig, ax = plt.subplots()
    df_bar.unstack().plot(kind='bar', ax=ax)
    ax.legend(months, title='Months')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    order = df_box['month'].unique().tolist()
    order = order[8:] + order[0:8]
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15,5))
    sns.set_palette("bright")
    sns.boxplot(ax=axes[0], data=df_box, x='year', y='value', hue='year', flierprops={"marker": "|"}, legend=False)
    sns.boxplot(ax=axes[1], data=df_box, x='month', y='value', hue='month', flierprops={"marker": "|"}, legend=False, order=order)
    axes[0].set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
    axes[1].set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
