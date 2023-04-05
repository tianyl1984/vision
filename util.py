import pyautogui

def get_game_location():
    icon = "images/game_icon.png"
    box = pyautogui.locateOnScreen(icon, confidence=0.8)
    if box is None:
        pyautogui.alert(title="提示", text="未找到游戏")
        return None
    return (box.left, box.top)