# GPUTweaker

**GPUTweaker** is a lightweight Python application that provides a graphical interface for monitoring GPU status and adjusting key performance parameters.  
It is built with **PySide2** for the GUI and uses **pynvml** to gather real-time GPU metrics.

## Features

- **Real-time GPU Monitoring**  
  Displays:
  - GPU name
  - Temperature
  - GPU usage (%)
  - VRAM usage (MB)
  - Core clock (MHz)
  - Memory clock (MHz)
  - Power usage (W)
  - Fan speed (%)

- **Interactive Controls (Sliders)**  
  Adjustable parameters include:
  - Clock Core (MHz)
  - Clock Memory (MHz)
  - Core Voltage (mV)
  - Power Limit (%)
  - Temperature Limit (°C)
  - Fan Speed Limit (%)

- **Fan Speed Tabs**  
  - Manual fan speed adjustment (future support for custom fan curve)

- **Utility Buttons**  
  - **Reset**: Restores all sliders to their default values  
  - **Refresh**: Updates the displayed GPU status  
