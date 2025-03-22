     # dialog.py
def lilia_dialog(player, lilia):
    print(f"{lilia.name}: {lilia.dialogue}")
    print("1. Спросить о травах")
    print("2. Рассказать о своей ферме")
    print("3. Уйти")

    choice = input("Выберите: ")

    if choice == "1":
        print(f"{lilia.name}: Я знаю много о травах. Что ты хочешь узнать?")
             # TODO: Добавить более сложные варианты диалога
    elif choice == "2":
        print(f"{lilia.name}: Интересно. Твоя ферма звучит многообещающе.")
             # TODO: Добавить изменение отношений
    elif choice == "3":
        print("До свидания.")
    else:
        print("Неверный выбор.")

     # locations.py
def talk_to_lilia(self, player, current_location):
    dialog.lilia_dialog(player, characters.lilia)
    return current_location