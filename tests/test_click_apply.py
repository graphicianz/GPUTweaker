import ctypes
import time

# Windows Virtual Key Codes
KEYEVENTF_KEYUP = 0x0002
VK_CONTROL = 0x11

# NumPad keys (ตามที่ตั้งใน MSI Afterburner)
VK_NUMPAD = {
    1: 0x61,  # NumPad1
    2: 0x62,  # NumPad2
    3: 0x63,
    4: 0x64,
    5: 0x65,
}

def apply_profile(profile_number):
    """
    Apply MSI Afterburner Profile using Ctrl + NumPad[1-5] hotkeys.
    Requires that the hotkeys are already set in Afterburner.
    """
    vk_key = VK_NUMPAD.get(profile_number)
    if not vk_key:
        raise ValueError("Profile number must be between 1 and 5")

    # Press Ctrl + NumPadX
    ctypes.windll.user32.keybd_event(VK_CONTROL, 0, 0, 0)
    ctypes.windll.user32.keybd_event(vk_key, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(vk_key, 0, KEYEVENTF_KEYUP, 0)
    ctypes.windll.user32.keybd_event(VK_CONTROL, 0, KEYEVENTF_KEYUP, 0)

    print(f"✅ Applied MSI Afterburner Profile {profile_number} via Ctrl + NumPad{profile_number}")
apply_profile(1)