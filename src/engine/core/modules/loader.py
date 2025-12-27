import importlib
from pathlib import Path
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
from typing import Any
from time import time 
from os import fsdecode
from .module import Module

class Loader(Module, FileSystemEventHandler):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.registry: dict[str, Any] = {}
        self.last_reload: dict[str, float] = {}
        self.observer = Observer()
        self.observer.start()

    def on_modified(self, event):
        now = time()
        event_path = Path(fsdecode(event.src_path)).resolve()

        for path_name, module_obj in self.registry.items():
            module_file = getattr(module_obj, "__file__", None)
            if module_file and Path(module_file).resolve() == event_path:
                
                if now - self.last_reload.get(path_name, 0) < 0.5:
                    return

                self.last_reload[path_name] = now
                print(f"🔄 Cambio detectado en {path_name}. Recargando...")
                importlib.reload(module_obj)

    def Load(self, **kwargs) -> Any:
        path = kwargs.get("path")
        if path is None:
            return None

        module = importlib.import_module(path)
        raw_path = getattr(module, "__file__", None)

        if raw_path is None:
            return None

        file_path = Path(raw_path).resolve()
        folder_to_watch = file_path.parent

        self.registry[path] = module
        self.observer.schedule(self, str(folder_to_watch), recursive=False)
        
        return module

    def Unload(self, **kwargs) -> Any:
        path = kwargs.get("path")
        if path in self.registry:
            del self.registry[path]
            self.last_reload.pop(path, None)

    def _update(self, **kwargs):
        pass