
import readline

def hello(*args):
    return "<<hello"
def add(*args):
    return "<<add"
def change(*args):
    return "<<change"
def phone(*args):
    return "<<phone"
def show_all(*args):
    return "<<show_all"
def good_bye(*args):
    exit(0)
    return None
def show_next(*args):
    return "<<show_next"
def rename(*args):
    return "<<rename"
def find(*args):
    return "<<find"
def no_command(*args):
    return "Unknown command"

COMMANDS = {
    hello: ("hello", "hi"),
    add: ("add", "+"),
    change: ("change", "edit"),
    phone: ("phone", "user"),
    show_all: ("showall", "all"),
    good_bye: ("exit", "close", "end"),
    show_next: ("next",),
    rename: ("rename",),
    find: ("find", "see", "seek", "search"),
}

################################################################
def complete(text, state):
    results = []
    if len(text) > 0:
        for cmd, kwds in COMMANDS.items():
            for kwd in kwds:
                if kwd.lower().startswith(text):
                    results.append(kwd)
    results.append(None)
    return results[state]
################################################################
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)
################################################################

def parser(text: str):
    for cmd, kwds in COMMANDS.items():
        for kwd in kwds:
            if text.lower().startswith(kwd):
                data = text[len(kwd):].strip().split()
                return cmd, data 
    return no_command, None

def main():
    while True:
        user_input = input(">>>")
        command, args = parser(user_input)
        if args != None:
            result = command(*args)
        else:
            result = command()
        
        if result: print(result)

###############################################
if __name__ == "__main__":
    main()
