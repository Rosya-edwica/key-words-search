import csv

def save(data: list):
    with open("key_words.csv", encoding="utf-8", mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(("original", "key_word"))
        writer.writerows(data)
