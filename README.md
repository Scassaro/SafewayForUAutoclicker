Very rudimentary python autoclicker to click rapidly and handle error message popups.
Requirements: pyautogui, python 3. Install with pip3 install pyautogui.

Process:
10 second delay after running, clicks every 0.01 seconds and sends an escape command to handle error popups. Very short sleep after each cycle. Clicks for 40 seconds total.
Has a failsafe that is triggered by moving the mouse to the upper left corner of the screen.
