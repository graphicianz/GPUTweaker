import ctypes

dll_path = r"N:\VersionControl\CPP\MyFirstDLL\x64\Debug\MyFirstDLL.dll"
gpu = ctypes.CDLL(dll_path)

gpu.set_gpu_fan_speed.argtypes = [ctypes.c_int, ctypes.c_int]
gpu.set_gpu_fan_speed.restype = ctypes.c_int

result = gpu.set_gpu_fan_speed(0, 70)  # set to 70%
if result == 0:
    print("✅ Fan speed set to 70% and applied via Afterburner")
else:
    print("❌ Failed to set fan speed, code:", result)
