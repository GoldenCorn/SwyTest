from modules.players import players
from modules.tasks import tasks
from modules.tasks import KeChaoTask
import modules.utils as utils
from modules.players import ADBPlayer
import time
import atexit

FPS = 2
player = None
def get_player():
    global player
    if player is not None:
        return
    for (name, desc, Player) in players():
        if Player is not None:
            player = Player
            print(f"{name}: {desc}，{Player}")
        else:
            print(f"模拟器连接失败")

def run(task):
    def onclicked(x, y, is_preview):
        task.clicked = (x, y)
        if is_preview:
            player.click(x, y)

    if player is None:
        get_player()
        if player is None:
            print("尚未连接至设备, 无法执行挂机任务")
            return
    print(f"开始运行挂机任务: {task.name}")
    utils.createpreview(onclicked)
    co = task.run(player)
    while True:
        t = time.perf_counter()
        task.frame = player.screenshot()
        try:
            co.send(None)
        except StopIteration:
            break
        utils.showpreview(task.frame)
        wait = 1 / FPS - (time.perf_counter() - t)
        if wait < 0:
            print(f"严重滞后, 处理时间超出 {-int(wait * 1000)} ms, 发生了什么呢?")
            wait = 0
        time.sleep(wait)
    utils.destroypreview()
    print("挂机任务运行完毕")

@atexit.register
def onexit():
    if player is not None:
        player.release()
    print("挂机脚本已退出")

if __name__ == '__main__':
    player = ADBPlayer()
    if player is None:
        get_player()
    
    task = KeChaoTask()
    run(task)