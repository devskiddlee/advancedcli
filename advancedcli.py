import os
import keyboard
import time

class fcolors:
    BLACK = "\033[30m"
    DARK_RED = "\033[31m"
    DARK_GREEN = "\033[32m"
    DARK_YELLOW = "\033[33m"
    DARK_BLUE = "\033[34m"
    DARK_MAGENTA = "\033[35m"
    DARK_CYAN = "\033[36m"
    DARK_WHITE = "\033[37m"
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    WHITE = "\033[97m"

class bcolors:
    BLACK = "\033[40m"
    DARK_RED = "\033[41m"
    DARK_GREEN = "\033[42m"
    DARK_YELLOW = "\033[43m"
    DARK_BLUE = "\033[44m"
    DARK_MAGENTA = "\033[45m"
    DARK_CYAN = "\033[46m"
    DARK_WHITE = "\033[47m"
    BRIGHT_BLACK = "\033[100m"
    BRIGHT_RED = "\033[101m"
    BRIGHT_GREEN = "\033[102m"
    BRIGHT_YELLOW = "\033[103m"
    BRIGHT_BLUE = "\033[104m"
    BRIGHT_MAGENTA = "\033[105m"
    BRIGHT_CYAN = "\033[106m"
    WHITE = "\033[107m"

class style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    ACTIVE = bcolors.BRIGHT_GREEN

linux = False

def use_linux_syntax():
    global linux
    linux = True

def clear():
    if linux:
        os.system("clear")
        return
    os.system("cls")

def menu(title: str, options: list[str], callback = None):
    active = 0
    while True:
        clear()
        print(title + style.RESET)
        print("")
        for option in options:
            if options[active] == option:
                print(style.ACTIVE + option + style.RESET)
                continue
            print(option + style.RESET)
        key = keyboard.read_event(True)
        if key.scan_code in keyboard.key_to_scan_codes("up"):
            if active != 0:
                active -= 1
        if key.scan_code in keyboard.key_to_scan_codes("down"):
            if active != len(options)-1:
                active += 1
        if key.scan_code in keyboard.key_to_scan_codes("enter"):
            clear()
            if callback:
                callback(active)
                return
            else:
                return active
        time.sleep(0.1)

def input_menu(title: str, options: list[str], callback = None):
    print(title + style.RESET)
    inputs = []
    for option in options:
        inputs.append(input(f"{option}: " + style.RESET))
    if callback:
        callback(inputs)
    return inputs

def options_menu(title: str, options: list[str], values: list[list[str]], callback = None):
    selected = []
    for value in values:
        selected.append(0)
    active = 0
    while True:
        clear()
        print(title + style.RESET)
        print("")
        if active == len(options):
            for i in range(len(options)):
                print(options[i] + ": " + style.RESET + str(values[i][selected[i]]) + style.RESET)
            print(style.BOLD + bcolors.BRIGHT_RED + "Enter to ACCEPT" + style.RESET)
        else:
            for i in range(len(options)):
                string = ""
                if selected[i]-1 >= 0:
                    string += "← "+ values[i][selected[i]-1] + " " + style.RESET
                string += fcolors.BRIGHT_GREEN + values[i][selected[i]] + style.RESET
                if selected[i]+1 < len(values[i]):
                    string += " " + values[i][selected[i]+1] + " →" + style.RESET
                    
                if options[active] == options[i]:
                    print(style.ACTIVE + options[i]+ style.RESET + ": " + string + style.RESET)
                    continue
                print(options[i] + style.RESET + ": " + string + style.RESET)
            print(style.BOLD + fcolors.BRIGHT_RED + "ACCEPT" + style.RESET)
        key = keyboard.read_event(True)
        if key.scan_code in keyboard.key_to_scan_codes("right"):
            if active != len(options) and selected[active] != len(values[active])-1:
                selected[active] += 1
        if key.scan_code in keyboard.key_to_scan_codes("left"):
            if active != len(options) and selected[active] != 0:
                selected[active] -= 1
        if key.scan_code in keyboard.key_to_scan_codes("up"):
            if active != 0:
                active -= 1
        if key.scan_code in keyboard.key_to_scan_codes("down"):
            if active != len(options):
                active += 1
        if key.scan_code in keyboard.key_to_scan_codes("enter"):
            if active == len(options):
                clear()
                if callback:
                    callback(selected)
                    return
                else:
                    return selected
        time.sleep(0.1)

def text(lines : list[str], line_delay : float = 0, char_delay : float = 0, y_line_offset : int = 0, x_space_offset : int = 0):
    clear()
    for i in range(y_line_offset):
        print("")
    offset = ""
    for i in range(x_space_offset):
        offset += " "
    if char_delay == 0:
        for line in lines:
            print(offset + line)
            time.sleep(line_delay)
    else:
        done = []
        for line in lines:
            for i in range(len(line)):
                for d in done:
                    print(d)
                print(offset + line[0:i+1])
                time.sleep(char_delay)
                clear()
            done.append(line)
    for d in done:
        print(d)
    keyboard.wait("enter", True)