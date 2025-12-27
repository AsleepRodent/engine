from typing import Any
from .modules.loader import Loader


class Game:
    def __init__(self, **kwargs) -> None:
        super.__init__(**kwargs)
        self.root: str = str(kwargs.get("root", "."))
        self.modules: dict[str, Any] = {
            "Loader": Loader(parent=self)
        }

    def start(self) -> None: pass
    def update(self, **kwargs) -> None: pass