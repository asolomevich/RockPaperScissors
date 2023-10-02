import random

def get_user_choice():
    choice = input("Выберите: камень (r), ножницы (s), бумага (p): ").lower()
    if choice in ['r', 's', 'p']:
        return choice
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        return get_user_choice()

def get_computer_choice():
    choices = ['r', 's', 'p']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 's' and computer_choice == 'p') or \
         (user_choice == 'p' and computer_choice == 'r'):
        return "На этот раз выйграли вы!"
    else:
        return "Компьютер выиграл! Ура!"

def play_game():
    print("Игра началась!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

play_game()