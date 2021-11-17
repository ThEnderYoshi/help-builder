# Help Builder
A Python library to make pretty help strings!

Help Builder doesn't use any other libraries, just pure Python!

## Example:

The following Python code:
```python
import help_builder as hb

terms = [
    ["rule"],
    ["plain", "Welcome to the Example NotARealAPI!"],
    ["plain", "Here's a list of commands:"],
    ["rule"],
    [
        "commands",
        ["help", "", "Show this list."],
        ["foo", "<bar> <baz>", "Some command."]
    ],
    ["rule"],
]

print(hb.build({"terms": terms}))
```
Will output: \
![The code above, but nice and formatted](https://user-images.githubusercontent.com/24496547/142094247-8688077f-13a4-4367-8e13-37fd9889a168.png)

If you don't like the colors, you can style it!
```python
config = {
    "params": {
        "rule": {
            "default_width": 40,
        },
    },
    "style": {
        "commands": {
            "name": hb.AnsiColor(hb.AnsiColor.CYAN, hb.AnsiColor.BOLD),  # ANSI color helper class!
            "params": "\033[2;33m",  # You can also manually write the codes.
        },
        "rule": {
            "color": hb.AnsiColor(hb.AnsiColor.RED),
        },
    },
}

print(hb.build({"terms": terms, "config": config}))
```

The same output as before, but with the styling: \
![The same as the image above, but the colors are different](https://user-images.githubusercontent.com/24496547/142095257-241b070a-8d42-480e-8309-f0ebce74ec9d.png)

## How to use?

Simply import the script and call it's `build()` method.
It takes a dict that takes a `terms` list (text) and, optionally, a `config` dict (styling).

For further reading, refer to the [repo's wiki](https://github.com/ThEnderYoshi/help-builder/wiki).
