import time, pynput
from pynput.mouse import Button

def clickLoop(s):
    while True:
        time.sleep(s)
        clickLeftMouse()
        
def main():
    clickOnStop()

def clickLeftMouse(holdMs=0):
    mouse.press(Button.left)
    time.sleep(holdMs)
    mouse.release(Button.left)
    
mouse = pynput.mouse.Controller()
mouse_position_last = mouse.position
is_mouse_moving = False
def clickOnStop(interval_sec=.11, cooldown_sec=.3, holdMs=0):
    global mouse_position_last, is_mouse_moving
    while(True):
        delta=distance(mouse.position, mouse_position_last)
        if is_mouse_moving:
			# E.g. if the mouse is moved programmatically
            sudden_jump = (delta > 50)
            if delta==0 and not sudden_jump:
                clickLeftMouse(holdMs=holdMs)
                is_mouse_moving = False
                time.sleep(cooldown_sec)
        else:
            if delta>0:
                is_mouse_moving = True
                time.sleep(cooldown_sec)

        mouse_position_last = mouse.position
        time.sleep(interval_sec)

def distance(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**.5

if __name__=="__main__":
    main()
