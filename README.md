# eTextEdit
Extensible Text Editor; built with prompt toolkit

Originally a simple text editor created by Jonathan Slenders
Source: https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/examples/full-screen/text-editor.py

Modified and Enhanced by Eliran Wong:
* added file and clipboard utilities
* added regex search & replace feature
* added key bindings
* added handling of unasaved changes
* added dark theme and lexer style
* support stdin, e.g. echo "Hello world!" | etextedit
* support file argument, e.g. etextedit <filename>
* support startup with clipboard text content, e.g. etextedit -p true
* support printing
* support plugins, written in python, to extend the editor functionalities; place plugins in ~/etextedit/plugins

Check plugins examples at https://github.com/eliranwong/agentmake/tree/main/agentmake/etextedit_plugins

eTextEdit repository:
https://github.com/eliranwong/eTextEdit

# Screenshots

<img width="706" height="519" alt="Image" src="https://github.com/user-attachments/assets/dcd4f05d-3e43-4f4b-96b2-5994fda130bf" />

![search_replace](https://github.com/eliranwong/eTextEdit/assets/25262722/c7a564ce-2e3c-4913-8210-52e259545044?raw=True)

![menu](https://github.com/eliranwong/eTextEdit/assets/25262722/7703f138-e56e-4c6f-84fc-4abe768f161a?raw=True)

# Download

> pip install --upgrade etextedit

# Usage

To launch eTextEdit:

> etextedit

To open a text file, e.g. test.txt:

> etextedit test.txt

To pipe in a text string, e.g. "Hello World!":

> echo "Hello World!" | etextedit

To append a file, e.g. test.txt, with a text string, e.g. "Hello World!":

> echo "Hello World!" | etextedit test.txt

# Key Bindings

escape + m: toggle menu

control + k: help

control + q: quit

control + a: select all

escape + a: deselect all

control + c: copy

control + v: paste

control + x: cut

control + z: undo

control + i: insert spaces

control + f: find

escape + f: clear i-search highlights

control + r: find & replace

control + l: go to line

control + d: delete

control + n: new file

control + o: open file

control + s: save file

control + w: save as file

## Navigation

escape + a: go to beginning of document

escape + z: go to end of document

escape + b: go to beginning of current line

escape + e: go to end of current line

## Plugins

An 'etextedit' plugin is designed to run script to process the selected text or the whole text in the editor.

Examples of 'etextedit' plugins:

https://github.com/eliranwong/etextedit/tree/main/package/etextedit/etextedit_plugins

https://github.com/eliranwong/agentmake/tree/main/agentmake/etextedit_plugins

https://github.com/eliranwong/biblemate/tree/main/package/biblemate/etextedit/plugins

User can create custom plugins and place them in directory '~/etextedit/plugins' for them to work with 'etextedit'.

Each 'etextedit' plugin is written in python.

Read the comments in the following example to get ideas how to write a plugin:

https://github.com/eliranwong/etextedit/blob/main/package/etextedit/etextedit_plugins/Change%20to%20Upper%20Cases.py
