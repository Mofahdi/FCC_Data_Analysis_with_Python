import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    bst_ft=linregress(df.Year, df['CSIRO Adjusted Sea Level'])
    yrs_ft=np.linspace(df['Year'].min(), 2050, 2050-df['Year'].min()+1)
    #yrs_ft=np.arange(df['Year'].min(),2050,1)
    sea_lvl_ft=bst_ft.slope*yrs_ft+bst_ft.intercept
  
    plt.plot(yrs_ft, sea_lvl_ft)
  
    # Create second line of best fit
    df_2000=df[df.Year>=2000]
    bst_ft_2000 = linregress(df_2000.Year, df_2000['CSIRO Adjusted Sea Level'])
    yrs_2000=np.linspace(df_2000['Year'].min(), 2050, 2050-df_2000['Year'].min()+1)
    sea_lvl_ft_2000 = bst_ft_2000.slope*yrs_2000+bst_ft_2000.intercept
    plt.plot(yrs_2000, sea_lvl_ft_2000)
    #print(yrs_2000.shape, sea_lvl_ft_2000.shape)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()