from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

def googlefind(query):
    # Создаем объект для выполнения поиска
    ddgs = DDGS()

    # Выполняем поиск и получаем результаты в виде списка
    results = ddgs.text(query, region='wt-wt', safesearch='Moderate', timelimit='y')

    if results:
        # Пытаемся найти результат с Википедии
        wiki_result = next((res for res in results if "wikipedia.org" in res['href']), None)

        if wiki_result:
            print("Информация найдена на Википедии:")
            get_wikipedia_summary(wiki_result['href'])
        else:
            print("Информация с других источников:")
            # Если нет Википедии, используем первый результат из других источников
            first_result = results[0]
            print(f"{first_result['title']}")
            print(f"Описание: {first_result.get('body', 'Описание не найдено')}")
    else:
        print("Ничего не найдено.")

def get_wikipedia_summary(url):
    # Получаем HTML содержимое страницы
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем первый непустой абзац с текстом
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        text = paragraph.get_text(strip=True)
        # Фильтруем ненужные абзацы и проверяем на содержание полезной информации
        if text and not text.lower().startswith(('см.', 'это статья', 'этот термин')):
            print("\nТекст из Википедии:")
            print(text)
            break
    else:
        print("Не удалось найти основной текст на странице.")

if __name__ == "__main__":
    query = input("Введите запрос: ")
    googlefind(query)
