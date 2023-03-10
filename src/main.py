import re
import db
import filters


def prepare_text(text: str) -> str: 
    without_bracked_text = re.sub("\(([^)]*)\)", "", text)
    return " ".join(set(without_bracked_text.lower().split()) - filters.STOP_WORDS)


def getKeyWords(text: str) -> set[str]:
    key_words: list[str] = []
    key_words += filters.get_noun_words(text)
    key_words += filters.get_abbreviation(text) 
    key_words += filters.get_colon_words(text) # 
    key_words.append(filters.get_key_word_by_yake(text))
    languages = filters.get_languages(text)
    if languages:key_words.append(languages)

    return set([i.lower() for i in key_words])



if __name__ == "__main__":
    data_path = input("Введите путь до файла со списком наименований в формате .csv: ")
    data = db.load_texts(data_path)
    result: list[list[str, str]] = []
    
    print("Запустили поиск ключевых слов...")
    for index, i in enumerate(data):
        key_words = getKeyWords(prepare_text(i))
        result.append((i, "|".join(key_words)))
    print("Готово! Результат в файле: key_words.csv.")
    db.save(result)
