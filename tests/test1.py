import pyray as pr

from src.engine.core.modules.game.game import Game

class Test(Game):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def on_update(self, dt):
        if pr.is_key_pressed(pr.KeyboardKey.KEY_A):
            self.stop()

if __name__ == "__main__":
    test = Test()
    test.start()