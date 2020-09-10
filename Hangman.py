import random

word_list = [
    'minister',
    'kitchen',
    'church', 
    'threaten',
    'search', 
    'anniversary',
    'outlet', 
    'trench', 
    'doubt', 
    'tree'
]

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_complete = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print(word_complete)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed ", guess)
            elif guess not in word:
                print(guess, " is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job, ", guess, " is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_complete)
                indicies = [i for i, letter in enumerate(word) if letter == guess]
                for index in indicies:
                    word_as_list[index] = guess
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed ", guess)
            elif guess != word:
                print(guess, " is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                giessed = True
                word_complete = word
        else:
            print("Not a valid guess")
        
        print("Tries: ", tries)
        print(word_complete)
        print("\n")
    if guessed:
        print("Congratulations, you guessed the word!")
    else:
        print("Sorry, you ran out of tries. The word was ", word)

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()