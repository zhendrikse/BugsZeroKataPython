import unittest
from approvaltests.approvals import verify
from game import Game
from game_runner import GameRunner
from subprocess import run

class GameTest(unittest.TestCase):
    def test_trivia_game(self):
        # NOT WORKING YET!!!!!!!           
        output = run("ls", capture_output=True).stdout
        verify(output)

if __name__ == "__main__":
    unittest.main()

