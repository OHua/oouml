from models import UltimatePasswordGame, Player, OddComputer, EvenComputer, Computer

if __name__ == '__main__':
    game = UltimatePasswordGame()

    game.add_player(game.render_player(Player("john")))
    game.add_player(game.render_player(Computer()))
    game.add_player(game.render_player(EvenComputer("peter")))
    game.add_player(game.render_player(OddComputer("julia")))

    game.start()
