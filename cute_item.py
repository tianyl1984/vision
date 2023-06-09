import tkinter as tk
import pyautogui
import os
import datetime
import time
import pytesseract
from PIL import Image
import util

ITEM_IMAGE_WIDTH = 110
ITEM_IMAGE_HEIGHT = 170
INCREASE_X = 195
INCREASE_Y = 235
START_X = 158
START_Y = 195
GAME_WIDTH = 2560
GAME_HEIGHT = 1600


def start():
    # 创建窗口
    window = tk.Tk()
    window.title("切图工具")
    # 窗口定位到屏幕中间位置
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width - 500) / 2)
    y = int((screen_height - 400) / 2)
    window.geometry("500x400+{}+{}".format(x, y))

    cute_btn = tk.Button(window, text="开始切图", command=cute)
    cute_btn.place(relx=0.5, rely=0.5, anchor="center")

    # 进入消息循环
    window.mainloop()


def cute():
    screenshot()
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads/vision")
    im = Image.open(download_folder + "/temp.png")
    x = 760
    y = 1300
    for i in range(8):
        for j in range(5):
            x = START_X + INCREASE_X * i
            y = START_Y + INCREASE_Y * j
            box = (x, y, x + ITEM_IMAGE_WIDTH, y + ITEM_IMAGE_HEIGHT)
            region = im.crop(box)
            region.save(os.path.join(download_folder, f"{i}_{j}.png"))
    pyautogui.alert(title="提示", text="完成")

def screenshot():
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads/vision")
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    # 指定坐标位置
    location = util.get_game_location()
    if location is None:
        return
    x = location[0]
    y = location[1]
    screenshot_pic = pyautogui.screenshot(
        region=(x, y, GAME_WIDTH, GAME_HEIGHT))
    screenshot_pic.save(os.path.join(download_folder, "temp.png"))
    print("截图生成成功")

start()
