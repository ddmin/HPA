# HPA

![](https://github.com/ddmin/HPA/blob/master/excelang.png)

# ExceLang
A language based on the Google Sheet Cells and using a Google Sheets backend.

# Commands
| Command name | Function |
| ------------ | ----- |
| RUN | Type into first cell to execute until EOF |
| EOF | Signify end of file |
| MOVE X Y | Move to coordinate X, Y |
| CLICK | Click current position |
| TYPE <word> | Type word |
| WAIT <seconds> | Wait for certain amount of seconds |
| CLOSE | Alt + F4 |
| HOME | Windows Key + D |
| CTRL <key> | Ctrl + <key> |
| WIN | Windows Key |
| ENTER | Press Enter |
| SPACE | Press Spacebar |

# Usage
Example of ExceLang script

(Note this language does not actually support inline comments)
```
RUN                     // Start script
WIN                     // Open search bar
TYPE NOTEPAD            // Look up Notepad program
ENTER                   // Press enter
TYPE HELLO              // Type HELLO
SPACE                   // Type Space
TYPE WORLD              // Type WORLD
EOF                     // Indicate end of file
```
