import numpy as np
from numpy import nan as NA
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('turcja.xlsx')



ankara_data = df[df['city'] == 'Ankara']
ankara_data = ankara_data[(ankara_data['years'] >= 2005) & (ankara_data['years'] <= 2010)]
print(ankara_data)
plt.bar(ankara_data['years'], ankara_data['pop'])
plt.xlabel('Rok')
plt.ylabel('Populacja')
plt.title('Populacja w mieście Ankara (2005-2010)')
plt.show()


