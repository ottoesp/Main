import numpy as np
import matplotlib.pyplot as plt

data = [1, 4, 2, 9, 12, 34, -13, 5]

fig2, ax2 = plt.subplots()
ax2.set_title('Notched boxes')
ax2.boxplot(data, notch=True)

