
def get_languages(text) -> str | None:
    try:
        for index, word in enumerate(text.split()):
            if word.lower() in {"язык", "языка", "языке"}:
                return text.split()[index-1] + " язык"
    except IndexError:
        return None