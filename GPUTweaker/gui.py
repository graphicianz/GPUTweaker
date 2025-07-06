from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from GPUTweaker.monitor import get_all_gpu_status
import sys

def run_gui():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("GPUTweaker")

    layout = QVBoxLayout()
    status_label = QLabel("Waiting for data...")

    def refresh():
        gpu_list = get_all_gpu_status()
        if not gpu_list:
            status_label.setText("No GPU detected.")
            return

        gpu = gpu_list[0]
        output = (
            f"GPU: {gpu['name']}\n"
            f"Temperature: {gpu['temperature']} °C\n"
            f"GPU Usage: {gpu['gpu_usage']} %\n"
            f"VRAM Used: {gpu['vram_used_MB']} / {gpu['vram_total_MB']} MB\n"
            f"Core Clock: {gpu['graphics_clock']} MHz\n"
            f"Memory Clock: {gpu['memory_clock']} MHz\n"
            f"Power Usage: {gpu['power_usage']} W\n"
            f"Fan Speed: {gpu['fan_speed']} %\n"
        )
        status_label.setText(output)

    refresh_btn = QPushButton("Refresh")
    refresh_btn.clicked.connect(refresh)

    layout.addWidget(status_label)
    layout.addWidget(refresh_btn)
    window.setLayout(layout)
    window.show()

    refresh()  # show data on startup
    sys.exit(app.exec_())
