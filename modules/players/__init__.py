from .player import addplayer, players

try:
    from .adb import ADBPlayer
    addplayer("ADB模式", "请打开食物语并切换到客潮界面", ADBPlayer)
except ModuleNotFoundError as e:
    addplayer("ADB模式", e.name, None)