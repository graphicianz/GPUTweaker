import pynvml

def get_all_gpu_status():
    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()
    gpu_list = []

    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)

        name = pynvml.nvmlDeviceGetName(handle)
        if isinstance(name, bytes):
            name = name.decode("utf-8")

        temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
        gpu_usage = utilization.gpu

        memory = pynvml.nvmlDeviceGetMemoryInfo(handle)
        vram_used_MB = memory.used // 1024 // 1024
        vram_total_MB = memory.total // 1024 // 1024

        try:
            power_usage = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000.0
        except pynvml.NVMLError:
            power_usage = None

        try:
            fan_speed = pynvml.nvmlDeviceGetFanSpeed(handle)
        except pynvml.NVMLError:
            fan_speed = None

        try:
            graphics_clock = pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_GRAPHICS)
            memory_clock = pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_MEM)
        except pynvml.NVMLError:
            graphics_clock = None
            memory_clock = None

        gpu_list.append({
            'name': name,
            'temperature': temperature,
            'gpu_usage': gpu_usage,
            'vram_used_MB': vram_used_MB,
            'vram_total_MB': vram_total_MB,
            'power_usage': power_usage,
            'fan_speed': fan_speed,
            'graphics_clock': graphics_clock,
            'core_clock': graphics_clock,  # ✅ alias เพิ่มตรงนี้
            'memory_clock': memory_clock,
        })

    pynvml.nvmlShutdown()
    return gpu_list
