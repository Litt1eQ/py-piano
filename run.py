import win32api
import win32con
import time
import ctypes

# 键位虚拟码表
kay_map = {
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'A': 0x41,
    'B': 0x42,
    'C': 0x43,
    'D': 0x44,
    'E': 0x45,
    'F': 0x46,
    'G': 0x47,
    'H': 0x48,
    'I': 0x49,
    'J': 0x4A,
    'K': 0x4B,
    'L': 0x4C,
    'M': 0x4D,
    'N': 0x4E,
    'O': 0x4F,
    'P': 0x50,
    'Q': 0x51,
    'R': 0x52,
    'S': 0x53,
    'T': 0x54,
    'U': 0x55,
    'V': 0x56,
    'W': 0x57,
    'X': 0x58,
    'Y': 0x59,
    'Z': 0x5A,
}


def keydown(num):
    """
    模拟按键函数
    :param num: 键位的虚拟码
    :return:
    """
    map_virtual_key = ctypes.windll.user32.MapVirtualKeyA
    time.sleep(0.4)
    win32api.keybd_event(num, map_virtual_key(num, 0), 0, 0)
    time.sleep(0.2)
    win32api.keybd_event(num, map_virtual_key(num, 0), win32con.KEYEVENTF_KEYUP, 0)


music_score = """
WQWE WQQ WQQHW WQWE WWQQWQQHHGG
TTEEEERERRRR WWEEWQQHQYYYTT
EEEE WWQWEWQQWE  WHQWQQWETTET
TTTY TERTYRR WWQEWQHWQWQQ 
TTTRYTREEEWW TTTEWWQWQWEE
JJWEWETEWQWH QQWEWETYTTEEEEW
YTTET YYTE TEW WWQEWQHWQQ 
"""

if __name__ == '__main__':
    # 这里延时原因: 因为程序从开始运行的时候就开始模拟按键了, 如果不设置延时, 前几个键位就浪费了
    time.sleep(3)
    for i in music_score:
        if i != '\n' and i != ' ':
            keydown(kay_map[i])
        else:
            time.sleep(0.5)
