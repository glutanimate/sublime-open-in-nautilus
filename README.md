# Open in Nautilus

## Overview

This is a simple Sublime Text 3 package that adds a hotkey and command to reveal a file in its parent directory with Nautilus (GNOME and Unity's file manager).

## Usage

The hotkey defaults to <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd>. Use the `open_folder_in_nautilus` command in your key bindings to customize it, e.g.:


```json
[
    { 
      "keys": ["alt+shift+f"], "command": "open_folder_in_nautilus"
    }
]
```

In addition to the hotkey, you can access the plugin via the command palette (command: *Open in Nautilus file manager*).

## License

This plugin is licensed under the [GNU GPLv3](http://www.gnu.de/documents/gpl-3.0.en.html). A copy of the license is included in the LICENSE file that accompanies this README.

*Copyright 2014 Glutanimate*.