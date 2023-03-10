import yake


def get_extractor(text) -> yake.KeywordExtractor:
    if set(text.lower()) & {"а", "о", "у", "е", "и"}:
        return yake.KeywordExtractor(lan="ru", n=2, dedupLim=0.3, top=3)
    else:
        return yake.KeywordExtractor(lan="en", n=4, dedupLim=0.3, top=3)
    

def get_key_word_by_yake(text: str) -> str:
    extractor = get_extractor(text)
    words = extractor.extract_keywords(text)
    max_result = 0
    best_choise = ""
    for i in words:
        if i[1] > max_result:
            best_choise, max_result = i

    return best_choise    