import json
import os
import pyautogui
import keyboard
import time
import pydirectinput

configuration = {
    "upgrade_position": tuple(),
    "blacksmith_position": tuple(),
    "upgrade_target_position": tuple(),
    "buy_tools_position": tuple(),
    "buy_tools_target_position": tuple(),
    "buy_button_position": tuple(),
    "upgrade_button_position": tuple(),
    "upgrade_accept_button_position": tuple(),
    "close_upgrade_menu_position": tuple(),
    "blacksmith_leave_position": tuple(),
}

configuration_path = "configuration.json"

is_cancelled = False


def init_configuration():
    # check if the configuration exists
    if not os.path.exists(configuration_path):
        ask_for_configuration_values()
        if is_cancelled:
            return
    else:
        with open(configuration_path, "r") as f:
            global configuration
            configuration = json.load(f)


def get_cursor_position_when_hotkey_pressed():
    while True:
        # Get the mouse position
        mouse_position = pyautogui.position()
        if keyboard.is_pressed("f6"):
            print("Set position: " + str(mouse_position))
            time.sleep(0.5)
            return mouse_position
        elif keyboard.is_pressed("f8"):
            is_cancelled = True
            return None


def ask_for_configuration_values():
    print("Setting configuration values\n")
    print("Set the position for the upgrade area (F6 to set, F8 to cancel)")
    configuration["upgrade_position"] = get_cursor_position_when_hotkey_pressed()
    if is_cancelled:
        return
    print("Set the position for the item you want to upgrade (F6 to set, F8 to cancel)")
    configuration["upgrade_target_position"] = get_cursor_position_when_hotkey_pressed()
    if is_cancelled:
        return
    print("Set the position for the upgrade button (F6 to set, F8 to cancel)")
    configuration["upgrade_button_position"] = get_cursor_position_when_hotkey_pressed()
    if is_cancelled:
        return
    print("Set the position for the accept button (F6 to set, F8 to cancel)")
    configuration["upgrade_accept_button_position"] = get_cursor_position_when_hotkey_pressed()
    if is_cancelled:
        return
    print("Set the position for the close upgrade menu button (F6 to set, F8 to cancel)")
    configuration["close_upgrade_menu_position"] = get_cursor_position_when_hotkey_pressed()
    if is_cancelled:
        return
    print("Set the position for the blacksmith area (F6 to set, F8 to cancel)")
    configuration["blacksmith_position"] = get_cursor_position_when_hotkey_pressed()
    if is_cancelled:
        return
    print("Set the position for the blacksmith's buy tools button (F6 to set, F8 to cancel)")
    configuration["buy_tools_position"] = get_cursor_position_when_hotkey_pressed()
    if is_cancelled:
        return
    print("Set the position for the item you want to buy back if it was destroyed (F6 to set, F8 to cancel) | If you "
          "need to scroll it won't work, sorry!")
    configuration["buy_tools_target_position"] = get_cursor_position_when_hotkey_pressed()
    if is_cancelled:
        return
    print("Set the position for the buy button (F6 to set, F8 to cancel)")
    configuration["buy_button_position"] = get_cursor_position_when_hotkey_pressed()
    if is_cancelled:
        return
    print("Set the position for the blacksmith's leave button (F6 to set, F8 to cancel)")
    configuration["blacksmith_leave_position"] = get_cursor_position_when_hotkey_pressed()
    if is_cancelled:
        return
    dump_configuration()


def dump_configuration():
    with open(configuration_path, "w") as f:
        json.dump(configuration, f)


def main_loop():
    print("Starting main loop hold F8 to close the application")
    x, y = configuration["upgrade_position"]
    pyautogui.moveTo(x, y, duration=0.1)
    pydirectinput.leftClick(x, y)
    while True:
        if keyboard.is_pressed("f8"):
            break
        x, y = configuration["upgrade_position"]
        pyautogui.moveTo(x, y, duration=0.1)
        pydirectinput.leftClick(x, y, duration=0.1)
        if keyboard.is_pressed("f8"):
            break
        x, y = configuration["upgrade_target_position"]
        pyautogui.moveTo(x, y, duration=0.1)
        pydirectinput.leftClick(x, y, duration=0.1)
        if keyboard.is_pressed("f8"):
            break
        print("pressing upgrade button")
        x, y = configuration["upgrade_button_position"]
        pyautogui.moveTo(x, y, duration=0.1)
        pydirectinput.leftClick(x, y, duration=0.1)
        if keyboard.is_pressed("f8"):
            break
        print("pressing accept button")
        x, y = configuration["upgrade_accept_button_position"]
        pyautogui.moveTo(x, y, duration=0.1)
        pydirectinput.leftClick(x, y, duration=0.1)
        if keyboard.is_pressed("f8"):
            break
        time.sleep(5)
        print("Upgrade finished?")
        x, y = configuration["close_upgrade_menu_position"]
        pyautogui.moveTo(x, y, duration=0.1)
        pydirectinput.leftClick(x, y, duration=0.1)
        if keyboard.is_pressed("f8"):
            break
        x, y = configuration["blacksmith_position"]
        pyautogui.moveTo(x, y, duration=0.1)
        pydirectinput.leftClick(x, y, duration=0.1)
        pydirectinput.leftClick(x, y, duration=0.1)
        if keyboard.is_pressed("f8"):
            break
        time.sleep(1)
        x, y = configuration["buy_tools_position"]
        pyautogui.moveTo(x, y, duration=0.1)
        pydirectinput.leftClick(x, y, duration=0.1)
        if keyboard.is_pressed("f8"):
            break
        x, y = configuration["buy_tools_target_position"]
        pyautogui.moveTo(x, y, duration=0.1)
        pydirectinput.leftClick(x, y, duration=0.1)
        if keyboard.is_pressed("f8"):
            break
        x, y = configuration["buy_button_position"]
        pyautogui.moveTo(x, y, duration=0.1)
        pydirectinput.leftClick(x, y, duration=0.1)
        if keyboard.is_pressed("f8"):
            break
        time.sleep(1.5)
        x, y = configuration["blacksmith_leave_position"]
        pyautogui.moveTo(x, y, duration=0.1)
        pydirectinput.leftClick(x, y, duration=0.1)
        pydirectinput.leftClick(x, y, duration=0.1)
        if keyboard.is_pressed("f8"):
            break
        time.sleep(1.5)


if __name__ == "__main__":
    init_configuration()
    if not is_cancelled:
        print("Starting main loop in 5 seconds")
        time.sleep(5)
        main_loop()
    print("Shutting down")
