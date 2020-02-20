# Tools

## Windows Terminal

* keybindins (profiles.json)

    ```json
    {
        // Add any keybinding overrides to this array.
        // To unbind a default keybinding, set the command to "unbound"
        "keybindings": [
            { "command": "newTab",   "keys": ["ctrl+t"] },
            { "command": "closeTab", "keys": ["ctrl+w"] },
            { "command": "prevTab",  "keys": ["ctrl+pgup"] },
            { "command": "nextTab",  "keys": ["ctrl+pgdn"] }
        ]
    }
    ```
