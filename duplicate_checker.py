import os
class DATA:  
    def arr_to_str(data, div1 = "  ", div2 = "##", div3 = "!!"):
        # Formats 1D or 2D or 3D array into string
        # div1 divides 1st dimension [a, b, c]
        # div2 divides 2nd dimension [[a, b, c]]
        # div3 divides 3rd dimension [[[a, b, c]]]
        str1 = ""
        for dat in data:
            if isinstance(dat, str):
                str1 += dat
            elif isinstance(dat, list):
                for da in dat:
                    if isinstance(da, str):
                        str1 += da
                    elif isinstance(da, list):
                        for d in da:
                            str1 += d + div3
                        str1 = str1[:-len(div3)]
                    str1 += div2
                str1 = str1[:-len(div2)]
            str1 += div1
        str1 = str1[:-len(div1)]
        return str1

    def str_to_arr(data, div1 = "\n", div2 = "  ", div3 = "##", div4 = "!!"):
        # Reads formatted data and converts it into up to 4D array
        data = data.split(div1)
        for i in range(len(data)):
            if data[i].__contains__(div2):
                data[i] = data[i].split(div2)
                for x in range(len(data[i])):
                    if data[i][x].__contains__(div3):
                        data[i][x] = data[i][x].split(div3)
                        for y in range(len(data[i][x])):
                            if data[i][x][y].__contains__(div4):
                                data[i][x][y] = data[i][x][y].split(div4)
        if data == None:
            data = []
        elif data[-1] == "":
            data.pop(-1)
        return data

class ANSI: # VSCODE darkmode automatically bumps up darker values so there is a minimum brightness
    reset = "\033[0m"
    class fg:
        ESC = "\033["
        # Dark colors from 30-37 
        black       = ESC + "30m"
        red         = ESC + "31m"
        green       = ESC + "32m"
        yellow      = ESC + "33m"
        blue        = ESC + "34m"
        magenta     = ESC + "35m"
        cyan        = ESC + "36m"
        # Bright colors from 90-97
        bright_red     = ESC + "91m"
        bright_green   = ESC + "92m"
        bright_yellow  = ESC + "93m"
        bright_blue    = ESC + "94m"
        bright_magenta = ESC + "95m"
        bright_cyan    = ESC + "96m"
        white          = ESC + "97m"
        # Use empty slot at 38 for custom color
        def rgb(r=255, g=255, b=255): return "\033[38;2;" + str(r % 256) + ";" + str(g % 256) + ";" + str(b % 256) + "m"
        #bright_gray = ESC + "37m" # <-- Functions same as white on this console
        #gray        = ESC + "90m" # <-- Functions same as black on this console

    class bg:
        ESC = "\033["
        # Dark colors from 40-47 
        black       = ESC + "40m"
        red         = ESC + "41m"
        green       = ESC + "42m"
        yellow      = ESC + "43m"
        blue        = ESC + "44m"
        magenta     = ESC + "45m"
        cyan        = ESC + "46m"
        # Bright colors from 100-107
        bright_red     = ESC + "101m"
        bright_green   = ESC + "102m"
        bright_yellow  = ESC + "103m"
        bright_blue    = ESC + "104m"
        bright_magenta = ESC + "105m"
        bright_cyan    = ESC + "106m"
        white          = ESC + "107m"
        # Use empty slot at 48 for custom color
        def rgb(r=255, g=255, b=255): return "\033[48;2;" + str(r % 256) + ";" + str(g % 256) + ";" + str(b % 256) + "m"
        #bright_gray = ESC + "47m" # <-- Functions same as white on this console
        #gray        = ESC + "1000m" # <-- Functions same as black on this console

    class style:
        ESC = "\033["
        bold      = ESC + "1m"
        dim       = ESC + "2m" # Doesn't work in default console
        underline = ESC + "4m"
        blink     = ESC + "5m"
        reverse   = ESC + "7m" # Inverts BG and FG
        hide      = ESC + "8m"

    def black(text):
        return ANSI.fg.black + text + ANSI.reset
    def red(text):
        return ANSI.fg.red + text + ANSI.reset
    def green(text):
        return ANSI.fg.green + text + ANSI.reset
    def yellow(text):
        return ANSI.fg.yellow + text + ANSI.reset
    def blue(text):
        return ANSI.fg.blue + text + ANSI.reset
    def magenta(text):
        return ANSI.fg.magenta + text + ANSI.reset
    def cyan(text):
        return ANSI.fg.cyan + text + ANSI.reset
    def bright_red(text):
        return ANSI.fg.bright_red + text + ANSI.reset
    def bright_green(text):
        return ANSI.fg.bright_green + text + ANSI.reset
    def bright_yellow(text):
        return ANSI.fg.bright_yellow + text + ANSI.reset
    def bright_blue(text):
        return ANSI.fg.bright_blue + text + ANSI.reset
    def bright_magenta(text):
        return ANSI.fg.bright_magenta + text + ANSI.reset
    def bright_cyan(text):
        return ANSI.fg.bright_cyan + text + ANSI.reset
    def white(text):
        return ANSI.fg.white + text + ANSI.reset
    def reset_all():
        print(ANSI.reset)

# UTIL FUNCTIONS

def clear():
    os.system("cls")

def error(text):
    clear()
    print(ANSI.fg.bright_red + text)
    buffer()

def buffer():
    print(ANSI.black("Press enter to continue\n>>> "), end = "")
    input()

def read_file():
    with open("data.txt", "r") as file:
        data = DATA.str_to_arr(file.read())
    return data

data = read_file()
names = [dat[0] for dat in data]
countries  = [dat[2] for dat in data]
chosen = []
countries_chosen = []
matches = []

def reset():
    global chosen, countries_chosen, display, matches, names, countries, data
    data = read_file()
    names = [dat[0] for dat in data]
    countries  = [dat[2] for dat in data]
    chosen = []
    countries_chosen = []
    matches = []

def menu():
    global chosen, countries_chosen, display, matches, names, countries, data
    clear()
    display = []
    for i in range(len(data)):
        dat = data[i]
        display.append(str(i+1) + ") " + dat[0] + " - " + dat[2] + "(" + str(dat[1]) + ")")
    
    # DISPLAY
    colors = ["92m", "93m", "91m", "30m"] # [green, yellow, red, black]
    for i in range(len(display)):
        level = 0
        for match0 in matches:
            if names[i] in match0:
                level += 1
        for country in countries_chosen:
            if countries[i] == country:
                level += 1
        if level > 3:
            level = 3
        print("\033[" + colors[level] + display[i])

    # INFO
    print("\n\033[96m---------Duplicate_chekcer_v1.py---------")
    print("\n\033[92m■ = No duplicate matches") 
    print("\033[93m■ = One duplicate matches") 
    print("\033[91m■ = Two duplicate matches") 
    print("\033[30m■ = Three duplicate matches\n")   
    print("Selected", end = " : ")
    print(chosen)
    # INPUT
    if len(chosen) == 4:
        print("Maxinum selected is (4)")
    cmd = input("Command (x to reset)  : ")
    if cmd.isnumeric() and len(chosen) < 4:
        cmd = int(cmd)
        if cmd > 0 and cmd <= len(names):
            cmd -= 1
            chosen.append(names[cmd])
            countries_chosen.append(data[cmd][2])
            matches.append(data[cmd][3])
            countries.pop(cmd)
            data.pop(cmd)
            names.pop(cmd)
        else:
            error("Command out of range")
    elif cmd == "x":
        reset()
        menu()
    else:
        error("Command must be int")
    menu()

reset()
menu()