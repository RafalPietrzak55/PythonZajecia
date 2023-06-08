import matplotlib.pyplot as plt

# Dane
names = ['RMF FM', 'Radio Zet','Eska','Inne']
percentages = [24.8, 13.0, 6.7, 55.5]
colors = ['pink', 'blue', 'green', 'purple']
explode = (0.1, 0, 0, 0)  # Wyróżnienie segmentu Kategoria B

# Tworzenie wykresu kołowego
plt.pie(percentages, explode=explode, labels=names, colors=colors, autopct='%1.1f%%', shadow=True, startangle=80)

# Dodanie tytułu
plt.title('Wyniki słuchalności - II - IV 2017')

# Równomierne skalowanie osi X i Y, aby koło było okrągłe
plt.axis('equal')

plt.show()