meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "ВАРИК": "Просто обычный вариант",
            "РОФЛ": "Шутка",
            "ЩИЩ": "Одобрение или восторг",
            "КРИПОВЫЙ": "Страшный, пугающий",
            "АГРИТЬСЯ": "Злиться"
            }
word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
    # Что делать, если слово нашлось?
      if word == "КРИНЖ":
                print("Что-то очень странное или стыдное")
      if word == "ЛОЛ":
                print("Что-то очень смешное")
      if word == "ВАРИК":
                print("Просто обычный вариант")
      if word == "РОФЛ":
                print("Шутка")
      if word == "ЩИЩ":
                print("Одобрение или восторг")
      if word == "КРИПОВЫЙ":
                print("Страшный, пугающий")
      if word == "АГРИТЬСЯ":
                print("Злиться")
else:
    # Что делать, если слово не нашлось?
        print("Извините, такого слова тут нету")
