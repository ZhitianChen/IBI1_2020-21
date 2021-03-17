import numpy as np
import matplotlib.pyplot as plt
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK' # import different country names
a = 29862124
b = 11285561
c = 11205972
d = 4360823
e = 4234924  # import data from the five countries
f = a+b+c+d+e  # sum up all the data
L = [a/f, b/f, c/f, d/f, e/f] # calculate the percent that every country has occupied
sizes = [round(a*100/f, 2), round(b*100/f, 2), round(c*100/f, 2), round(d*100/f, 2), round(e*100/f, 2)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1) # take the pies apart to see more clearly
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()

