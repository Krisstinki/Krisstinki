import time
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume_to_max():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    while True:
        volume.SetMasterVolumeLevelScalar(1.0, None)
        time.sleep(0.1)

if __name__ == "__main__":
    set_volume_to_max()
