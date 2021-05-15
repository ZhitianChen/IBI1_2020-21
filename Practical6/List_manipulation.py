# draw a box plot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
gene_lengths = [9410, 394141, 4442, 105338, 19149, 76779, 126550, 36296, 842, 15981]
exon_counts = [51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523]    # import the data
a = np.array(gene_lengths)
b = np.array(exon_counts)  # give them names separately for convenience
length = a/b  # calculate the average

F = []
for i in range(9):
    x = round(length[i], 2)
    F.append(x)
F.sort(reverse=True)

gs = gridspec.GridSpec(4, 1)
plt.figure(figsize=(10, 7))

plt.subplot(gs[:3, 0])
plt.boxplot(length,  # use the data from "length" to create the data
            vert=True,  # set the box plot ventricle
            whis=1.5,  # Western plot
            patch_artist=True,  # color the box
            meanline=False,  # use a line to represent the mean value
            showbox=True,  # show the box line
            showcaps=True,  # show the lines which represent the maximum and the minimum
            showfliers=True,  # show the outliers
            notch=False,  # do not show the plot with notches
            )
plt.title('Average exon lengths')  # to give a title of the plot

plt.subplot(gs[3, 0])
plt.axis('off')
rowLabels = ['Average exon lengths']
cellText = [F]
table = plt.table(cellText=cellText, rowLabels=rowLabels, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)

plt.show()  # show the plot
