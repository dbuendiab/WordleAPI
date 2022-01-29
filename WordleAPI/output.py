FG_BLACK = "30"
FG_RED = "31"
FG_GREEN = "32"
FG_YELLOW = "33"
FG_BLUE = "34"
FG_PURPLE = "35"
FG_CYAN = "36"
FG_WHITE = "37"

FGB_BLACK = "90"
FGB_RED = "91"
FGB_GREEN = "92"
FGB_YELLOW = "93"
FGB_BLUE = "94"
FGB_PURPLE = "95"
FGB_CYAN = "96"
FGB_WHITE = "97"

BG_BLACK = "40"
BG_RED = "41"
BG_GREEN = "42"
BG_YELLOW = "43"
BG_BLUE = "44"
BG_PURPLE = "45"
BG_CYAN = "46"
BG_WHITE = "47"

BGB_BLACK = "100"
BGB_RED = "101"
BGB_GREEN = "102"
BGB_YELLOW = "103"
BGB_BLUE = "104"
BGB_PURPLE = "105"
BGB_CYAN = "106"
BGB_WHITE = "107"

plantilla = "\x1b[%sm %s \x1b[0m"


def color(fg, bg):
    return "0;{};{}".format(fg, bg)


def aviso(texto):
    r = plantilla % (color(FG_WHITE, BG_RED), texto)
    print(r)


def aviso2(texto):
    r = plantilla % (color(FGB_WHITE, BG_BLACK), texto)
    print(r)


def forbidden(texto):
    s = plantilla % (color(FG_WHITE, BG_BLACK), "descartes: ")
    r = plantilla % (color(FG_YELLOW, BG_BLACK), texto)
    print(s + r)


def candidatas(texto):
    s = plantilla % (color(FG_WHITE, BG_BLACK), "posibles: ")
    r = plantilla % (color(FGB_BLUE, BG_BLACK), texto)
    print(s + r)


def printc(guess, test, last=False):
    s = ""
    r = ""
    for (ch, cl) in zip(guess.upper(), test):
        if cl == '0':
            r += plantilla % (color(FG_WHITE, BG_BLACK), ' ')
            s += plantilla % (color(FG_WHITE, BG_BLACK), ch)
        if cl == '1':
            r += plantilla % (color(FG_BLACK, BG_YELLOW), ' ')
            s += plantilla % (color(FG_BLACK, BG_YELLOW), ch)
        if cl == '2':
            r += plantilla % (color(FG_BLACK, BG_GREEN), ' ')
            s += plantilla % (color(FG_BLACK, BG_GREEN), ch)
    if last is True:
        print(r)
    print(s)
    if last is True:
        print(r)


# Python program to print
# colored text and background
def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


if __name__ == "__main__":
    print_format_table()

    printc("casal", "01021")
    printc("assert", "22122")
