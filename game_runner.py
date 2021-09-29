from random import randrange
from game import Game


class GameRunner:
    def __init__(self):
        self.not_a_winner = False

    @staticmethod
    def main():
        game = GameRunner()
        game.play_game(randrange(5) + 1)

    def play_game(self, rand:int) -> None:
        game = Game()

        game.add('Chet')
        game.add('Pat')
        game.add('Sue')

        while True:
            game.roll(rand)

            if randrange(9) == 7:
                self.not_a_winner = game.wrong_answer()
            else:
                self.not_a_winner = game.was_correctly_answered()

            if not self.not_a_winner:
                break


if __name__ == '__main__':
    GameRunner.main()
