from duckduckgo_search import DDGS

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
    else:
        print("Ничего не найдено.")

if __name__ == "__main__":
    query = input("Введите запрос: ")
    googlefind(query)
