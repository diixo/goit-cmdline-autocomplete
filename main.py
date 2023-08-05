
#pip install pyreadline3

import readline

def hello():
   pass
def add():
   pass
def change():
   pass
def phone():
   pass
def show_all():
   pass
def good_bye():
    exit(0)
    return None
def show_next():
   pass
def rename():
   pass
def find():
   pass
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
    find: ("find", "search"),
}

def complete(text, state):
    results = []
    for cmd, kwds in COMMANDS.items():
        for kwd in kwds:
            if kwd.lower().startswith(text):
                results.append(kwd)
                results.append(None)   
    return results[state]

################################################################
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

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
