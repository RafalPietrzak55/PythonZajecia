import numpy as np
from numpy import nan as NA
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('stacjepaliw.xlsx')

sorted_df = df.sort_values(by='2019', ascending=False)

sorted_df.to_excel('posortowane_dane.xlsx', index=False)

wielkopolskie = sorted_df[sorted_df['Nazwa'] == 'WIELKOPOLSKIE']
zachodniopomorskie = sorted_df[sorted_df['Nazwa'] == 'ZACHODNIOPOMORSKIE']

plt.plot(sorted_df.columns[1:],wielkopolskie.values[0][1:], label='WIELKOPOLSKIE')
plt.plot(sorted_df.columns[1:],zachodniopomorskie.values[0][1:], label='ZACHODNIOPOMORSKIE')

plt.title('Ilość stacji paliw w wybranych Województwach')
plt.xlabel('Rok')
plt.ylabel('Ilość stacji paliw')
plt.legend()

plt.savefig('wykres2.png', dpi=300)

plt.show()

print(sorted_df)