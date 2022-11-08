
class ModelGui:
    def __init__(self):
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
        self.load_gui_parameters()

    def load_gui_parameters(self):
        self.main_win_resolution = [1280, 720]
        
        _proc_btn = 5
        self.btn_font_size = _proc_btn * 0.01 * self.main_win_resolution[1]
        self.btn_font_name = 'Arial'
        
        _proc_lab_small = 3
        self.lab_small_font_size = _proc_lab_small * 0.01 * self.main_win_resolution[1]
        self.lab_small_font_name = 'Arial'

        _proc_lab_medium = 5
        self.lab_medium_font_size = _proc_lab_medium * 0.01 * self.main_win_resolution[1]
        self.lab_medium_font_name = 'Arial'

        _proc_lab_large = 8
        self.lab_large_font_size = _proc_lab_large * 0.01 * self.main_win_resolution[1]
        self.lab_large_font_name = 'Arial'

        # dla 13-16 gniazd _proc_lab_dut = 2
        # dla 9-12 gniazd _proc_lab_dut = 3
        # dla 5-8 gniazd _proc_lab_dut = 4
        # dla 1-4 gniazd _proc_lab_dut = 5
        _proc_lab_dut = 5
        self.lab_dut_font_size = _proc_lab_dut * 0.01 * self.main_win_resolution[1]
        self.lab_dut_font_name = 'Arial'

    def load_dut_font_size(self, _count_dut):
        if _count_dut>12:
            return 2
        elif 8<_count_dut<=12:
            return 3
        elif 4<_count_dut<=8:
            return 4
        elif 0<_count_dut<=4:
            return 5
        else:
            return 2
        