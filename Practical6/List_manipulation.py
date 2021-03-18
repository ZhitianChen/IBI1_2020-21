# draw a box plot
import numpy as np
import matplotlib.pyplot as plt
gene_lengths = [9410, 394141, 4442, 105338, 19149, 76779, 126550, 36296, 842, 15981]
exon_counts = [51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523]    # import the data
a = np.array(gene_lengths)
b = np.array(exon_counts)  # give them names separately for convenience
length = a/b  # calculate the average
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
plt.show()  # show the plot
