import pyautogui
import time

# Configure PyAutoGUI settings
pyautogui.FAILSAFE = True  # Move mouse to top-left corner to stop the script
pyautogui.PAUSE = 0.01  # Small pause between clicks to prevent system overload

# 5-second delay before starting
print("Starting in 5 seconds... Move mouse to top-left corner to cancel.")
time.sleep(10)

# Click for 20 seconds
start_time = time.time()
click_count = 0
duration = 40  # Duration in seconds

while time.time() - start_time < duration:
    pyautogui.click(button='left')
    pyautogui.press('esc')
    click_count += 1
    # Optional: Small delay to control click speed (adjust as needed)
    time.sleep(0.005)

print(f"Finished clicking. Total clicks: {click_count}")
