import random

colours = ["R", "G", "B", "Y", "W" , "O"]
tries = 10
code_length = 4

def generate_code():
    code = []

    for a in range(code_length):
        colour = random.choice(colours)
        code.append(colour)

    return code

def guess_code():
    while True:
        guess = input("guess: ").upper().split(" ")

        if len(guess) != code_length:
            print(f"you must guess {code_length} colours.")
            continue

        for colour in guess:
            if colour not in colours:
                print(f"invalid colour: (colour). try again.")
                break

        else:
            break

    return guess 

def check_code(guess, real_code):
    colour_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for colour in real_code:
        if colour not in colour_counts:
            colour_counts[colour] = 0
        colour_counts[colour] += 1
    
    for guess_colour, real_colour in zip(guess, real_code):
        if guess_colour == real_colour:
            correct_pos += 1
            colour_counts[guess_colour] -= 1

    for guess_colour, real_colour in zip(guess, real_code):
        if guess_colour in colour_counts and colour_counts[guess_colour] > 0:
            incorrect_pos += 1
            colour_counts[guess_colour] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"welcome to mastermind, you have {tries} to guess the code......")
    print("the vaild colours are", *colours)
    code = generate_code()
    for attempts in range(1, tries + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == code_length:
            print(f"you guessed the code in {attempts} tries!")
            break

        print(f"correct positions: {correct_pos} | incorrect positions: {incorrect_pos}")
    
    else:
        print("you ran out of tries, the code was:", *code)


        
if __name__ == "__main__":
    game()
    



