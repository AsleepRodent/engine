from typing import Any
import pyray as pr
from ..module import Module

class Loop(Module):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.queue: list[list[Any]] = [[], [], [], [], [], []]

    def add(self, module: Module, layer: int) -> None:
        if 0 <= layer < len(self.queue):
            if module not in self.queue[layer]:
                self.queue[layer].append(module)

    def _start(self) -> None:
        self.enabled = True
        renderer = self.parent.modules.get("Renderer")
        
        for layer in self.queue:
            for module in layer:
                if module is not renderer and hasattr(module, "_start"):
                    module._start()

        self.parent.on_start()

        while self.enabled and not pr.window_should_close():
            dt: float = pr.get_frame_time()

            for layer in self.queue:
                for module in layer:
                    if hasattr(module, "_update"):
                        module._update(dt)
            
            if renderer:
                renderer._render()

            self.parent.on_update(dt)
        
        self._stop()
