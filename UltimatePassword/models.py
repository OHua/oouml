import logging
import random
from abc import abstractmethod
from enum import Enum


class GameFramework:
    def start(self):
        try:
            self._before_start()
        except Exception as e:
            print(f"game is close before start.")
        self._start()
        self._after_start()

    def _before_start(self):
        pass

    @abstractmethod
    def _start(self):
        raise NotImplementedError

    def _after_start(self):
        pass


class SinglePlayerMode:
    game_mode = "single"

    def __init__(self, player=None):
        self.player = player if self.check_player_valid(player) else User()

    @staticmethod
    def check_player_valid(player):
        return bool(player)


class MultiplePlayerMode:
    game_mode = "multiple"

    def __init__(self):
        self.players = []

    @staticmethod
    def check_player_valid(player):
        return bool(player)

    def add_player(self, player):
        if self.check_player_valid(player):
            self.players.append(player)
        else:
            logging.warning(f"{player} is not valid for this game mode")


class UltimatePasswordGame(GameFramework, MultiplePlayerMode):
    def __init__(self):
        super().__init__()
        self.final_code = random.randint(1, 100)
        self.guess_code = None
        self.guess_range = [1, 100]
        self.current_order = 0

    def _before_start(self):
        if len(self.players) == 0:
            print("there's no valid player in game, please add player")
            raise Exception

    def _start(self):
        while self.guess_code != self.final_code:
            self.update_range()
            player = self.players[self.current_order % len(self.players)]
            print(f"Hi {player.name}, now it's your turn!")
            self.guess_code = player.guess(self.guess_range)
            self.current_order += 1

        print(f"congratulations! {player.name}, you lose... ")

    def update_range(self):
        if not self.guess_code:
            return
        elif self.guess_range[0] < self.guess_code < self.final_code:
            self.guess_range[0] = self.guess_code
        elif self.final_code < self.guess_code < self.guess_range[1]:
            self.guess_range[1] = self.guess_code
        elif self.guess_code == self.final_code:
            return
        else:
            print(f"guess_code: {self.guess_code}")
            print(f"guess_range[0]: {self.guess_range[0]}")
            print(f"guess_range[1]: {self.guess_range[1]}")
            logging.error("get value error in update range func.")
            raise ValueError

    @staticmethod
    def check_player_valid(player):
        return hasattr(player, "guess")

    def render_player(self, player):
        def auto_guess(guess_range):
            return random.randint(guess_range[0], guess_range[1])

        def guess(guess_range):
            return int(input(f"please input a number between {self.guess_range[0]} and {self.guess_range[1]}: "))

        if not hasattr(player, "guess"):
            player.guess = guess
        return player


class PlayerType(Enum):
    user = 1
    computer = 2


class Player:
    name = "Player 1"
    type = PlayerType.user

    def __init__(self, name=None, player_type=None):
        self.name = name if name else self.__class__.name
        self.type = player_type if player_type else self.__class__.type


class Computer(Player):
    name = "Computer 1"
    type = PlayerType.computer

    def __init__(self, name=None):
        super().__init__(name, PlayerType.computer)


class OddComputer(Computer):
    name = "odd computer player"
    type = PlayerType.computer

    @staticmethod
    def guess(guess_range):
        start = guess_range[0] + 1 if guess_range[0] % 2 == 0 else guess_range[0] + 2
        guess_code = random.randrange(start, guess_range[1], 2)
        print(f"after calculate, I guess {guess_code}")
        return guess_code


class EvenComputer(Computer):
    name = "even computer player"
    type = PlayerType.computer

    @staticmethod
    def guess(guess_range):
        start = guess_range[0] + 1 if guess_range[0] % 2 == 1 else guess_range[0] + 2
        guess_code = random.randrange(start, guess_range[1], 2)
        print(f"after calculate, I guess {guess_code}")
        return guess_code
