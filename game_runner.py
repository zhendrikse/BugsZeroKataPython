from random import randint
from game import Game

class GameRunner:
  def __init__(self):
    self.notAWinner: bool

  @staticmethod
  def main() -> None:
    runner = GameRunner()
    runner.playGame(randint(0, 10))


  def playGame(self, rand: int) -> None:
    aGame = Game()

    aGame.add("Chet")
    aGame.add("Pat")
    aGame.add("Sue")

    while True:
      aGame.roll(randint(0, 5) + 1)

      if rand == 7:
        self.notAWinner = aGame.wrongAnswer()
      else: 
        self.notAWinner = aGame.wasCorrectlyAnswered()

      if not self.notAWinner:
        break


if __name__ == "__main__":
    GameRunner.main()