import random

def number_guessing_game():
    print("\nWelcome to the Number Guessing Game!")
    while True:
        print()
        number_to_guess = random.randint(1, 100)
        attempts = 0
        guess = None

        while guess != number_to_guess:
            guess = input("Guess a number between 1 and 100 (or type 'exit' to go back to the main menu): ")
            if guess.lower() == 'exit':
                return
            guess = int(guess)
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the right number in {attempts} attempts.")

def rock_paper_scissors():
    print("\nWelcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]

    while True:
        print()
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (rock, paper, scissors, or 'exit' to go back to the main menu): ").lower()

        if user_choice == "exit":
            return

        while user_choice not in choices:
            user_choice = input("Invalid choice. Please enter rock, paper, scissors, or 'exit': ").lower()

        if user_choice == "exit":
            return

        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

def simple_calculator():
    print("\nWelcome to the Simple Calculator!")
    while True:
        print()
        expression = input("Enter an arithmetic expression (e.g., 3 + 4) or type 'exit' to go back to the main menu: ")
        if expression.lower() == 'exit':
            return
        try:
            num1, operator, num2 = expression.split()
            num1, num2 = float(num1), float(num2)

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero is not allowed.")
                    continue
            else:
                print("Invalid operator. Please use one of +, -, *, /.")
                continue

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter a valid arithmetic expression.")

def main():
    while True:
        print("\nChoose a game to play:")
        print("1. Number Guessing Game")
        print("2. Rock, Paper, Scissors")
        print("3. Simple Calculator")
        print("4. Exit games")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            number_guessing_game()
        elif choice == 2:
            rock_paper_scissors()
        elif choice == 3:
            simple_calculator()
        elif choice == 4:
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
