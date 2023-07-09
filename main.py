import time

import eel
import keyboard
from time import sleep


if __name__ == '__main__':
    data_arr = []
    fl = ""
    eel.init('web')


    @eel.expose
    def my_func(plane1,plane2, start: int, stop: int, step: int):
        global data_arr
        data_arr.clear()
        sto_m = int(stop) + 1
        sta_m = int(start)
        ste_m = int(step)
        sleep(2)
        while (sta_m < sto_m):
            string = plane1 + str(sta_m) + plane2 +"\n"
            data_arr.append(string)
            sta_m += ste_m


    keyboard.add_hotkey('ctrl + alt + j', lambda: (time.sleep(2),[keyboard.write(string) for string in data_arr],keyboard.press_and_release('enter')))
    eel.start('interface.html', size=(780, 400))



