import curses

def get_integer(stdscr, message):
    stdscr.addstr(message)
    stdscr.refresh()
    value = int(stdscr.getstr().decode())
    return value

def get_string(stdscr, message):
    stdscr.addstr(message)
    stdscr.refresh()
    return stdscr.getstr().decode()
