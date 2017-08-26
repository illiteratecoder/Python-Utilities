"""ANSI Escape Sequences for colored output. Runs with both Python2 and Python3"""

def colored(args, msg):
    colors = {
        "black":     "\x1b[30m",
        "red":       "\x1b[31m",
        "green":     "\x1b[32m",
        "yellow":    "\x1b[33m",
        "blue":      "\x1b[34m",
        "magenta":   "\x1b[35m",
        "cyan":      "\x1b[36m",
        "white":     "\x1b[37m",
        "bold":      "\x1b[1m", # bold/bright
        "italic":    "\x1b[3m",
        "underline": "\x1b[4m",
        "end":       "\x1b[0m",
    }

    output = ""

    for arg in args:
        output += colors[arg]

    output += msg
    output += colors["end"]
    return output
