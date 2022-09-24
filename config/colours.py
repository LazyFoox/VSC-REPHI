DEFAULT = '\033[0m'

class colour:                   # Colours
    DARKGRAY = '\033[2m'
    GRAY = '\033[30m'
    YELLOW_LIGHT = '\033[33m'
    RED_LIGHT = '\033[31m'
    GREEN_LIGHT = '\033[32m'
    BLUE_LIGHT = '\033[34m'
    PURPLE = '\033[95m'
    CYAN_LIGHT = '\033[36m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE_LIGHT = '\033[35m'
    CYAN = '\033[96m'

class highlight:                # Highlight colours
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    PURPLE = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    GRAY = '\033[100m'
    RED_LIGHT = '\033[101m'
    GREEN_LIGHT = '\033[102m'
    YELLOW_LIGHT = '\033[103m'
    BLUE_LIGHT = '\033[104m'
    PURPLE_LIGHT = '\033[105m'
    CYAN_LIGHT = '\033[106m'

class style:                    # Text styles
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    HIGHLIGHT_INVERT = '\033[7m'
    INVISIBLE = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'

class template:                 # Premade templates
    TITLE = f"{DEFAULT}{style.BOLD}{colour.YELLOW_LIGHT}"
    SUBTITLE = f"{DEFAULT}{colour.GRAY}{style.BOLD}"
    WARN = f"{DEFAULT}{style.ITALIC}{colour.YELLOW}"
    BAD = f"{DEFAULT}{style.BOLD}{colour.RED}"
    INFO = f"{DEFAULT}{colour.BLUE}{style.BOLD}"
    FROM = f"{DEFAULT}{colour.PURPLE_LIGHT}"
    DEPENDS = f"{DEFAULT}{colour.GREEN_LIGHT}{style.ITALIC}"
    FATAL = f"{DEFAULT}{colour.RED_LIGHT}{highlight.YELLOW_LIGHT}{style.BOLD}"

def stylize(text,style):        # Stylize individual text
    if str(style).startswith("COLOURS."): 
        raise TypeError
    output = style + text + DEFAULT
    return(output)

def showcase():
    for var in vars(colour).values():
        if str(var).__contains__("None"): next
        elif str(var).__contains__("__"): next
        elif str(var).__contains__("colours"): next
        else:
            print(f"{var}Test\t{DEFAULT}")
    for var in vars(style).values():
        if str(var).__contains__("None"): next
        elif str(var).__contains__("__"): next
        elif str(var).__contains__("colours"): next
        else:
            print(f"{var}Test\t{DEFAULT}")
    for var in vars(style).values():
        if str(var).__contains__("None"): next
        elif str(var).__contains__("__"): next
        elif str(var).__contains__("colours"): next
        else:
            print(f"{var}Test\t{DEFAULT}")
    for var in vars(template).values():
        if str(var).__contains__("None"): next
        elif str(var).__contains__("__"): next
        elif str(var).__contains__("colours"): next
        else:
            print(f"{var}Test\t{DEFAULT}")