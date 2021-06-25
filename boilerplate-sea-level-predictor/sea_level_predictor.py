import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = df.plot.scatter(x='Year', y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    best1 = linregress(x=df['Year'], y=df["CSIRO Adjusted Sea Level"])

    y = pd.Series([*range(1880,2051)])
    fig.plot(y, best1.slope * y + best1.intercept, 'r')

    # Create second line of best fit
    x = df['Year'] >= 2000
    best2 = linregress(x=df['Year'][x], y=df["CSIRO Adjusted Sea Level"][x])

    y = pd.Series([*range(2000,2051)])
    fig.plot(y, best2.slope * y + best2.intercept, 'y')

    # Add labels and title
    fig.set_ylabel("Sea Level (inches)")
    fig.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()