import numpy as np
from numpy import nan as NA
import matplotlib.pyplot as plt
import pandas as pd

names = ['inne','RMF FM','Radio Zet','Eska']
percentages = [55,25,13,7]
colors = ['pink', 'green', 'orange', 'purple']
explode = (0,0,0,0.15)

plt.pie(percentages, labels=names, colors=colors, explode=explode, startangle=295,autopct='%1.1f%%')
plt.title('Wyniki słuchalności - II-IV 2017')
plt.show()


