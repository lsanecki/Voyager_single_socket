from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from view_main import GuiWidget
from model_main_win import ModelGui
import sys


class ControlGui(QWidget, GuiWidget):
    def __init__(self, _path_gui_parameter, parent=None):
        super(ControlGui, self).__init__(parent, )
        self.setup_ui(self)
        self.model_gui = ModelGui('settings/global.json')
        self.set_window_size()
        self.set_btn_size()
        self.set_lab_size()

    def set_window_size(self):
        """Ustawia rozmiar okna"""
        win_size = self.model_gui.main_win_resolution
        self.resize(int(win_size[0]), int(win_size[1]))

    def set_btn_size(self):
        self.btn_test_details.setFont(QFont(self.model_gui.btn_font_name, int(self.model_gui.btn_font_size)))
        self.btn_close_program.setFont(QFont(self.model_gui.btn_font_name, int(self.model_gui.btn_font_size)))
        self.btn_print.setFont(QFont(self.model_gui.btn_font_name, int(self.model_gui.btn_font_size)))
        self.btn_settings.setFont(QFont(self.model_gui.btn_font_name, int(self.model_gui.btn_font_size)))
        self.btn_change_project.setFont(QFont(self.model_gui.btn_font_name, int(self.model_gui.btn_font_size)))

    def set_lab_size(self):
        self.lab_counter_nok.setFont(QFont(self.model_gui.lab_small_font_name, int(self.model_gui.lab_small_font_size)))
        self.lab_counter_ok.setFont(QFont(self.model_gui.lab_small_font_name, int(self.model_gui.lab_small_font_size)))
        self.lab_status_device.setFont(
            QFont(self.model_gui.lab_small_font_name, int(self.model_gui.lab_small_font_size)))
        self.lab_tester_message.setFont(QFont(self.model_gui.lab_large_font_name,
                                              int(self.model_gui.lab_large_font_size)))
        self.lab_select_project.setFont(QFont(self.model_gui.lab_medium_font_name,
                                              int(self.model_gui.lab_medium_font_size)))
        print(len(self.socket_dut))

        for dut in self.socket_dut:
            # self.socket_dut[dut]['frame'].setStyleSheet("background-color: blue")
            self.socket_dut[dut]['status_dut'].setFont(QFont(self.model_gui.lab_dut_font_name,
                                                             int(self.model_gui.lab_dut_font_size)))
            self.socket_dut[dut]['sn_dut'].setFont(QFont(self.model_gui.lab_dut_font_name,
                                                         int(self.model_gui.lab_dut_font_size)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ControlGui("settings/global.json")
    window.show()
    sys.exit(app.exec_())
