import numpy as np
import matplotlib.pyplot as plt
gene_lengths = [9410, 394141, 4442, 105338, 19149, 76779, 126550, 36296, 842, 15981]
exon_counts = [51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523]    # import the data
a = np.array(gene_lengths)
b = np.array(exon_counts)  # give them names separately for convenience
length = a/b  # calculate the average
plt.boxplot(length,
            vert=True,
            whis=1.5,  # Western plotgigit
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
            )
plt.show()
