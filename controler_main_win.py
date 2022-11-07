from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from view_main import GuiWidget
import sys


class ControlGui(QWidget, GuiWidget):
    def __init__(self, _path_gui_parameter, parent=None):
        super(ControlGui, self).__init__(parent, )
        self.setup_ui(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ControlGui("settings/global.json")
    window.show()
    sys.exit(app.exec_())
