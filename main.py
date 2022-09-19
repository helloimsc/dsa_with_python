import importlib
import sys

if __name__ == "__main__":
    module = importlib.import_module(sys.argv[1])
    func = getattr(module, sys.argv[2])
    func()
