import pymorphy2

def get_noun_words(text) -> list[str]:
    noun_words: list[str] = []
    morph = pymorphy2.MorphAnalyzer()
    for word in text.split():
        parsed = morph.parse(word)[0]
        if parsed.tag.POS == "NOUN":
            noun_words.append(parsed.normal_form)
    return noun_words

def test(text: str):
    """Надо машинного обучения привести в вид машинный обучение"""
    m = pymorphy2.MorphAnalyzer()
    parsed_words = [m.parse(word)[0] for word in text.split()]
    for i in parsed_words:
        print(i)