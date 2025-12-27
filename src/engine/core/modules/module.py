from typing import Any

class Module:
    def __init__(self, **kwargs) -> None:
        self.parent: Any = kwargs.get("parent")