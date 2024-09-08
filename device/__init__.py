from uiautomator2 import connect

def get_device(device_id='127.0.0.1:16416'):
    """Connect to the specified device."""
    return connect(device_id)


# d = get_device()
# if d:
#     print(f"连接到：{d}")
#     d.screenshot("../resources/screenshot.png")
#     print("截图成功")
# else:
#     print("连接失败")