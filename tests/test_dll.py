import ctypes

dll_path = r"N:\VersionControl\CPP\MyFirstDLL\x64\Debug\MyFirstDLL.dll"
gpu = ctypes.CDLL(dll_path)

gpu.get_gpu_temp.argtypes = [ctypes.c_int]
gpu.get_gpu_temp.restype = ctypes.c_int

gpu.get_gpu_fan_speed.argtypes = [ctypes.c_int]
gpu.get_gpu_fan_speed.restype = ctypes.c_int

gpu.get_gpu_power_usage.argtypes = [ctypes.c_int]
gpu.get_gpu_power_usage.restype = ctypes.c_int

gpu.get_gpu_utilization.argtypes = [ctypes.c_int]
gpu.get_gpu_utilization.restype = ctypes.c_int

gpu.get_gpu_mem_info.argtypes = [
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_ulonglong),
    ctypes.POINTER(ctypes.c_ulonglong)
]
gpu.get_gpu_mem_info.restype = ctypes.c_int

gpu.get_gpu_core_clock.argtypes = [ctypes.c_int]
gpu.get_gpu_core_clock.restype = ctypes.c_int

gpu.get_gpu_mem_clock.argtypes = [ctypes.c_int]
gpu.get_gpu_mem_clock.restype = ctypes.c_int

idx = 0
total = ctypes.c_ulonglong()
used = ctypes.c_ulonglong()

print("Temp:", gpu.get_gpu_temp(idx), "°C")
print("Fan:", gpu.get_gpu_fan_speed(idx), "%")
print("Power:", gpu.get_gpu_power_usage(idx), "W")
print("Util:", gpu.get_gpu_utilization(idx), "%")

gpu.get_gpu_mem_info(idx, ctypes.byref(total), ctypes.byref(used))
print(f"Memory: {used.value/1024**2:.0f}/{total.value/1024**2:.0f} MB")

print("Core Clock:", gpu.get_gpu_core_clock(idx), "MHz")
print("Memory Clock:", gpu.get_gpu_mem_clock(idx), "MHz")
