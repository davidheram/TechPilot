import sys 
from PyQt6.QtWidgets import QApplication
from ui.ventana import VentanaTechPilot


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaTechPilot()
    ventana.show()
    sys.exit(app.exec())
