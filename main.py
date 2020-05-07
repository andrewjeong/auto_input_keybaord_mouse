import pyautogui
import time

def wellformed_time():
    now = time.localtime()
    formed_time = ("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    return formed_time

print("Key list: %s", pyautogui.KEYBOARD_KEYS)

for idx in range(0, 6):
    # pyautogui.press('hangul')

    print("%s  index: %s" % (wellformed_time(), idx))
    pyautogui.press('pause')
    time.sleep(590)           # for 9 minutes 50 seconds

    print("%s  index: %s" % (wellformed_time(), idx))
    pyautogui.press('shiftright')
    time.sleep(590)           # for 9 minutes 50 seconds





