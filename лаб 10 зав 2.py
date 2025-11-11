import numpy as np
import matplotlib.pyplot as plt
import sys
import os

#користувачі інтернету на 100 осіб
x = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y = [3.7, 4.5, 6.6, 11, 17.9, 23.3, 28.7, 35.3, 41, 46.2, 48.9, 53, 58.9, 60, 61.7, 66.3]  # Україна
z = [68, 68.9, 75, 74, 71, 71.4, 69.7, 74.7, 71.4, 73, 74.6, 85.5, 87.3, 88, 89.4, 90.1]  # США

#Лінійні графіки для двох країн
plt.plot(x, y, label='Ukraine', color="blue", linewidth=3)
plt.plot(x, z, label='USA', color="red", linewidth=3)

plt.title('Internet users (per 100 people) (2005–2020)', fontsize=15)
plt.xlabel('Year', fontsize=12, color='black')
plt.ylabel('Internet users', fontsize=12, color='black')
plt.legend()
plt.grid(True)
plt.show()

#Стовпчаста діаграма для вибраної країни
country = input("Введіть країну (Ukraine або USA): ").strip()

if country.lower() == "ukraine":
    values = y
    color = "blue"
elif country.lower() == "usa":
    values = z
    color = "red"
else:
    print("Невідома країна! Використано Україну за замовчуванням.")
    values = y
    country = "Ukraine"
    color = "blue"

plt.bar(x, values, color=color)
plt.title(f'Internet users (per 100 people) — {country}', fontsize=15)
plt.xlabel('Year', fontsize=12, color='black')
plt.ylabel('Internet users', fontsize=12, color='black')
plt.grid(axis='y')
plt.show()
