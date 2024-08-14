from PySide6.QtWidgets import QApplication
from widgets import Window
import sys

app = QApplication(sys.argv)

window = Window()
window.show()

app.exec()
