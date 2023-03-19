import tkinter as tk
import pyautogui
import os
import datetime
import time
import pytesseract
from PIL import Image

NUMBER_IMAGE_WIDTH = 120
NUMBER_IMAGE_HEIGHT = 30
ITEM_IMAGE_WIDTH = 110
ITEM_IMAGE_HEIGHT = 170
GAME_WIDTH = 2560
GAME_HEIGHT = 1600


def create_window():
    # 创建窗口
    window = tk.Tk()
    window.title("神之眼")
    # 窗口定位到屏幕中间位置
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width - 500) / 2)
    y = int((screen_height - 400) / 2)
    window.geometry("500x400+{}+{}".format(x, y))

    screenshot_btn = tk.Button(window, text="截图", command=screenshot)
    screenshot_btn.place(relx=0.5, rely=0.5, anchor="center")

    recognize_btn = tk.Button(window, text="识别", command=recognize)
    recognize_btn.place(relx=0.7, rely=0.5, anchor="center")

    # 进入消息循环
    window.mainloop()


def screenshot():
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads/vision")
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    # 指定坐标位置
    location = get_game_location()
    if location is None:
        return
    x = location[0]
    y = location[1]
    # 定时执行截图操作，每2秒执行一次，共执行5次
    for i in range(1):
        screenshot_pic = pyautogui.screenshot(
            region=(x, y, GAME_WIDTH, GAME_HEIGHT))
        screenshot_pic.save(os.path.join(
            download_folder, f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"))
        time.sleep(2)

    print("操作成功")


def get_game_location():
    icon = "images/game_icon.png"
    box = pyautogui.locateOnScreen(icon, confidence=0.8)
    if box is None:
        pyautogui.alert(title="提示", text="未找到游戏")
        return None
    return (box.left, box.top)


def crop(img, loc):
    im = Image.open(img)
    x = loc.left
    y = loc.top + ITEM_IMAGE_HEIGHT + 5
    box = (x, y, x + NUMBER_IMAGE_WIDTH, y + NUMBER_IMAGE_HEIGHT)
    print(box)
    return im.crop(box)


def recognize():
    # 提供两张图片，一个大图一个小图，通过识别算法，查找小图在大图的坐标
    big_image = "C:\\Users\\tianyl\\Downloads\\vision\\20230318213403.png"
    # small_image = "C:\\Users\\tianyl\\Downloads\\vision\\target_2.png"
    small_images = ["0001", "0002", "0003", "0004"]
    for img in small_images:
        small_image = f"images/{img}.png"
        location = pyautogui.locate(small_image, big_image, confidence=0.8)
        if location is None:
            print("查找失败")
            return
        # print(location)
        number_img = crop(big_image, location)
        number_img.show()
        # number_img.show()
        number = pytesseract.image_to_string(
            number_img, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        print(f"{img}:{number}")
    print("操作成功")


create_window()
