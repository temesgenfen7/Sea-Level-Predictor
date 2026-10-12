import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=20)

    # Create first line of best fit using all data
    x_all = df['Year']
    y_all = df['CSIRO Adjusted Sea Level']
    slope_all, intercept_all, r_all, p_all, stderr_all = linregress(x_all, y_all)

    # Extend line to year 2050
    x_pred_all = np.arange(x_all.min(), 2051)
    y_pred_all = intercept_all + slope_all * x_pred_all
    plt.plot(x_pred_all, y_pred_all, color='red', label='Best fit (all data)')

    # Create second line of best fit using data from year 2000 onward
    df_2000 = df[df['Year'] >= 2000]
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']
    slope_2000, intercept_2000, r_2000, p_2000, stderr_2000 = linregress(x_2000, y_2000)

    # Extend second line to year 2050
    x_pred_2000 = np.arange(2000, 2051)
    y_pred_2000 = intercept_2000 + slope_2000 * x_pred_2000
    plt.plot(x_pred_2000, y_pred_2000, color='green', label='Best fit (2000 onward)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
