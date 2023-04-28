import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt


"""
Title: pandas library, covid data

Author: Miguel Angel Verdi Resendiz, verdi.resendiz.miguel@gmail.com
Description:  This algorithm gets data from a covid data page, 
gets some countries and some dates, and returns a plot of the diference of
cases in those countries those days, and generates a sinlge excel file,
with multiple sheets.  
"""




#Here we get the data from internet.
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
data = pd.read_csv(url)


#We define the parameters of the countries we want, of the plot and the range of dates. 
countries = ['Mexico', 'Spain', 'Italy','Brazil']
Dates_range = pd.date_range(start= '8/11/2021', end= '8/11/2022', inclusive="left")
fig, axs = plt.subplots(len(countries))




path = r'New_data.xlsx'



#Function to convert the dates to an especific format. 
def date_format(date):
    return datetime.datetime.strptime(date, "%m/%d/%y")



#We will fill a new data frame 
new_data = []
difference = {}


#We are iterating through the countries matrix
for index,count_name in enumerate(countries): 
    
  #The specific country we are iterating at
  country = data[data['Country/Region'] == count_name]
  
  
  #We melt the country so we can work with the dates-number of cases
  melted_country = country.melt( id_vars=['Country/Region', 'Province/State', 'Lat', 'Long'], var_name="Date" ,value_name='TotalCases')
  formated_dates =  melted_country['Date'].apply(date_format)
  
  
  #Here we filter for the specific dates, creating a mask of specific dates 
  mask = formated_dates.isin(Dates_range) 
  melted_country = melted_country[mask]
  
  
  #And we add the new column with the difference of change in cases
  melted_country['Change'] = melted_country['TotalCases'].diff()
  
  
  
  #Here we print the dates vs the change for each country in the loop
  axs[index].plot(Dates_range,melted_country['Change'],'k')
  text = 'Country: ' + str(count_name)
  axs[index].set_title(text, fontsize=20) 
  axs[index].grid(True)
  axs[index].set_ylabel('Diference of cases')
  
  
  #We fill these vector an dictionary to create the plots and the correlation matrix
  new_data.append(melted_country)
  difference[count_name] = melted_country['Change']


#Here we write, we use a path and an engine
with pd.ExcelWriter(path) as engine:
    
    #We iterate to create the new sheets 
    for i,count_name in enumerate(countries): 
        
        
        #We create a name for each
        text2 = 'Data of ' + str(count_name) 
        new_data[i].to_excel(excel_writer = engine, sheet_name = text2)
       

#Parameters for plotting
fig.set_figheight(10) 
fig.set_figwidth(10) 
fig.subplots_adjust(hspace = 0.6) 
plt.show()




#We create a data frame of countries and their changes of days
#so we can plot the correlation matrix
Data_frame_of_diferences = pd.DataFrame(difference)
corr_matrix = Data_frame_of_diferences.corr()
print(corr_matrix)





 
    




