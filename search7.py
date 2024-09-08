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
            if not get_wikipedia_summary(wiki_result['href']):
                # Если не удалось найти текст, выводим информацию из других источников
                print("Текст на Википедии не найден, покажем другой источник.")
                show_alternative_result(results)
        else:
            # Если Википедия не найдена, используем первый результат из других источников
            print("Информация с других источников:")
            show_alternative_result(results)
    else:
        print("Ничего не найдено.")

def get_wikipedia_summary(url):
    # Получаем HTML содержимое страницы
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем основной контент статьи (например, первый абзац)
    paragraphs = soup.find_all('p')

    for paragraph in paragraphs:
        text = paragraph.get_text(strip=True)
        # Фильтруем ненужные абзацы и проверяем на содержание полезной информации
        if text and not text.lower().startswith(('см.', 'это статья', 'этот термин', 'this is an')):
            print("\nТекст из Википедии:")
            print(text)
            return True
    return False

def show_alternative_result(results):
    # Если Википедия не сработала, показываем информацию из других источников
    first_result = results[0]
    print(f"{first_result['title']}")
    print(f"Описание: {first_result.get('body', 'Описание не найдено')}")

if __name__ == "__main__":
    query = input("Введите запрос: ")
    googlefind(query)
