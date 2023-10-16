import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QColor

app = QApplication(sys.argv)
window = QMainWindow()

# Personaliza el color de fondo de la barra de título
palette = QPalette()
palette.setColor(QPalette.Window, QColor(0, 0, 255))  # Cambia a azul
window.setPalette(palette)

window.setWindowTitle('Ventana personalizada')
window.show()

sys.exit(app.exec_())
