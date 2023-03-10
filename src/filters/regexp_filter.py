import re


def get_abbreviation(text: str) -> list[str]:
    """Ищем аббревиатуры и игнорируем слова, которые начинаются с большой буквы (len(word) > 1)"""

    return [word for word in re.findall("[A-Z]+|[А-Я]+", text) if len(word) > 1]

def get_colon_words(text: str) -> list[str]:
    """Ищем слова, после которых стоит двоеточие
    Например:\n
    Input: "Python: для начинающих" 
    Output: "Python" 
    """

    return [word.replace(":", "") for word in re.findall("\w+:|\w+ :", text)]