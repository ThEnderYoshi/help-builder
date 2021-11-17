"""This script is an example on how to use Help Builder."""

import help_builder as hb


terms = [  # Terms is where you write the text of the help str.
    ["plain", "Hello world!"],  # Plain is just plain text.
    ["rule"],  # Rule is a horizontal rule.
    ["plain", "Here are some of the types of terms:"],
    [
        "commands",  # Commands is a list of commands.
        ["plain", "['plain', <text>]", "Plain text."],
        [
            "commands",
            "['commands', <cmd>...]",
            "A list of commands."
        ],
        ["↳   <cmd>", "[<name>, <params>, <desc>]", "Params of <cmd>"],
        ["rule", "['rule', <width>?]", "A horizontal rule."],
    ],
    ["rule", 24],
    ["plain", ("See the source for this example script to "
        + "find out how this is all structured.")],
]


if __name__ == "__main__":
    cy = hb.AnsiColor(hb.AnsiColor.CYAN)
    rs = hb.AnsiColor.RESET
    print("Examples:")
    print(f"{cy}1.{rs} Simple command list")
    print(f"{cy}2.{rs} Simple styled help str")
    idx = input("Type a number: ")


    ### EXAMPLE 1 ###

    if idx.startswith("1"):
        print(hb.build({"terms": terms}))


    ### EXAMPLE 2 ###

    elif idx.startswith("2"):
        config = {  # This dict's structure must match the
                    # source's _config var.
            
            "params": {
                "plain": {
                    "trailing": "\n* '*-._.-*'*-._ .\n",
                },
                "commands": {
                    "align_descs": False,
                    "desc_spacing": 2,
                },
                "rule": {
                    "left_chars": "+- -",
                    "middle_char": "=",
                    "right_chars": "- -+",
                },
            },

            "style": {  # ANSI codes go here.

                "plain": {  # All fields in this level
                            # match the term types' names.
                    
                    #   This field accepts ANSI codes.
                    #   To make life easier, you can use
                    # ↓ the AnsiColor class and it's constants.
                    "color": hb.AnsiColor(hb.AnsiColor.RED, hb.AnsiColor.DIM),
                },
                "commands": {
                    "desc": hb.AnsiColor(hb.AnsiColor.BLUE, hb.AnsiColor.BLUE),
                    # Not all fields need to be included!
                },
                "rule": {
                    "color": "\033[4;35m",  # You may manually write
                                            # ANSI codes, if you wish.
                },
            },
        }
        print(hb.build({"terms": terms, "config": config}))
