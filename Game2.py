import random

# Список слов, которые нужно угадать
words = ["кот", "собака", "мышь", "слон", "жираф", "тигр"]
def display_word(word, guessed_letters) #отображает угаданные буквы в слове
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
def main():
    # Выбор случайного слова из списка
    word_to_guess = random.choice(words).lower()
    guessed = []
    attempts = 6
    print("Добро пожаловать в игру 'Поле чудес'!")
    print(display_word(word_to_guess, guessed))
    while True:
        guess = input("Угадайте букву или введите слово целиком: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed:
                print("Вы уже угадали эту букву")
            elif guess in word_to_guess:
                guessed.append(guess)
                print("Поздравляю! Вы угадали букву.")
            else:
                print("К сожалению, такой буквы нет в слове.")
                attempts -= 1
        elif len(guess) == len(word_to_guess) and guess.isalpha():
            if guess == word_to_guess:
                print("Поздравляю! Вы угадали слово!")
                break
            else:
                print("К сожалению, это не правильное слово.")
                attempts -= 1
        else:
            print("Пожалуйста, введите одну букву или слово целиком.")
        print(display_word(word_to_guess, guessed))
        print("У вас осталось", attempts, "попыток.")

        if attempts == 0:
            print("У вас закончились попытки. Загаданное слово было:", word_to_guess)
            break
        if "_" not in display_word(word_to_guess, guessed):
            print("Поздравляю! Вы угадали слово!")
            break
