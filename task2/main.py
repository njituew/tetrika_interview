import requests
from bs4 import BeautifulSoup
from collections import defaultdict

def count_animals_by_letter(url):
    base_url = "https://ru.wikipedia.org"
    counts = defaultdict(int)  # Словарь для хранения подсчётов
    
    while url:
        print(f"Парсим страницу: {url}")
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Ошибка при загрузке страницы: {response.status_code}")
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        items = soup.select(".mw-category-group ul li a")
        for item in items:
            animal_name = item.text.strip()
            if animal_name:
                first_letter = animal_name[0].upper()
                counts[first_letter] += 1
        
        next_page = soup.select_one("a:contains('Следующая страница')")
        if next_page:
            url = base_url + next_page["href"]
        else:
            url = None
    
    return counts

start_url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"

result = count_animals_by_letter(start_url)

for letter, count in sorted(result.items()):
    print(f"{letter}: {count}")
