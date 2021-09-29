from typing import List
from collections import deque

class Player:
  def __init__(self, name: str):
    self.name = name
    self.purse = 0
    self.rank = 0
    self.inPenaltyBox = False

  def add_coin(self) -> None:
    self.purse += 1

  def has_won(self) -> bool:
    return self.purse == 6

  def add_to_rank(self, amount:int) -> None:
    self.rank += amount
    if self.rank > 11:
        self.rank -= 12

  def __repr__(self):
    return self.name

class Game:
    def __init__(self, player1: Player, player2: Player, others:[Player] = []):
        self.players: List[Player] = []

        # https://realpython.com/linked-lists-python/
        self.popQuestions = deque()
        self.scienceQuestions = deque()
        self.sportsQuestions = deque()
        self.rockQuestions = deque()

        self.currentPlayer = 0
        self.isGettingOutOfPenaltyBox: bool = False

        for i in range(50):
            self.popQuestions.append("Pop Question " + str(i))
            self.scienceQuestions.append("Science Question " + str(i))
            self.sportsQuestions.append("Sports Question " + str(i))
            self.rockQuestions.append(self.createRockQuestion(i))
        
        self.add(player1)
        self.add(player2)
        for player in others:
          self.add(player)

    def createRockQuestion(self, index: int) -> str:
        return "Rock Question " + str(index)

    def add(self, player: Player) -> bool:
        self.players.append(player)
        print(repr(player) + " was added")
        print("They are player number " + str(len(self.players)))
        return True

    def howManyPlayers(self) -> int:
        return len(self.players)

    def roll(self, roll: int) -> None:
        print(repr(self.players[self.currentPlayer]) + " is the current player")
        print("They have rolled a " + str(roll))

        if self.players[self.currentPlayer].inPenaltyBox:
            if roll % 2 != 0:
                self.isGettingOutOfPenaltyBox = True
                print(
                    repr(self.players[self.currentPlayer]) +
                    " is getting out of the penalty box")
                self.movePlayerAndAskQuestion(roll)
            else:
                print(
                    repr(self.players[self.currentPlayer]) +
                    " is not getting out of the penalty box")
                self.isGettingOutOfPenaltyBox = False
        else:
            self.movePlayerAndAskQuestion(roll)

    def movePlayerAndAskQuestion(self, roll: int) -> None:
        self.players[self.currentPlayer].add_to_rank(roll)

        print(repr(self.players[self.currentPlayer]) + "'s new location is " +
            str(self.players[self.currentPlayer].rank))
        print("The category is " + self.currentCategory())
        self.askQuestion()

    def askQuestion(self) -> None:
        if self.currentCategory() == "Pop":
            print(self.popQuestions.popleft())
        if self.currentCategory() == "Science":
            print(self.scienceQuestions.popleft())
        if self.currentCategory() == "Sports":
            print(self.sportsQuestions.popleft())
        if self.currentCategory() == "Rock":
            print(self.rockQuestions.popleft())

    def currentCategory(self) -> str:
        if self.players[self.currentPlayer].rank == 0: return "Pop"
        if self.players[self.currentPlayer].rank == 4: return "Pop"
        if self.players[self.currentPlayer].rank == 8: return "Pop"
        if self.players[self.currentPlayer].rank == 1: return "Science"
        if self.players[self.currentPlayer].rank == 5: return "Science"
        if self.players[self.currentPlayer].rank == 9: return "Science"
        if self.players[self.currentPlayer].rank == 2: return "Sports"
        if self.players[self.currentPlayer].rank == 6: return "Sports"
        if self.players[self.currentPlayer].rank == 10: return "Sports"
        return "Rock"

    def was_correctly_answered(self) -> bool:
        if self.players[self.currentPlayer].inPenaltyBox:
            if self.isGettingOutOfPenaltyBox:
                print("Answer was correct!!!!")
                self.currentPlayer += 1
                if self.currentPlayer == len(self.players):
                    self.currentPlayer = 0
                self.players[self.currentPlayer].add_coin()
                print(
                    repr(self.players[self.currentPlayer]) + " now has " +
                    str(self.players[self.currentPlayer].purse) + " Gold Coins.")

                winner = self.didPlayerWin()

                return winner
            else:
                self.currentPlayer += 1
                if self.currentPlayer == len(self.players):
                    self.currentPlayer = 0
                return True
        else:
            print("Answer was corrent!!!!")
            self.players[self.currentPlayer].add_coin()
            print(
                repr(self.players[self.currentPlayer]) + " now has " +
                str(self.players[self.currentPlayer].purse) + " Gold Coins.")

            winner = self.didPlayerWin()
            self.currentPlayer += 1
            if self.currentPlayer == len(self.players):
                self.currentPlayer = 0

            return winner

    def wrong_answer(self) -> bool:
        print("Question was incorrectly answered")
        print(
            repr(self.players[self.currentPlayer]) +
            " was sent to the penalty box")
        self.players[self.currentPlayer].inPenaltyBox = True

        self.currentPlayer += 1
        if self.currentPlayer == len(self.players):
            self.currentPlayer = 0
        return True

    def didPlayerWin(self) -> bool:
        return not self.players[self.currentPlayer].has_won()
