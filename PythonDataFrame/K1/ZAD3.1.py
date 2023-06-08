import numpy as np
from numpy import nan as NA
import matplotlib.pyplot as plt
import pandas as pd

# Wczytanie danych z pliku stacjepaliw.xlsx
data = pd.read_excel('C:\GITHUB\PythonZajecia\PythonDataFrame\K1\stacjepaliw.xlsx')

data.sort_values(by='Nazwa', inplace=True)

# Wyodrębnienie danych dla województwa śląskiego i małopolskiego
woj_slaskie = data[data['Nazwa'] == 'ŚLĄSKIE']
woj_malopolskie = data[data['Nazwa'] == 'MAŁOPOLSKIE']

# Stworzenie wykresu liniowego
plt.plot(data.columns[1:], woj_slaskie.values[0][1:], label='Województwo Śląskie')
plt.plot(data.columns[1:], woj_malopolskie.values[0][1:], label='Województwo Małopolskie')

# Ustawienie etykiet osi i tytułu wykresu
plt.xlabel('Rok')
plt.ylabel('Liczba Stacji paliw')
plt.title('Liczba Stacji paliw w Województwie Śląskim i Małopolskim')

# Dodanie legendy
plt.legend()

# Zapisanie wykresu do pliku PNG
plt.savefig('wykres.png', dpi=300)
