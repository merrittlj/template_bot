#!/usr/bin/env python3

# Global imports
import os, sys, time, pyautogui

# Local imports
from template_bot.util import hotkey_utils
from template_bot.util import logging_utils


launched = False
def main():
    bot_hotkey = hotkey_utils.Hotkey(key_combination = '<ctrl>+p', activated_func = bot_launch)
    bot_hotkey.run()

def bot_launch():
    global launched
    if launched:
        logging_utils.logpr("Bot already launched!")
        return
    launched = True
 
    for i in range(0, 5):
        logging_utils.logpr(f"Running MLB bot in {str(5 - i)} seconds.")
        time.sleep(1)

    while True:
        x, y = pyautogui.position()
        logging_utils.logpr(f"(x: {x}, y: {y}) {pyautogui.pixel(x, y)}")

if __name__ == "__main__":
    print("\n")
    main()
    print("\n")
else:
    logging_utils.logpr(f"Only use \"{os.path.basename(__file__)}\" as a script!")
    sys.exit()

