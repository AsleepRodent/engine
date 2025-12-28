from typing import Any

class Module:
    def __init__(self, **kwargs) -> None:
        self.parent: Any = kwargs.get("parent")
        self.enabled: bool = False

    def _start(self) -> None:
        pass

    def _stop(self) -> None:
        self.enabled = False

    def _update(self, dt: float) -> None:
        pass

    def _render(self) -> None:
        pass