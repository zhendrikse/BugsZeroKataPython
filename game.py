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

class Questions:
    def __init__(self):        
        # https://realpython.com/linked-lists-python/
        self.popQuestions = deque()
        self.scienceQuestions = deque()
        self.sportsQuestions = deque()
        self.rockQuestions = deque()
        for i in range(50):
          self.popQuestions.append("Pop Question " + str(i))
          self.scienceQuestions.append("Science Question " + str(i))
          self.sportsQuestions.append("Sports Question " + str(i))
          self.rockQuestions.append("Rock Question " + str(i))

    def currentCategory(self, index:int) -> str:
        rank_category_map = ["Pop", "Science", "Sports", "Rock", "Pop", "Science", "Sports", "Rock", "Pop", "Science", "Sports"]
        if index <= 10:
          return rank_category_map[index]
        else:
          return "Rock"
    
    def ask_question(self, index:int) -> str:
        if self.currentCategory(index) == "Pop":
            print(self.popQuestions.popleft())
        if self.currentCategory(index) == "Science":
            print(self.scienceQuestions.popleft())
        if self.currentCategory(index) == "Sports":
            print(self.sportsQuestions.popleft())
        if self.currentCategory(index) == "Rock":
            print(self.rockQuestions.popleft())

class Game:
    def __init__(self, player1: Player, player2: Player, others:[Player] = []):
        self.players: List[Player] = []
        self.questions = Questions()

        self.isGettingOutOfPenaltyBox: bool = False
        
        self.add(player1)
        self.add(player2)
        for player in others:
          self.add(player)

        self.currentPlayer = 0
        self.current_player = self.players[self.currentPlayer]

    def add(self, player: Player) -> bool:
        self.players.append(player)
        print(repr(player) + " was added")
        print("They are player number " + str(len(self.players)))
        return True

    def roll(self, roll: int) -> None:
        print(repr(self.current_player) + " is the current player")
        print("They have rolled a " + str(roll))

        if self.current_player.inPenaltyBox:
            if roll % 2 != 0:
                self.isGettingOutOfPenaltyBox = True
                print(
                    repr(self.current_player) +
                    " is getting out of the penalty box")
                self.movePlayerAndAskQuestion(roll)
            else:
                print(
                    repr(self.current_player) +
                    " is not getting out of the penalty box")
                self.isGettingOutOfPenaltyBox = False
        else:
            self.movePlayerAndAskQuestion(roll)

    def movePlayerAndAskQuestion(self, roll: int) -> None:
        self.current_player.add_to_rank(roll)

        print(repr(self.current_player) + "'s new location is " +
            str(self.current_player.rank))
        print("The category is " + self.questions.currentCategory(self.current_player.rank))
        self.questions.ask_question(self.current_player.rank)

    def next_player(self) -> None:
      self.currentPlayer += 1
      if self.currentPlayer == len(self.players):
          self.currentPlayer = 0
      self.current_player = self.players[self.currentPlayer]

    def was_correctly_answered(self) -> bool:
        if self.current_player.inPenaltyBox:
            if self.isGettingOutOfPenaltyBox:
                print("Answer was correct!!!!")

                self.next_player()

                self.current_player.add_coin()
                print(
                    repr(self.current_player) + " now has " +
                    str(self.current_player.purse) + " Gold Coins.")

                winner = self.didPlayerWin()

                return winner
            else:
                self.next_player()
                return True
        else:
            print("Answer was corrent!!!!")
            self.current_player.add_coin()
            print(
                repr(self.current_player) + " now has " +
                str(self.current_player.purse) + " Gold Coins.")

            winner = self.didPlayerWin()
            self.next_player()

            return winner

    def wrong_answer(self) -> bool:
        print("Question was incorrectly answered")
        print(
            repr(self.current_player) +
            " was sent to the penalty box")
        self.current_player.inPenaltyBox = True

        self.next_player()
        return True

    def didPlayerWin(self) -> bool:
        return not self.current_player.has_won()
