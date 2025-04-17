import random

def play_rps():
    def game(user_choice, cmp_choice):
        if user_choice == cmp_choice:
            return 2  # tie
        elif (user_choice == "rock" and cmp_choice == "paper") or \
             (user_choice == "paper" and cmp_choice == "scissors") or \
             (user_choice == "scissors" and cmp_choice == "rock"):
            return 0  # loss
        elif (user_choice == "rock" and cmp_choice == "scissors") or \
             (user_choice == "paper" and cmp_choice == "rock") or \
             (user_choice == "scissors" and cmp_choice == "paper"):
            return 1  # win
        else:
            return 3  # invalid input

    art_comp = {
        "rock": '''
  _______
 (____   '---
(_____)
(_____)
 (____)
  (___)__.---
''',
        "paper": '''
       ______   
  ____(___  '---
 (______
(_______
  (_______
    (_______.---
''',
        "scissors": ''' 
      _______     
  ___(___    '---
 (______
(_______
      (____)
       (___)__.---
'''
    }

    art_user = {
        "rock": '''
    _______ 
---'   ____)
      (_____)
      (_____)
      (____)
---.(____)
''',
        "paper": '''
    _______
---'    ___)____
           ______)
          _______)
         _______)
---._______)
''',
        "scissors": '''
    ______
---'   ___)_______
          ________)
       __________)
      (____)
---.(____)
'''
    }

    print("\nWelcome to Rock, Paper, Scissors!")

    # Initialize score counters
    wins = 0
    losses = 0
    ties = 0

    while True:
        user_choice = input("\nEnter Rock, Paper, or Scissors: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please try again.")
            continue

        # Generate computer's choice
        cmp_choice_num = random.randint(1,3)
        if(cmp_choice_num == 1):
            cmp_choice = "rock"
        elif(cmp_choice_num == 2):
            cmp_choice = "paper"
        elif(cmp_choice_num == 3):
            cmp_choice = "scissors"

        print("\nYou chose:", user_choice)
        print("Computer chose:", cmp_choice)

        # Display side-by-side ASCII Art
        user_lines = art_user[user_choice].splitlines()
        comp_lines = art_comp[cmp_choice].splitlines()
        max_lines = max(len(user_lines), len(comp_lines))
        user_width = max(len(line) for line in user_lines)

        print()
        for i in range(max_lines):
            u_line = user_lines[i] if i < len(user_lines) else " " * user_width
            c_line = comp_lines[i] if i < len(comp_lines) else ""
            separator = " V/S " if i == 0 else "     "
            print(f"{u_line:<{user_width}}{separator}{c_line}")
        print()

        # Determine result and update counters
        result = game(user_choice, cmp_choice)
        if result == 1:
            print("🎉 You won the game!")
            wins += 1
        elif result == 0:
            print("😞 You lost the game!")
            losses += 1
        elif result == 2:
            print("😐 The game is a tie!")
            ties += 1

        # Print running score
        print(f"\n🏆 Score -> Wins: {wins}, Losses: {losses}, Ties: {ties}")

        # Replay option
        next_move = input("\nEnter 'Quit' to exit the game or 'Play' to play again: ").strip().lower()
        if next_move == "quit":
            print("Thanks for playing!")
            break
        elif next_move == "play":
            print("Let's play again!")
            continue
        else:
            print("Please enter a valid input ('Play' or 'Quit').")

if __name__ == '__main__':
    play_rps()
