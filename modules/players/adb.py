from ppadb.client import Client as ADBClient
from device import get_device
from PIL import Image
import numpy
import cv2
from .player import Player

class ADBPlayer(Player):
    """通过ADB控制手机"""
    client = None
    device = None

    def __init__(self):
        # os.system("adb start-server")
        #self.client = ADBClient(host="127.0.0.1", port=16416)
        devices = []
        try:
            print("正在检测设备...")
            #devices = self.client.devices()
            devices.append(get_device())
        except:
            print("无法连接至ADB Server, 请先启动ADB")
            raise
        size = len(devices)
        if size == 1:
            print(f"已自动选择设备: {devices[0].serial}")
            self.device = devices[0]
        elif size > 1:
            for i in range(size):
                print("{i + 1}. {devices[i].serial}")
            select = 0
            while select < 1 or select > size:
                select = int(input("请选择设备序号: "))
            self.device = devices[select - 1]
        else:
            print("未检测到设备, 请手动连接设备")
            raise Exception("No devices detected")
        print(f"已成功连接至设备 {self.device.serial}")
        self.height, self.width = self.device.window_size()
        print(f"已获得设备屏幕尺寸: {self.width} X {self.height}")
        super().__init__()

    def _screenshot(self):
        # 截取屏幕
        screen_pil = self.device.screenshot()

        screen_pil = screen_pil.convert('RGBA')

        image_uiauto = cv2.cvtColor(numpy.array(screen_pil), cv2.COLOR_RGBA2BGRA)
        return image_uiauto

    def _click(self, x, y):
        self.device.click(int(x), int(y))
