# advancedcli
A python library for an advanced console line interface

[Download Library](https://downgit.github.io/#/home?url=https://github.com/devskiddlee/advancedcli/blob/main/advancedcli.py)

# Utility
Console Colors such as Foreground, Background and Style elements
```py
from advancedcli import bcolors, fcolors, style

print(fcolors.BRIGHT_RED + "This is foreground!" + style.RESET + "\n"
      + bcolors.BRIGHT_BLUE + "This is background!" + style.RESET + "\n"
      + fcolors.BRIGHT_GREEN + bcolors.BRIGHT_YELLOW + "This is both!" + style.RESET)
```
![Output of code](/output_imgs/1.png)

Clear the Console
```py
from advancedcli import *

clear()
```

You can set it to use linux syntax
```py
from advancedcli import *

use_linux_syntax()
```
This will just switch the clear commands

# Functions
Simple Text with Character & Line Delay
```py
from advancedcli import *

text(
    [fcolors.BRIGHT_MAGENTA + "This is an example of text in advancedcli",
     "You can create an immersive text-adventure experience",
     bcolors.BRIGHT_MAGENTA + "Or another application"],
     line_delay = 0,     # delays the print of the next line (if char_delay is set, line_delay is ignored)
     char_delay = 0.1,   # this will delay each character
     y_line_offset = 2,  # the amount of lines above the text
     x_space_offset = 4) # the amount of spaces in front of the text
                         # i've found that x=y*2 is a good and mostly equal offset
```
![Output of code](/output_imgs/2.png)

Menu with Simple Buttons and Title that you can navigate using the arrow keys
```py
from advancedcli import *

def menu_callback(value):
    print(value)

menu("This is a title", # A title, obviously
     ["Start",          # Here you can add all the options you want
      "Options",
      "Quit"],
      menu_callback)    # callback for logic after selecting
                        # if callback is undefined the function will return the value
                        # could also do value = menu(...)
```
![Output of code](/output_imgs/3.png)
![Output of code](/output_imgs/4.png)

An Input Menu
```py
from advancedcli import *

inputs = input_menu("Very good Title",   # This time we are not using a callback
           ["What is your name?",        # These are the questions
            "What is your age?",         # pretty obvious...
            "What are your strenghts?"])

print(inputs)
```
![Output of code](/output_imgs/5.png)
![Output of code](/output_imgs/6.png)

A option-like menu
```py
from advancedcli import *

options = options_menu("Best title so far, for sure",      # The title
                       ["Quality",                         # These are the option-names
                        "Operating System",
                        "Best country"],
                        [["Low", "Med", "High"],           # These are all the possible values for an option
                         ["Win", "Linux", "macOS"],        # These have no limit but only max 3 will be shown at a time
                         ["France", "USA", "Germany"]])    # The current and the 2 (if possible) nearest values will be shown

print(options)
```
![Output of code](/output_imgs/7.png)
![Output of code](/output_imgs/8.png)
![Output of code](/output_imgs/9.png)
