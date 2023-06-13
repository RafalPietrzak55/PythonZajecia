import numpy as np
from numpy import nan as NA
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('turcja.xlsx')
adana_data = df[df['city'] == 'Adana']
adana_data = adana_data[(adana_data['years'] >= 2005) & (adana_data['years'] <= 2010)]
print(adana_data)
plt.bar(adana_data['years'], adana_data['cinema_audiences'])
plt.xlabel('Rok')
plt.ylabel('Widzowie kin')
plt.title('Widzowie kin w mieście Adana (2005-2010)')
plt.show()