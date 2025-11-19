import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

#1 Читання XML
def load_xml(path):
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return None
    except ET.ParseError:
        print("Помилка: некоректний XML-файл.")
        return None

#2 Перетворення XML → DataFrame
def xml_to_dataframe(root):
    books = []
    for b in root.findall("book"):
        books.append({
            "title": b.findtext("title", default=""),
            "author": b.findtext("author", default=""),
            "year": int(b.findtext("year", default=0)),
            "genre": b.findtext("genre", default=""),
            "price": float(b.findtext("price", default=0))
        })
    return pd.DataFrame(books)

#3 Фільтрація даних
def filter_books(df, genre=None, year=None):
    if genre:
        df = df[df["genre"] == genre]
    if year:
        df = df[df["year"] == year]
    return df

#4 Аналіз даних
def analyze(df):
    print("Кількість записів:", len(df))
    if len(df) > 0:
        print("Найпопулярніший жанр:", df["genre"].mode()[0])
        print("Середня ціна:", df["price"].mean())

#5 Побудова графіка
def plot_year_distribution(df):
    df["year"].value_counts().sort_index().plot(kind="bar")
    plt.title("Кількість книг за роками")
    plt.xlabel("Рік")
    plt.ylabel("Кільність")
    plt.tight_layout()
    plt.show()

#Функція перевірки так або ні
def yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ["так"]:
            return True
        if ans in ["ні"]:
            return False
        print("Помилка: введіть 'так' або 'ні'. Спробуйте ще раз.\n")

#Перевірка коректності вводу жанру
def input_genre(df):
    genres = df["genre"].unique()
    print("\nДоступні жанри:", ", ".join(genres))

    while True:
        genre = input("Введіть жанр для фільтрації (або Enter): ").strip()
        if genre == "":
            return None
        if genre in genres:
            return genre
        print("Помилка: такого жанру немає. Спробуйте ще.")

#Перевірка коректності вводу року
def input_year(df):
    years = df["year"].unique()
    print("\nДоступні роки:", ", ".join(map(str, years)))

    while True:
        year = input("Введіть рік для фільтрації (або Enter): ").strip()
        if year == "":
            return None
        if year.isdigit() and int(year) in years:
            return int(year)
        print("Помилка: некоректний рік. Спробуйте ще.")

#Основна програма
def main():
    #повторний запит шляху
    while True:
        path = input("Введіть шлях до XML-файлу: ").strip()
        root = load_xml(path)
        if root is not None:
            break
        print("Спробуйте ще раз.\n")

    df = xml_to_dataframe(root)
    print("\nВсього знайдено записів:", len(df))

    genre = input_genre(df)
    year = input_year(df)

    df_filtered = filter_books(df, genre, year)

    print("\n    Результати фільтрації    ")
    print(df_filtered)

    analyze(df_filtered)

    #Перевірений запит графіка
    if yes_no("Побудувати графік? (так/ні): "):
        plot_year_distribution(df_filtered)

    #Перевірений запит CSV
    if yes_no("Зберегти результати у CSV? (так/ні): "):
        df_filtered.to_csv("books_filtered.csv", index=False)
        print("Файл збережено як books_filtered.csv")

if __name__ == "__main__":
    main()
