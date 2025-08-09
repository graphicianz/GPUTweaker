from PySide2.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSlider, QFrame,
    QTabWidget, QHBoxLayout
)
from PySide2.QtCore import Qt
from monitor import get_all_gpu_status


class GPUTweakerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SOC")
        self.setMinimumWidth(400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.status_label = QLabel("GPU Status")
        self.status_label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.status_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.status_label.setWordWrap(True)
        self.layout.addWidget(self.status_label)

        # Sliders (Mock) — excluding Fan Speed
        self.sliders = {}
        slider_labels = [
            ["Clock Core (MHz)", [0,-500,1000]],
            ["Clock Mem (MHz)",[0,-1000,2000]],
            ["Voltage Core (mV)",[0, 0,100]],
            ["Power Limit (%)",[100,46,140]],
            ["Temperature Limit (C)",[70, 65, 90]],
            ["Fan Speed Limit (%)", [30,0,100]]
        ]
        for data in slider_labels:
            self.add_slider(data[0], data[1])

        # Fan Speed Tabs
        self.add_fan_speed_tabs()

        # Refresh button
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh_status)
        self.layout.addWidget(self.refresh_button)

        self.refresh_status()

    def add_slider(self, label_text, values):
        label = QLabel(label_text)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(values[1])
        slider.setMaximum(values[2])
        slider.setValue(values[0])
        value_label = QLabel( f"{ ('+' if values[0] > 0 else '') +str(values[0])}")

        slider.valueChanged.connect(lambda val, lbl=value_label: lbl.setText(f"{ ('+' if val > 0 else '') +str(val)}"))

        self.layout.addWidget(label)
        self.layout.addWidget(slider)
        self.layout.addWidget(value_label)

        self.sliders[label_text] = slider

    def add_fan_speed_tabs(self):
        tab_widget = QTabWidget()

        # Manual tab
        manual_tab = QWidget()
        manual_layout = QVBoxLayout()
        manual_tab.setLayout(manual_layout)

        label = QLabel("Manual Fan Speed (%)")
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        value_label = QLabel("50%")
        slider.valueChanged.connect(lambda val: value_label.setText(f"{val}%"))

        manual_layout.addWidget(label)
        manual_layout.addWidget(slider)
        manual_layout.addWidget(value_label)

        # Fan Curve tab (Placeholder)
        # curve_tab = QWidget()
        # curve_layout = QVBoxLayout()
        # curve_tab.setLayout(curve_layout)
        # curve_layout.addWidget(QLabel("Fan Curve settings (coming soon...)"))
        #
        # # Add tabs
        # tab_widget.addTab(manual_tab, "Manual")
        # tab_widget.addTab(curve_tab, "Fan Curve")
        # self.layout.addWidget(QLabel("Fan Speed"))
        # self.layout.addWidget(tab_widget)

    def refresh_status(self):
        gpu_status = get_all_gpu_status()
        if not gpu_status:
            self.status_label.setText("No GPU detected.")
            return

        gpu = gpu_status[0]
        text = (
            f"Name: {gpu['name']}\n"
            f"Temperature: {gpu['temperature']} ℃\n"
            f"GPU Usage: {gpu['gpu_usage']} %\n"
            f"VRAM Used: {gpu['vram_used_MB']} / {gpu['vram_total_MB']} MB\n"
            f"Core Clock: {gpu['graphics_clock']} MHz\n"
            f"Memory Clock: {gpu['memory_clock']} MHz\n"
            f"Power Usage: {gpu['power_usage']} W\n"
            f"Fan Speed: {gpu['fan_speed']} %"
        )
        self.status_label.setText(text)


def run_gui():
    app = QApplication([])
    window = GPUTweakerGUI()
    window.show()
    app.exec_()
