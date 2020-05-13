import pyautogui
import sys
import time

def wellformed_time():
    now = time.localtime()
    formed_time = ("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    return formed_time

def countdown(max_num):
    for idx in reversed(range(0, max_num)):
        time.sleep(1 - time.time() % 1) # sleep until a whole second boundary
        sys.stdout.write('\r%5d seconds (%02d min %02d sec)' % (idx, idx/60, idx%60))
    sys.stdout.write('\n')

def total_remain_time(reamain_cnt, sleep_duration):
    total_sleep_duration = sleep_duration * max_index * 2
    sleep_hour = (int) (total_sleep_duration / 3600)
    sleep_min  = (int) ((total_sleep_duration - (sleep_hour * 3600)) / 60)
    sleep_sec  = total_sleep_duration % 60
    print("Total remain time: %02d:%02d:%02d" % (sleep_hour, sleep_min, sleep_sec)) 

# print("Key list: %s", pyautogui.KEYBOARD_KEYS)


max_index = 20
sleep_duration = 540
total_sleep_duration = sleep_duration * 2 * max_index

for idx in reversed(range(0, max_index)):
    total_remain_time(idx, sleep_duration)
    
    # pyautogui.press('hangul')
    print("%s  index: %s" % (wellformed_time(), idx), flush=True)
    # pyautogui.press('pause')
    pyautogui.press('shiftleft')
    countdown(sleep_duration)

    print("%s  index: %s" % (wellformed_time(), idx), flush=True)
    pyautogui.press('shiftright')
    countdown(sleep_duration)


print("All job is done")

# os.system("taskkill /f /im ttree.exe")

time.sleep(5)
import ctypes
ctypes.windll.user32.LockWorkStation()


