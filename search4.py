from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

def googlefind(query):
    # Создаем объект для выполнения поиска
    ddgs = DDGS()
    
    # Выполняем поиск и получаем результаты в виде списка, ограничиваем сайт Википедией
    results = ddgs.text(query + " site:ru.wikipedia.org", region='wt-wt', safesearch='Moderate', timelimit='y')

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

    # Пытаемся получить первый абзац с основным текстом
    paragraphs = soup.find_all('p')

    # Ищем первый непустой абзац с текстом
    for paragraph in paragraphs:
        text = paragraph.get_text(strip=True)
        if text and not text.lower().startswith(('см.', 'это статья', 'этот термин')):
            print("\nТекст из Википедии:")
            print(text)
            break
    else:
        print("Не удалось найти основной текст на странице.")

if __name__ == "__main__":
    query = input("Введите запрос: ")
    googlefind(query)
