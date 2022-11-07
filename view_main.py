# from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QFrame, QLabel, QProgressBar, QLCDNumber
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt


class GuiWidget(object):
    """Interefejs gui"""

    def __init__(self):

        # stopka
        self.btn_test_details = None
        self.icon_status_device = None
        self.btn_close_program = None
        self.btn_print = None
        self.lab_counter_nok = None
        self.lab_counter_ok = None
        self.layout_counter = None
        self.lab_status_device = None
        self.layout_status_device = None
        self.layout_footer_menu = None
        self.frame_footer = None

        # dut test
        self.socket_dut = {}
        self.p_bar_test = None
        self.layout_win = None
        self.layout_dut = None
        self.frame_dut = None
        self.layout_test = None
        self.frame_test = None

        # nagłówek
        self.lab_tester_message = None
        self.layout_header = None
        self.btn_settings = None
        self.btn_change_project = None
        self.lab_select_project = None
        self.layout_project_menu = None
        self.frame_header = None

    def setup_ui(self, widget):
        """Tworzy główne okno"""
        widget.setObjectName("Widget")
        self.layout_win = QVBoxLayout(self)
        self.insert_header()
        self.insert_test_frame()
        self.insert_footer()

    def insert_header(self):
        """ Wstawia nagłówek wraz z elementami do głównego okna"""
        self.frame_header = QFrame()
        self.layout_header = QVBoxLayout(self.frame_header)
        self.layout_project_menu = QHBoxLayout()
        self.init_project_menu()
        self.layout_win.addWidget(self.frame_header, 2)

    def init_project_menu(self):
        """Wstawia elementy do pierwszego wiersza w nagłówku"""
        self.init_widget_lab_project()
        self.init_widget_lab_select_project()
        self.init_widget_btn_change_project()
        self.init_widget_btn_settings()
        self.layout_header.addLayout(self.layout_project_menu, 3)
        self.init_lab_tester_message()

    def init_widget_lab_project(self):
        """Wstawia etykiete statyczna 'Projekt:'"""
        _labProject = QLabel("Projekt: ")
        _labProject.adjustSize()
        self.layout_project_menu.addWidget(_labProject, 1)

    def init_widget_lab_select_project(self):
        """ Wstawia etykiete z nazwa wybranego projektu"""
        self.lab_select_project = QLabel("Wybrany project")
        self.lab_select_project.adjustSize()
        self.lab_select_project.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.layout_project_menu.addWidget(self.lab_select_project, 5)

    def init_widget_btn_change_project(self):
        """Wstawia przycisk do zmiany projektu"""
        self.btn_change_project = QPushButton("Zmien Projekt")
        self.btn_change_project.adjustSize()
        self.layout_project_menu.addWidget(self.btn_change_project, 2)

    def init_widget_btn_settings(self):
        """Wstawia przucisk do zmiany ustawien projektu"""
        self.btn_settings = QPushButton("Ustawienia")
        self.btn_settings.adjustSize()
        self.layout_project_menu.addWidget(self.btn_settings, 2)

    def init_lab_tester_message(self):
        """Wstawia etykiete do komunikatow z testera"""
        self.lab_tester_message = QLabel("Komunikaty")
        self.lab_tester_message.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.lab_tester_message.adjustSize()
        self.layout_header.addWidget(self.lab_tester_message, 7)

    def insert_test_frame(self):
        """Wstawia ramke obslugi testu"""
        self.frame_test = QFrame()
        self.layout_test = QVBoxLayout(self.frame_test)
        self.init_frame_dut()
        self.init_progress_bar()
        self.layout_win.addWidget(self.frame_test, 6)

    def init_frame_dut(self):
        """Wstawia ramke z gniazdami dut"""
        self.frame_dut = QFrame()
        self.init_sockets()
        self.layout_test.addWidget(self.frame_dut)

    def init_sockets(self):
        """Tworzy layout dla wszystkich gniazd DUT"""
        self.layout_dut = QGridLayout(self.frame_dut)
        self.init_dut()
        self.layout_test.addLayout(self.layout_dut)

    def init_dut(self):
        """Wstawia wszystkie gniazda DUT"""

        self.init_test_sockets()

        """
        # przyklad odwolania do gniazd dut
        for i in range(16):
            self.socket_dut['dut' + str(i + 1)]['frame'].setStyleSheet("background-color: red")
            self.socket_dut['dut' + str(i + 1)]['status_dut'].setText("NOK")"""

    def check_count_dut(self):
        pass

    def init_test_sockets(self, _count_socket=16):
        """Generuje gniazda DUT w oknie programu

                :param _count_socket: Ilosc gniazd DUT.
                :type _count_socket: int
        """
        _dut_elements = {}
        _i = 0
        for y in range(4):
            for x in range(4):
                _i = _i + 1
                if not (_i <= _count_socket):
                    break
                self._create_dut(_i, x, y)

    def _create_dut(self, _i, x, y):
        """Tworzy gniazdo DUT i umieszcza je w głównej ramce programu oraz w słowniku z gniazdami

        :param _i: Numer gniazda DUT.
        :type _i: int
        :param x: Numer kolumny w której ma być umieszczone gniazdo DUT.
        :type x: int
        :param y: Numer wiersza w którym ma być umieszczone gniazdo DUT.
        :type y: int
        """
        _dut = {}
        _frame_dut = QFrame()
        _layout_dut = QVBoxLayout(_frame_dut)
        _name_dut = self._create_lab_dut_name(_i, _layout_dut)
        _sn_dut = self._create_lab_sn_dut(_layout_dut)
        _status_dut = self._create_lab_status_dut(_layout_dut)
        self._update_dut(_dut, _frame_dut, _layout_dut, _name_dut, _sn_dut, _status_dut)
        self.socket_dut.update({'dut' + str(_i): _dut})
        self.layout_dut.addWidget(_frame_dut, y, x)

    @classmethod
    def _update_dut(cls, _dut, _frame_dut, _layout_dut, _name_dut, _sn_dut, _status_dut):
        """Dodaje do słownika elementy danego gniazda DUT

        :param _dut: Słownik gniazda z elementami gniazda DUT.
        :type _dut: Dict
        :param _frame_dut: Ramka gniazda DUT
        :type _layout_dut: QFrame
        :param _layout_dut: Layout gniazda DUT.
        :type _layout_dut: QVBoxLayout
        :param _name_dut: Nazwa gniazda DUT.
        :type _name_dut: QLabel
        :param _sn_dut: Numer seryjny testowanego wyrobu w gniezdzie DUT.
        :type _sn_dut: QLabel
        :param _status_dut: Status testowanego wyrobu w gniezdzie DUT.
        :type _status_dut: QLabel

        """
        _dut.update({'frame': _frame_dut})
        _dut.update({'layout_dut': _layout_dut})
        _dut.update({'name_dut': _name_dut})
        _dut.update({'sn_dut': _sn_dut})
        _dut.update({'status_dut': _status_dut})

    @classmethod
    def _create_lab_status_dut(cls, _layout_dut):
        """Tworzy etykiete ze statusem testu dla testowanego wyrobu w  danym gniezdzie DUT

        :param _layout_dut: Layout gniazda dut.
        :type _layout_dut: QVBoxLayout

        :returns: _status_dut: Zwraca utworzoną etykiete ze statusem testu.
        :rtype: QLabel
        """
        _status_dut = QLabel("OK")
        _status_dut.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        _layout_dut.addWidget(_status_dut)
        return _status_dut

    @classmethod
    def _create_lab_sn_dut(cls, _layout_dut):
        """Tworzy etykiete z numerem seryjnym dla testowanego wyrobu w  danym gniezdzie DUT

        :param _layout_dut: Layout gniazda dut.
        :type _layout_dut: QVBoxLayout

        :returns: _sn_dut: Zwraca utworzoną etykiete numeru seryjnego.
        :rtype: QLabel
        """
        _sn_dut = QLabel("----------")
        _sn_dut.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        _layout_dut.addWidget(_sn_dut)
        return _sn_dut

    @classmethod
    def _create_lab_dut_name(cls, _i, _layout_dut):
        """Tworzy etykiete z nazwa gniazda DUT

        :param _i: Numer gniazda DUT.
        :type _i: int
        :param _layout_dut: Layout gniazda dut.
        :type _layout_dut: QVBoxLayout

        :returns: _name_dut: Zwraca utworzoną etykiete z nazwa gniazda.
        :rtype: QLabel
        """
        _name_dut = QLabel("Gniazdo " + str(_i))
        _name_dut.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        _layout_dut.addWidget(_name_dut)
        return _name_dut

    def init_progress_bar(self):
        """Wstawia progress bar"""
        self.p_bar_test = QProgressBar()
        self.layout_test.addWidget(self.p_bar_test)

    def insert_footer(self):
        """Wstawia stopke wraz elementami"""
        self.frame_footer = QFrame()
        self.layout_footer_menu = QHBoxLayout(self.frame_footer)
        self.init_widget_status_device()
        self.init_widget_counter()
        self.btn_test_details = QPushButton("Szczegóły testu")
        self.layout_footer_menu.addWidget(self.btn_test_details, 1)
        self.btn_print = QPushButton("Drukuj")
        self.layout_footer_menu.addWidget(self.btn_print, 1)
        self.btn_close_program = QPushButton("Zamknij")
        self.layout_footer_menu.addWidget(self.btn_close_program, 1)
        self.layout_win.addWidget(self.frame_footer, 2)

    def init_widget_status_device(self):
        """Wstawia etykiete ze statusem urzadzenia"""
        self.layout_status_device = QVBoxLayout()
        _labStatus = QLabel("Status:")
        # self.icon_status_device = QPixmap("image/check.png")
        # self.icon_status_device.scaled(64, 64)
        self.layout_status_device.addWidget(_labStatus)
        self.lab_status_device = QLabel("OK")
        # self.lab_status_device.setPixmap(self.icon_status_device)
        self.layout_status_device.addWidget(self.lab_status_device)
        self.layout_footer_menu.addLayout(self.layout_status_device, 1)

    def init_widget_counter(self):
        """Wstawia licznik wykonanych testów ok i nok"""
        self.layout_counter = QGridLayout()
        _lab_ok = QLabel("OK:")
        self.layout_counter.addWidget(_lab_ok, 0, 0)
        self.lab_counter_ok = QLCDNumber()
        self.layout_counter.addWidget(self.lab_counter_ok, 0, 1)
        _lab_nok = QLabel("NOK:")
        self.layout_counter.addWidget(_lab_nok, 1, 0)
        self.lab_counter_nok = QLCDNumber()
        self.lab_counter_nok.display('0')
        self.layout_counter.addWidget(self.lab_counter_nok, 1, 1)
        self.layout_footer_menu.addLayout(self.layout_counter, 2)


if __name__ == '__main__':
    pass
