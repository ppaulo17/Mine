import unittest
import RPS_game
import RPS

class UnitTests(unittest.TestCase):
    def test_player_vs_quincy(self):
        print("Testing game against Quincy...")
        actual = RPS_game.play(RPS.player, RPS_game.quincy, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat Quincy at least 60% of the time.')

    def test_player_vs_abbey(self):
        print("Testing game against Abbey...")
        actual = RPS_game.play(RPS.player, RPS_game.abbey, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat Abbey at least 60% of the time.')

    def test_player_vs_kris(self):
        print("Testing game against Kris...")
        actual = RPS_game.play(RPS.player, RPS_game.kris, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat Kris at least 60% of the time.')

    def test_player_vs_mrugesh(self):
        print("Testing game against Mrugesh...")
        actual = RPS_game.play(RPS.player, RPS_game.mrugesh, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat Mrugesh at least 60% of the time.')

def run_test():
    unittest.main(argv=['first-arg-is-ignored'], exit=False)