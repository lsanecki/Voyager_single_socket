from setting_view import SettingView


class ModelGui:
    def __init__(self, _path_file_settings):
        """
        Konstruktor klasy ModelGui
        """

        self.setting_view = None
        self.lab_dut_font_name = None
        self.lab_dut_font_size = None
        self.lab_large_font_name = None
        self.lab_large_font_size = None
        self.lab_medium_font_name = None
        self.lab_medium_font_size = None
        self.lab_small_font_name = None
        self.lab_small_font_size = None
        self.btn_font_name = None
        self.btn_font_size = None
        self.main_win_resolution = None
        self.load_setting_from_file(_path_file_settings)
        self.load_gui_parameters()

    def load_gui_parameters(self):
        """
        Wczytanie paramatrów gui
        :return:
        """

        self.load_win_size()
        self.set_btn_size()
        self.set_lab_size()

    def set_lab_size(self):
        """
        Wczytanie parametrów dla widget typu label
        :return:
        """

        self.lab_small_font_name, self.lab_small_font_size = self.load_widget_size('LabSmallFont')
        self.lab_medium_font_name, self.lab_medium_font_size = self.load_widget_size('LabMediumFont')
        self.lab_large_font_name, self.lab_large_font_size = self.load_widget_size('LabLargeFont')
        self.lab_dut_font_name, self.lab_dut_font_size = self.load_widget_size('LabDutFont')

    def load_widget_size(self, _name_widget):
        """
        Wczytanie paramatrów dla określonego widget'u
        :param _name_widget: Nazwa widget'u
        :type _name_widget: str
        :return: Zwraca nazwe czcionki i rozmiar w procentach do wysokości okna
        :rtype: tuple
        """

        _proc_height_widget = self.setting_view[_name_widget][1]
        _font_size = _proc_height_widget * 0.01 * self.main_win_resolution[1]
        _font_name = self.setting_view[_name_widget][0]
        return _font_name, _font_size

    def set_btn_size(self):
        """
        Wczytanie paramatrów dla widget typu button
        :return:
        """

        self.btn_font_name, self.btn_font_size = self.load_widget_size('BtnFont')

    def load_win_size(self):
        """
        Wczutuje rozmiar okna
        :return:
        """

        self.main_win_resolution = [self.setting_view['MainWinResolution'][0],
                                    self.setting_view['MainWinResolution'][1]]

    @classmethod
    def load_dut_font_size(cls, _count_dut):
        # dla 13-16 gniazd _proc_lab_dut = 2
        # dla 9-12 gniazd _proc_lab_dut = 3
        # dla 5-8 gniazd _proc_lab_dut = 4
        # dla 1-4 gniazd _proc_lab_dut = 5
        if _count_dut > 12:
            return 2
        elif 8 < _count_dut <= 12:
            return 3
        elif 4 < _count_dut <= 8:
            return 4
        elif 0 < _count_dut <= 4:
            return 5
        else:
            return 2

    def load_setting_from_file(self, _path_file_settings):
        """
        Wczytuje parametry z pliku
        :param _path_file_settings: Lokalizacja pliku
        :type _path_file_settings: str
        :return:
        """

        self.setting_view = SettingView.load_file(_path_file_settings)
