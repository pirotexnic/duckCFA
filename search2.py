from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

def googlefind(query):
    # Создаем объект для выполнения поиска
    ddgs = DDGS()
    
    # Выполняем поиск и получаем результаты в виде списка
    results = ddgs.text(query, region='wt-wt', safesearch='Moderate', timelimit='y')

    if results:
        # Получаем первый результат
        first_result = results[0]
        print(f"Найдено: {first_result['title']}")
        print(f"Ссылка: {first_result['href']}")

        # Если ссылка содержит "wikipedia", пытаемся парсить её
        if "wikipedia.org" in first_result['href']:
            get_wikipedia_summary(first_result['href'])
        else:
            print("Краткий ответ не найден на Википедии.")
    else:
        print("Ничего не найдено.")

def get_wikipedia_summary(url):
    # Получаем HTML содержимое страницы
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим первый абзац статьи
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        if paragraph.text.strip():
            print("Краткий ответ из Википедии:")
            print(paragraph.text.strip())
            break

if __name__ == "__main__":
    query = input("Введите запрос: ")
    googlefind(query)
