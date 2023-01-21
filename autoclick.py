import pyautogui
import time
from datetime import datetime
import winsound


def annoy():
    for i in range(1, 10):
        winsound.Beep(i * 100, 200)


print('鍾弘浩天堂點擊器')
winsound.Beep(1000, 500)
n = 0

try:
    while True:
        button_position = pyautogui.locateCenterOnScreen('get.jpg', confidence=0.8)
        now = datetime.now()

        if button_position is None:
            print(now.strftime("%H:%M:%S"), f'已經拿到 {n} 個寶箱, 正在等待下一個寶箱......')

        else:
            pyautogui.click(button_position)
            annoy()
            time.sleep(3)
            pyautogui.screenshot(f'{now.strftime("%H點%M分%S秒")}取得的寶箱.jpg')
            pyautogui.click(button_position)
            n += 1

        time.sleep(300)

except KeyboardInterrupt:
    print('Program end')
