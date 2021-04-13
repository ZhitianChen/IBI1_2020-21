import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY

covid_data = pd.read_csv("full_data.csv")

print(covid_data.iloc[0:11:2, :])

n = 0
mylist1 = []
for n in range(0, len(covid_data)):
    a = covid_data.loc[n, "location"]
    if a == "Afghanistan":
        mylist1.append(True)
    else:
        mylist1.append(False)
print()
print(covid_data.loc[mylist1, "total_cases"])

m = 0
mylist2 = []
for m in range(0, len(covid_data)):
    b = covid_data.loc[m, "location"]
    if b == "World":
        mylist2.append(True)
    else:
        mylist2.append(False)
World_new_cases = np.array(covid_data.loc[mylist2, "new_cases"])
print()
print('The mean is ' + str(np.mean(World_new_cases)))
print('The median is ' + str(np.median(World_new_cases)))


plt.boxplot(World_new_cases,  # use the data from "World" to create the data
            vert=True,  # set the box plot ventricle
            whis=1.5,  # Western plot
            patch_artist=True,  # color the box
            meanline=True,  # use a line to represent the mean value
            showbox=True,  # show the box line
            showcaps=True,  # show the lines which represent the maximum and the minimum
            showfliers=True,  # show the outliers
            notch=False,  # do not show the plot with notches
            showmeans=True  # show means using a line
            )
plt.title('New cases worldwide', fontsize=20)
print()
plt.show()


print()
z = 0
mylist3 = []
for z in range(0, len(covid_data)):
    z = covid_data.loc[z, "location"]
    if z == "World":
        mylist3.append(True)
    else:
        mylist3.append(False)
World_new_deaths = np.array(covid_data.loc[mylist3, "new_deaths"])
World_dates = np.array(covid_data.loc[mylist2, "date"])
l1, = plt.plot(World_dates, World_new_cases, 'b.')
l2, = plt.plot(World_dates, World_new_deaths, 'r.')
plt.gcf().autofmt_xdate()
plt.title('New cases and new deaths worldwide')
plt.legend(handles=[l1, l2, ], labels=['World new cases', 'World new deaths'], loc='upper left')
plt.show()


y = 0
mylist4 = []
for y in range(0, len(covid_data)):
    y = covid_data.loc[y, "location"]
    if y == "Spain":
        mylist4.append(True)
    else:
        mylist4.append(False)
Spain_new_cases = np.array(covid_data.loc[mylist4, "new_cases"])
Spain_total_cases = np.array(covid_data.loc[mylist4, "total_cases"])
Spain_dates = np.array(covid_data.loc[mylist4, "date"])

l3, = plt.plot(Spain_dates, Spain_new_cases, 'y.')
l4, = plt.plot(Spain_dates, Spain_total_cases, 'g.')
plt.gcf().autofmt_xdate()
plt.title('New cases and total cases in Spain')
plt.legend(handles=[l3, l4, ], labels=['Spain new cases', 'Spain total cases'], loc='upper left')
plt.show()
