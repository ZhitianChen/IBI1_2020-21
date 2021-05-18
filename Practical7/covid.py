import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

os.chdir('/Users/A.BC.Perroquet/PycharmProjects/Practical7/venv/')  # change the directory to where the full_data.csv is
covid_data = pd.read_csv("full_data.csv")  # import the file

print(covid_data.iloc[0:11:2, :])  # to show all columns and every second row between and including 0 and 10

n = 0
mylist1 = []  # create a blank list
for n in range(0, len(covid_data)):  # use for loop to look through every location
    a = covid_data.loc[n, "location"]
    if a == "Afghanistan":  # use if to judge if the location is Afghanistan
        mylist1.append(True)  # use Boolean
    else:
        mylist1.append(False)  # use Boolean
print()  # print a blank row to separate the second output with the first output
print(covid_data.loc[mylist1, "total_cases"])  # to print the result

m = 0
mylist2 = []  # create another blank list
for m in range(0, len(covid_data)):  # similar to the last task, use for loop to look through
    b = covid_data.loc[m, "location"]
    if b == "World":
        mylist2.append(True)
    else:
        mylist2.append(False)
World_new_cases = np.array(covid_data.loc[mylist2, "new_cases"])  # select new cases in the World
print()  # print a blank row to separate the third output with the second output

print('World')  # to indicate this is the result of the World
print('The mean is ' + str(np.mean(World_new_cases)))  # to print the mean
print('The median is ' + str(np.median(World_new_cases)))  # to print the median


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
plt.show()  # show the figure


print()
z = 0
mylist3 = []
for z in range(0, len(covid_data)):  # similar to the previous tasks, use for loop
    z = covid_data.loc[z, "location"]
    if z == "World":
        mylist3.append(True)
    else:
        mylist3.append(False)
World_new_deaths = np.array(covid_data.loc[mylist3, "new_deaths"])
World_dates = covid_data.loc[mylist2, "date"]
l1, = plt.plot(World_dates, World_new_cases, 'b.')
l2, = plt.plot(World_dates, World_new_deaths, 'r.')  # show the difference between two kinds of dots
plt.gcf().autofmt_xdate()
plt.title('New cases and new deaths worldwide')  # give the figure a title
plt.legend(handles=[l1, l2, ], labels=['World new cases', 'World new deaths'], loc='upper left')  # give labels to two kinds of dots in the figure
plt.xticks(World_dates.iloc[0:len(World_dates):4], rotation=-90)  # let the x-axis less crowded
plt.ylabel('Population')  # give y-axis a label
plt.show()



y = 0
mylist4 = []
for y in range(0, len(covid_data)):  # similar to the previous tasks, use for loop
    y = covid_data.loc[y, "location"]
    if y == "Spain":
        mylist4.append(True)
    else:
        mylist4.append(False)
Spain_new_cases = np.array(covid_data.loc[mylist4, "new_cases"])
Spain_total_cases = np.array(covid_data.loc[mylist4, "total_cases"])
Spain_dates = covid_data.loc[mylist4, "date"]

l3, = plt.plot(Spain_dates, Spain_new_cases, 'y.')
l4, = plt.plot(Spain_dates, Spain_total_cases, 'g.')  # show the difference between two kinds of dots, give them different colors
plt.gcf().autofmt_xdate()
plt.title('New cases and total cases in Spain')
plt.legend(handles=[l3, l4, ], labels=['Spain new cases', 'Spain total cases'], loc='upper left')
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4], rotation=-90)  # let the x-axis less crowded
plt.ylabel('Population')  # give y-axis a label
plt.show()
