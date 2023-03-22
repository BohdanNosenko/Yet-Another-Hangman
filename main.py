import random

words = [
    'substitution',
    'insomnia',
    'bulldozer'
]


class Game:

    def __init__(self, word, cword):
        self.lives = 5
        self.word = list(word)
        self.cword = list(cword)

    def play(self) -> None:
        while let := input("Please pick a letter: "):
            if list(let) == self.word:
                print('Winner!')
                break
            if let in self.word:
                for _ in range(len(self.word)):
                    if self.word[_] == let:
                        self.cword[_] = self.word[_]
                print(''.join(self.cword))
                if '_' not in self.cword:
                    print('Winner!')
                    break
            else:
                if not self.life_counter():
                    break

    def life_counter(self) -> bool:
        if self.lives == 1:
            print('Looser >:(')
            return False
        else:
            self.lives -= 1
            print(f'Your have {self.lives} lives left.')
            return True


def word_picker(libre: list) -> str:
    return random.choice(libre)


def word_encryptor(word: str) -> str:
    cword = ''.join(['_' for _ in range(len(word))])
    print(cword)
    return cword


a = word_picker(words)
b = word_encryptor(a)

game = Game(a, b)

game.play()