from PySide6.QtWidgets import QApplication, QMainWindow
from peek import peek as ic  # type: ignore

__version__ = "0.1.0"


class App(QApplication):
    def __init__(self):
        super().__init__()
        ic(f'UtilsHub v{__version__} is starting...')
        self.window = QMainWindow()
        self.window.show()
        
        
if __name__ == "__main__":
    app = App()
    app.exec()