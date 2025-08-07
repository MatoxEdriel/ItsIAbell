
phrases = [
    "¿Qué puedes hacer?",
    "¿Qué sabes hacer?",
    "¿Me puedes ayudar?",
    "Necesito apoyo con algo",
    "Hola",
    "Buenos días",
    "Chao",
    "Adiós"
]
intention = [
    "capacidad",
    "capacidad",
    "ayuda",
    "ayuda",
    "saludo",
    "saludo",
    "despedida",
    "despedida"
]


with open("data.set", "w", encoding = "utf-8") as file:
    for phrase, intentions in zip(phrases, intention):
        file.write(f"{phrase}|{intentions}\n")
