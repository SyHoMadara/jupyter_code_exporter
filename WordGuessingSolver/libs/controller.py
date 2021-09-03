import types
import win32api
import threading
import pyautogui
import time


class NotMethod(BaseException):
    pass


msec = 10 ** (-3)


class BaseOnClickListener(threading.Thread):
    killed = False

    def __init__(self, call_back, button=None):
        # to check call_back be function
        if not isinstance(call_back, types.FunctionType):
            raise NotMethod(type(call_back).__name__)
        if not button:
            raise ValueError("button arg can't be null")
        self.call_back = call_back
        self.button = button
        super().__init__()

    def kill(self):
        self.killed = True

    # most implement
    def run(self):
        raise NotImplemented


"""
    Button clicking detection thread
        When you start an object of this class it waite for you to press button you give as parameter than run
    call_back function, it's necessary at object creation of class
        Remember if you want detect more than one click, after each detection use time.sleep or any method like
    sleep because it get more than click, that's why computer is so fast.
    recommended time gape between each is 60-70 millisecond. 
    For using time.sleep after import time package you can use time.sleep( 60 * 0.0001).
    
        Implementing run method necessary if you want use BaseOnClick class. While implementing run method you can use 
    killed value in infinity loops because kill method change killed value to false. 
    
    :param button, call_back:
"""


class Mouse:
    # buttons
    left_btn = 0x01
    right_btn = 0x02

    class OnClickListenerListener(BaseOnClickListener):

        def run(self):
            while True and not self.killed:
                # when clicked also holding
                button_status = win32api.GetKeyState(self.button)
                if button_status < 0:
                    x, y = pyautogui.position()
                    self.call_back(x, y)
                    break


class Keyboard:
    # buttons
    o_btn = 0x4F
    f_btn = 0x46

    class OnClickListenerListener(BaseOnClickListener):

        def run(self):
            while True and not self.killed:
                # when clicked also holding
                button_status = win32api.GetKeyState(self.button)
                if button_status < 0:
                    self.call_back()
