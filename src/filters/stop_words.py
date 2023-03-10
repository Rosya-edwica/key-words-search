

with open("stop-ru.txt", "r") as file:
    STOP_WORDS = set(i.replace("\n", "") for i in file.readlines())

STOP_WORDS |= {
    "часть",
    "тест",
    "тестовый",
    "вуз",
    "курс",
    "общий",
    "создание",
    "практика",
    "введение",
    "основы",
    "основные",
    "модуль",
    "тема",
    "начинающих",
    ""
}