import keyboard
import pyautogui

def test1():
    while keyboard.is_pressed('<'):
        pyautogui.click(button='middle')
        print("Pressed: <")

#def test1():
#    while keyboard.is_pressed('u') == False:
#        PressKey(51) # клавиша ,<
#        time.sleep(0.0001)
#        ReleaseKey(51)
#        print("Pressed: <")

#def test1():
#    isPressed = True
#    while isPressed:
#        PressKey(51) # клавиша ,<
#        time.sleep(0.0001)
#        ReleaseKey(51)
#        time.sleep(0.0001)
#        if keyboard.is_pressed('<'):
#            isPressed = False
#        print("Pressed: <")

def test2():
    while keyboard.is_pressed('>') == False:
        pyautogui.click(button='right')
        print("Pressed: >")

#def test2():
#    while keyboard.is_pressed('u') == False:
#        PressKey(52) # клавиша ,<
#        time.sleep(0.0001)
#        ReleaseKey(52)
#        print("Pressed: >")

#def test2():
#     isPressed = True
#     while isPressed:
#        PressKey(52) # клавиша ,<
#        time.sleep(0.0001)
#        ReleaseKey(52)
#        time.sleep(0.0001)
#        if keyboard.is_pressed('ctrl'):
#            break
#        print("Pressed: >")
 
if __name__ == '__main__':
    keyboard.add_hotkey('<',test1)
    keyboard.add_hotkey('>',test2)
    keyboard.wait()