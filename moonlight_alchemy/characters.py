   # characters.py
class NPC(Character):
    def __init__(self, name, health, dialogue):
        super().__init__(name, health)
        self.dialogue = dialogue
        self.relationship = 0  # Начальный уровень отношений

    def talk(self, player):
           # Теперь диалог зависит от relationship
        if self.relationship > 50:
            print(f"{self.name}: Рад тебя видеть, {player.name}! Что привело тебя ко мне?")
        elif self.relationship < -20:
            print(f"{self.name}: Что тебе нужно? Не мешай мне.")
        else:
            print(f"{self.name}: {self.dialogue}")  # Базовый диалог
