import ctypes
import time

def reverse_mouse():
    ctypes.windll.user32.SwapMouseButton(True)

def restore_mouse():
    ctypes.windll.user32.SwapMouseButton(False)

def change_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def main():
    try:
        reverse_mouse()
        image_path = r"C:\path\to\your\image.jpg"
        change_wallpaper(image_path)
        time.sleep(30)
    finally:
        restore_mouse()

if __name__ == "__main__":
    main()
