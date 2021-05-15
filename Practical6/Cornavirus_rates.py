import matplotlib.pyplot as plt
from matplotlib import gridspec
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'  # import different country names
a = 29862124
b = 11285561
c = 11205972
d = 4360823
e = 4234924  # import data from the five countries
f = a+b+c+d+e  # sum up all the data
L = [a/f, b/f, c/f, d/f, e/f]  # calculate the percent that every country has occupied
D = {'USA': a/f, 'India': b/f, 'Brazil': c/f, 'Russia': d/f, 'UK': e/f}
print(D)

F = []
for i in range(5):
    x = round(L[i], 2)
    F.append(x)
print(F)

gs = gridspec.GridSpec(4, 1)
plt.figure(figsize=(8, 7))

plt.subplot(gs[:3, 0])
sizes = [round(a*100/f, 2), round(b*100/f, 2), round(c*100/f, 2), round(d*100/f, 2), round(e*100/f, 2)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1)  # take the pies apart to see more clearly
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.title('Coronavirus rates', fontsize='large')
plt.axis('equal')

plt.subplot(gs[3, 0])
plt.axis('off')
rowLabels = ['Country', 'Frequency']
cellText = [labels, F]
table = plt.table(cellText=cellText, rowLabels=rowLabels, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 5)
plt.show()
