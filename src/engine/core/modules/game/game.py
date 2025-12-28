from typing import Any

from ..module import Module
from ..loop.loop import Loop
from ..renderer.renderer import Renderer

class Game(Module):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.root: str = str(kwargs.get("root", "."))
        self.modules: dict[str, Any] = {
            "Loop": Loop(parent=self),
            "Renderer": Renderer(parent=self)
        } 

    def on_start(self) -> None: pass
    def on_update(self, dt: float) -> None: pass

    def start(self):
        self.enabled = True
        self.modules.get("Renderer")._start()
        self.modules.get("Loop")._start()

    def stop(self):
        self.enabled = False
        self.modules.get("Renderer")._stop()
        self.modules.get("Loop")._stop()
