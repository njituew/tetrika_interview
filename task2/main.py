import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import time
import csv

def count_animals_by_letter(url, output_file):
    base_url = "https://ru.wikipedia.org"
    counts = defaultdict(int)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    while url:
        print(f"Парсим страницу: {url}")
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка соединения: {e}. Ждём 5 секунд...")
            time.sleep(5)
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.select(".mw-category-group ul li a")
        for item in items:
            animal_name = item.text.strip()
            if animal_name and ("А" <= animal_name[0].upper() <= "Я" or animal_name[0].upper() == "Ё"):
                first_letter = animal_name[0].upper()
                counts[first_letter] += 1
            else:
                url = None

        next_page = soup.select_one("a:contains('Следующая страница')")
        if next_page:
            url = base_url + next_page["href"]
        else:
            url = None

        time.sleep(0.5)  # Пауза между запросами

    # Сохраняем результат
    with open(output_file, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for letter, count in sorted(counts.items()):
            writer.writerow([letter, count])

    print(f"Результаты сохранены в файл: {output_file}")


if __name__ == "__main__":
    start_url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"
    output_file = "task2/beasts.csv"

    count_animals_by_letter(start_url, output_file)
