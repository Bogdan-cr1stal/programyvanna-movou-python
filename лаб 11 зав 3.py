import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords, gutenberg
import string
import nltk

#Завантаження ресурсів NLTK
nltk.download('stopwords', quiet=True)
nltk.download('gutenberg', quiet=True)
# Функція обрахунку кількісті слів
def count_words(tokens):
    return len(tokens)
# Побудова графіка найбільш уживаних слів
def most_used_words(tokens, title_suffix=""):
    k_words = Counter(tokens)
    cort = k_words.most_common(10)
    # Розділяємо слова (x) та їхні частоти (y)
    x = [cort[i][0] for i in range(len(cort))]
    y = [cort[i][1] for i in range(len(cort))]

    plt.bar(x, y, color='blue')
    plt.title(f"10 найбільш вживаних слів у тексті {title_suffix}")
    plt.xlabel("Слова")
    plt.ylabel("Кількість")
    plt.show()

def most_used_words_clear_text(tokens):
    stops = set(stopwords.words('english'))
    clean_tokens = [t.lower() for t in tokens if t not in string.punctuation and t.lower() not in stops]
    most_used_words(clean_tokens, "(очищений текст)")

# замінює пунктуацію пробілами та ділить текст на слова
def simple_tokenize(text):
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    text = text.translate(translator)#заміна всіх знаків пунктуації
    tokens = text.split()#розбиття на слова
    return tokens
#Читання тексту з Project Gutenberg
file_id = "blake-poems.txt"

try:
    text = gutenberg.raw(file_id)
    print(f"Текст '{file_id}' успішно завантажено з Project Gutenberg.")
except:
    print(f"Помилка: файл '{file_id}' недоступний у корпусі Project Gutenberg.")
    text = ""

if text:
    tokens = simple_tokenize(text)
    print("Кількість слів у тексті =", count_words(tokens))

    #ТОП-10 без очищення
    most_used_words(tokens, "(оригінальний текст)")
    #ТОП-10 з очищенням
    most_used_words_clear_text(tokens)