from random import shuffle
from json import load
from string import ascii_lowercase
def words():
    wordsetPermanent = open("words.txt").readlines()
    while True:
        wordset = wordsetPermanent
        shuffle(wordset)
        for word in wordset:
            yield word.strip("\n").strip("")

class conf:
    def __init__(self, **options):
        for option in options:
            setattr(self, option.replace(" ","_").strip().lower(), options[option])
config = conf(**load(open("config.json")))

class word:
    def __init__(self, word, guesses = config.allowed_incorrect_guesses):
        self.word = word
        self.remaining_guesses = guesses
        self.guessed_letters = []
    def guessLetter(self,letter):
        if letter in self.guessed_letters:
            print("You have already guessed {}".format(letter))
        elif letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            if letter in self.word:
                print("Good guess! {} is in the word".format(letter))
            else:
                print("Unlucky, {} isn't in the word".format(letter))
                self.remaining_guesses -= 1
    def formatWord(self):
        return "".join([x if not x.lower() in ascii_lowercase or x.lower() in self.guessed_letters else "*" for x in self.word])
    def allCorrect(self):
        return self.formatWord() == self.word
def main():
    for w in words():
        w = word(w)
        while w.remaining_guesses != 0:
            print("Word: {}".format(w.formatWord()))
            print("You have {} guesses left".format(w.remaining_guesses))
            letter = input("What is your guess?\n >>> ").lower().strip()
            while not letter in ascii_lowercase:
                letter = input("What is your guess?\n >>> ").lower().strip()
            w.guessLetter(letter)
            if w.allCorrect():
                print("Congratulations, you guessed the word {}".format(w.word))
                break
        if not w.allCorrect():
            print("Unlucky, you've ran out of guesses, the word was {}".format(w.word))
if  __name__ == "__main__":
    main()
