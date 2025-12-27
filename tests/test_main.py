import time
from utils import load

module = load("module")

def main():
  
  if module == None:
    return

  old_val = module.module_var

  print("empezando a observar el modulo", module.__name__)

  while True:
    time.sleep(0.1)
    new_val = module.module_var
    if not new_val == old_val:
      old_val = new_val
      print(new_val)

if __name__ == "__main__":
  main()