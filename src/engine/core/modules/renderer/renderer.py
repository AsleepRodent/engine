from typing import Any
import pyray as pr
from ..module import Module
from .other.window import Window

class Renderer(Module):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.window: Window = Window(**kwargs)

    def _start(self) -> None:
        if not self.enabled:
            loop = self.parent.modules.get("Loop")
            if loop:
                loop.add(self, 0)
            self.window.open()
            self.enabled = True

    def _render(self) -> None:
        if self.enabled:
            pr.begin_drawing()
            pr.clear_background(pr.RAYWHITE)
            loop = self.parent.modules.get("Loop")
            if loop:
                for layer in loop.queue:
                    for module in layer:
                        if module is not self and hasattr(module, "_render"):
                            module._render()
            pr.end_drawing()
