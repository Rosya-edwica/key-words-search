import csv


def load_texts(path: str) -> list[str]:
    if not path.endswith(".csv"): 
        exit(f"Неправильный формат файла: {path}. Должен быть .csv")
    
    data = []
    with open(path, encoding="utf-8", newline="") as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            data.append(i[0])
    return data