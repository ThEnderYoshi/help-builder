"""Help Builder by ThEnderYoshi

A simple library to build beautiful help
strings for the console using ANSI codes.

For help, see the project's GitHub page:
https://github.com/ThEnderYoshi/help-builder
"""

# {"terms": <terms>, "config": <config>}


class AnsiColor():
    RESET = "\033[0;37m"

    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    GRAY = 90

    BOLD = 1
    DIM = 2
    UNDERLINE = 4
    INVERT = 7

    def __init__(self, color: int, modifier=0) -> None:
        self.color = color
        self.mod = modifier
    
    def __repr__(self) -> str:
        return f"\033[{self.mod};{self.color}m"


_config: dict = {  # help["config"] should follow this dict.
    "params": {  # Parameters go here.
        "plain": {
            "trailing": "\n",  # Char(s) after every plain term.
        },
        "commands": {
            "align_descs": True,
            "desc_spacing": 4,
        },
        "rule": {
            "left_chars": "",
            "middle_char": "=",  # Should be only one character.
            "right_chars": "",
            "default_width": 30,  # In characters.
            # ↑ Must be at least the length of left_ and right_chars combined.
        },
    },

    "style": {  # ANSI codes go here.
        "plain": {
            "color": AnsiColor.RESET,
        },
        "commands": {
            "name": AnsiColor(AnsiColor.YELLOW, AnsiColor.BOLD),
            "params": AnsiColor(AnsiColor.GRAY, AnsiColor.BOLD),
            "desc": AnsiColor(AnsiColor.WHITE),
        },
        "rule": {
            "color": AnsiColor(AnsiColor.WHITE, AnsiColor.BOLD),
        },
    },
}
_cust_config: dict = {}


def build(help: dict) -> str:
    """Returns the formatted help string. See the GitHub page for info."""
    global _cust_config
    final_str = ""

    terms = help["terms"]
    if "config" in help:
        _cust_config = help["config"]
    else:
        _cust_config = {}

    # Terms
    for term in terms:
        if term[0] == "plain":
            # Plain text
            col = _get_config("style/plain/color")
            final_str += f"{col}{term[1]}{AnsiColor.RESET}" \
                + _get_config("params/plain/trailing")
        
        elif term[0] == "commands":
            # Command list
            longest_cmd = _get_longest_command(term) \
                + _get_config("params/commands/desc_spacing")

            for c in range(1, len(term)):
                arg = term[c]
                if arg[1] != "":
                    arg[1] = " " + arg[1]
                
                tab = " " * _get_config("params/commands/desc_spacing")
                if _get_config("params/commands/align_descs"):
                    tab = " " * (longest_cmd - len(arg[0] + arg[1]))

                final_str += "{0}{1}{3}{2}\n".format(
                    *_format_command(arg[0], arg[1], arg[2]), tab)
        
        elif term[0] == "rule":
            # Horizontal rule
            mid_amount: int
            if len(term) > 1:
                mid_amount = term[1]
            else:
                mid_amount = _get_config("params/rule/default_width")
            l = _get_config("params/rule/left_chars")
            m = _get_config("params/rule/middle_char")
            r = _get_config("params/rule/right_chars")
            mid_amount -= len(l + r)
            col = _get_config("style/rule/color")

            final_str += f"{col}{l}{m * mid_amount}{r}{AnsiColor.RESET}\n"

    return final_str


def _get_config(path: str) -> any:
    # Go down both config and custom config until either
    # the path ends or custom config runs out of paths.
    # Write path as "path/to/key_name".
    split = path.split("/")
    use_cust = True
    dir_def = _config
    dir_cust = _cust_config
    for d in split:
        dir_def = dir_def[d]
        if d in dir_cust:
            dir_cust = dir_cust[d]
        else:
            use_cust = False
            dir_cust = {}
    
    if use_cust:
        return dir_cust
    return dir_def


def _get_longest_command(terms: list) -> int:
    return max(len(
        terms[t][0] + " " + terms[t][1])for t in range(1, len(terms)))

def _format_command(cmd: str, params: str, desc: str, ) -> list:
    return [
        f"{_get_config('style/commands/name')}{cmd}{AnsiColor.RESET}",
        f"{_get_config('style/commands/params')}{params}{AnsiColor.RESET}",
        f"{_get_config('style/commands/desc')}{desc}{AnsiColor.RESET}",
    ]
