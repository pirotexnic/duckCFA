from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

def googlefind(query):
    # Создаем объект для выполнения поиска
    ddgs = DDGS()
    
    # Выполняем поиск и получаем результаты в виде списка
    results = ddgs.text(query + " site:wikipedia.org", region='wt-wt', safesearch='Moderate', timelimit='y')

    if results:
        # Получаем первый результат
        first_result = results[0]

        # Парсим содержимое страницы Википедии и выводим краткий ответ
        get_wikipedia_summary(first_result['href'])
    else:
        print("Ничего не найдено.")

def get_wikipedia_summary(url):
    # Получаем HTML содержимое страницы
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим краткий ответ, который может быть в первом <b> или <strong>
    title = soup.find('b') or soup.find('strong')
    if title:
        print(f"Краткий ответ: {title.text.strip()}")

    # Находим первый абзац статьи
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        if paragraph.text.strip():
            print("\nТекст из Википедии:")
            print(paragraph.text.strip())
            break

if __name__ == "__main__":
    query = input("Введите запрос: ")
    googlefind(query)
