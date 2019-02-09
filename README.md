# HPA

![Image](https://github.com/ddmin/HPA/blob/master/excelang.png = 500x300)

# ExceLang
A language based on the Google Sheet Cells and the Google Sheets API.

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
ENTER                   // Start Notepad program
TYPE SHUT               // Type message into Notepad
SPACE                   // Press spacebar
TYPE DOWN               // Type message into Notepad
WAIT 3                  // Wait for 3 seconds
HOME                    // Go to Desktop home
CLOSE                   // Press Alt + F4 to open shutdown prompt
ENTER                   // Confirm shutdown
EOF                     // Terminate program
```
