import time
import importlib
from pathlib import Path
from watchdog.observers import Observer # type: ignore
from watchdog.events import FileSystemEventHandler # type: ignore
from typing import Any 
from os import fsdecode

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, module_name, module):
        self.module_name = module_name
        self.module = module
        self.last_reload = 0

    def on_modified(self, event):
        now = time.time()
        if now - self.last_reload < 0.5:
            return  # ignora duplicados

        self.last_reload = now

        print(f"🔄 Cambio detectado en {self.module_name}. Recargando...")
        importlib.reload(self.module)

def load(path):
  if path is None:
      return None

  module = importlib.import_module(path)

  raw_path = getattr(module, "__file__", None)

  if raw_path is None:
      print(f"⚠️ El módulo {module.__name__} no tiene un archivo físico asociado.")
      return None

  file_path = Path(raw_path).resolve()

  handler = ReloadHandler(path, module)
  observer = Observer()
  observer.schedule(handler, str(file_path), recursive=False)
  observer.start()

  return module