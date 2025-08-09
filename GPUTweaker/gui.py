from PySide2.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSlider, QFrame,
    QTabWidget, QHBoxLayout
)
from PySide2.QtCore import Qt
from .monitor import get_all_gpu_status


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

        self.sliders = {}  # {label: {"widget": QSlider, "default": int}}
        slider_labels = [
            ["Clock Core (MHz)", [0, -500, 1000]],
            ["Clock Mem (MHz)", [0, -1000, 2000]],
            ["Voltage Core (mV)", [0, 0, 100]],
            ["Power Limit (%)", [100, 46, 140]],
            ["Temperature Limit (C)", [70, 65, 90]],
            ["Fan Speed Limit (%)", [30, 0, 100]]
        ]
        for label, values in slider_labels:
            slider = self.add_slider(label, values)
            self.sliders[label] = {"widget": slider, "default": values[0]}

        # Fan Speed Tabs
        self.add_fan_speed_tabs()

        # Reset & Refresh buttons in one row (half–half width)
        button_layout = QHBoxLayout()

        self.default_button = QPushButton("Default")
        self.default_button.clicked.connect(self.reset_status)
        button_layout.addWidget(self.default_button, stretch=1)

        self.apply_button = QPushButton("Apply")
        self.apply_button.clicked.connect(self.refresh_status)
        button_layout.addWidget(self.apply_button, stretch=1)

        self.layout.addLayout(button_layout)

        # Initial refresh
        self.refresh_status()

    def add_slider(self, label_text, values):
        label = QLabel(label_text)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(values[1])
        slider.setMaximum(values[2])
        slider.setValue(values[0])

        value_label = QLabel(f"{('+' if values[0] > 0 else '')}{values[0]}")

        slider.valueChanged.connect(
            lambda val, lbl=value_label: lbl.setText(f"{('+' if val > 0 else '')}{val}")
        )

        self.layout.addWidget(label)
        self.layout.addWidget(slider)
        self.layout.addWidget(value_label)

        return slider

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

        # ถ้าจะเปิดใช้ Fan Curve ในอนาคต ค่อยเพิ่มแท็บใหม่ได้
        # tab_widget.addTab(manual_tab, "Manual")
        # self.layout.addWidget(QLabel("Fan Speed"))
        # self.layout.addWidget(tab_widget)

    def reset_status(self):
        # รีเซ็ตทุกสไลเดอร์กลับค่า default ที่กำหนดใน slider_labels
        for data in self.sliders.values():
            slider_widget = data["widget"]
            default_value = data["default"]
            slider_widget.setValue(default_value)

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
