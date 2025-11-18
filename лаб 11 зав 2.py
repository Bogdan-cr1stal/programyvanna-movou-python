import pandas as pd
import matplotlib.pyplot as plt

#Читання CSV
df = pd.read_csv('comptagevelo20152.csv', encoding='latin1')
df.columns = df.columns.str.encode('latin1').str.decode('utf8')

#Створення дати
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Unnamed: 1'], dayfirst=True)
df = df.drop(columns=['Date', 'Unnamed: 1']).set_index('DateTime')

#Додавання місяця
df['Month'] = df.index.month

print("\nПерші 5 рядків")
print(df.head())

print("\nІнформація про DataFrame")
print(df.info())

print("\nОписова статистика")
print(df.describe())

#Числові колонки
numeric_cols = df.select_dtypes('number').columns.drop('Month')

#Загальна кількість
total_year = df[numeric_cols].sum().sum()
print("\nЗагальна кількість велосипедистів за рік:", total_year)

print("\nСума за кожною велодоріжкою:")
print(df[numeric_cols].sum())

#топ місяці для вибраних доріжок
lanes = ['Berri1', 'Brébeuf', 'Maisonneuve_2']

print("\nНайпопулярніший місяць для велодоріжки:")

for lane in lanes:
    top3 = (
        df.groupby('Month')[lane]
        .sum()
        .nlargest(1)
    )

    print(f"\n{lane}:")
    for month_num, value in top3.items():
        month_name = pd.to_datetime(f"2024-{month_num}-01").month_name(locale='uk_UA')
        print(f"  {month_name} — {value}")

#Графік
monthly = df.groupby('Month')[numeric_cols].sum()
first_lane = numeric_cols[0]
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)
plt.plot(monthly.index, monthly[first_lane], label=first_lane)
plt.title(f"Завантаженість велодоріжки {first_lane} по місяцях")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.tight_layout()
plt.show()
