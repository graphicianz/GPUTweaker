import ctypes

dll_path = r"N:\VersionControl\CPP\MyFirstDLL\x64\Debug\MyFirstDLL.dll"
mydll = ctypes.CDLL(dll_path)

# เรียก add
mydll.add.argtypes = [ctypes.c_int, ctypes.c_int]
mydll.add.restype = ctypes.c_int
print(mydll.add(5, 7))  # 12

# เรียก get_hello
mydll.get_hello.restype = ctypes.c_char_p
print(mydll.get_hello().decode())

# เรียก square
mydll.square.argtypes = [ctypes.c_int]
mydll.square.restype = ctypes.c_int
print(mydll.square(9))  # 81
