# advancedcli
A python library for an advanced console line interface

# Utility
Console Colors such as Foreground, Background and Style elements
```py
from advancedcli import bcolors, fcolors, style

print(fcolors.BRIGHT_RED + "This is foreground!" + style.RESET + "\n"
      + bcolors.BRIGHT_BLUE + "This is background!" + style.RESET + "\n"
      + fcolors.BRIGHT_GREEN + bcolors.BRIGHT_YELLOW + "This is both!" + style.RESET)
```
![Output of code](/output_imgs/1.png)

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
