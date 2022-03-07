from talon import Module, ctrl
import time, multiprocessing, subprocess
from talon import ctrl

mod = Module()

global automouse_process
automouse_process=None

@mod.action_class
class Actions:
    def click_pause(interval:float=.020):
        """Click with pause in betw:een. for repeated clicks"""
        ctrl.mouse_click(button=0)
        time.sleep(interval)
        
    def start_clickonstop(interval:float=1):
        """Start auto mouse"""
        global automouse_process
        print("tommy test" + str(automouse_process))
        if automouse_process:        
            try:
                automouse_process.terminate()
                automouse_process.wait()
                automouse_process=None
            except Exception as e:
                print(e)
        else:
#             automouse_process = subprocess.run("python user/automouse/clickOnStop.py", shell=True)
            automouse_process = subprocess.Popen(["python", "user/automouse/clickOnStop.py"] )
        # automouse_process = multiprocessing.Process(target=click_on_stop, args=())
        # automouse_process.start()

def click_on_stop(interval_sec=.11, cooldown_sec=.3, hold_ms=0):
    global mouse_position_last, is_mouse_moving, pmouse_position_last
    pmouse_position_last = ctrl.mouse_pos()
    is_mouse_moving = False
    while(True):
        delta=distance(mouse.position, mouse_position_last)
        if is_mouse_moving:
			# E.g. if the mouse is moved programmatically
            sudden_jump = (delta > 50)
            if delta==0 and not sudden_jump:
                slow_click()
                is_mouse_moving = False
                time.sleep(cooldown_sec)
        else:
            if delta>0:
                is_mouse_moving = True
                time.sleep(cooldown_sec)

        mouse_position_last = ctrl.mouse_pos()
        time.sleep(interval_sec)

def distance(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**.5

def slow_click():
    ctrl.mouse_click(button=0, down=True)
    time.sleep(.016)
    ctrl.mouse_click(button=0, up=True)