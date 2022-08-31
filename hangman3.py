
from hangmanscrib import stages
from hangmanwords import word_list
import random

display = []
chosenword = random.choice(word_list)
wordlength = len(chosenword)

for i in chosenword:
    display.append("_")
print(' '.join(display))

lives = 6
endgame = False

while not endgame:
    guess = input("Guess a letter ").lower()
    if guess in display:
        print("You have already guessed the letter")
    
    if guess not in chosenword:
        print(f"You guessed {guess}, that is not in the list, you lose one life")
        lives -= 1
        if lives == 0:
            endgame = True
            print("You lose")
    
    for position in range(wordlength):
        letter = chosenword[position]
        if letter == guess:
             display[position] = letter
            
    
    print(' '.join(display))
    print(stages[lives])