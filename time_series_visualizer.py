import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset
lower_quantile = df['value'].quantile(0.025)
upper_quantile = df['value'].quantile(0.975)

df = df.loc[(df['value'] >= lower_quantile) & (df['value'] <= upper_quantile)]


def draw_line_plot():
    # Draw line plot

    # Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". 
    # The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. 
    # The label on the x axis should be Date and the label on the y axis should be Page Views.
    
    fig = plt.figure(figsize=(14, 4.5))
    plt.plot(df, color="#C80000", linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png".

    # Copy and modify data for monthly bar plot
    df_bar = df.copy() # Make a copy of the original DataFrame
    df_bar['year'] = df_bar.index.year  # Extract year from the index and create a new 'year' column
    df_bar['month'] = df_bar.index.month    # Extract month (as a number) from the index and create a new 'month' column

    # Group by year and month, calculate the mean value, round it, convert it to integer, and handle missing months with 0.
    df_bar = df_bar.groupby(['year', 'month'], sort=True)['value'].mean().round().astype(int).unstack().fillna(0).stack().reset_index(name='average_page_views')
    
    # Convert the 'month' numbers into month names using the ordered list
    months_ordered = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['month'] = df_bar['month'].apply(lambda x: months_ordered[x - 1])


    fig, ax = plt.subplots(figsize=(14, 12))

    ax.set_xlabel("Years", fontsize=18) # Label and fontsize for x-axis (years)
    ax.set_ylabel("Average Page Views", fontsize=18) # Label and fontsize for y-axis (average_page_views)

    # Create the bar plot using seaborn
    sns.barplot(data=df_bar, x="year", y="average_page_views", hue="month", palette="tab10", dodge=True, width=0.5)
    ax.legend(title='Months', title_fontsize=18, fontsize=18)
    plt.xticks(rotation=90, horizontalalignment='center')
    ax.tick_params(axis='x', labelsize=18)  # Increase font size for x-axis (years)
    ax.tick_params(axis='y', labelsize=18)  # Increase font size for y-axis (average page views)


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
