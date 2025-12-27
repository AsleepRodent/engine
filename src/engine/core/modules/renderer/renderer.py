from ..module import Module

from .other.render import Render

class Renderer(Module):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.renders: dict[str, Render] = {}

    def _update(**kwargs) -> None:
        pass