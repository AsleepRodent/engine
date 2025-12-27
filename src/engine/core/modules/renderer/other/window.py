import pyray as pr

class Window:
    def __init__(self, **kwargs) -> None:
        self.width: int = int(kwargs.get("width", 800))
        self.height: int = int(kwargs.get("height", 600))
        self.title: str = str(kwargs.get("title", "Unknown"))
        self.enabled = False

    def open(self) -> None:
        if not self.enabled:
            pr.init_window(self.width, self.height, self.title)
            self.enabled = True

    def close(self) -> None:
        if self.enabled:
            pr.close_window()
            self.enabled = False

    