if command == 'CLOSE':
    pyautogui.hotkey('alt', 'f4')

elif command.startswith('MOVE'):
    _, x, y = command.split()
    pyautogui.moveTo(int(x), int(y))

elif command == 'CLICK':
    pyautogui.click()

elif command == 'HOME':
    pyautogui.hotkey('win', 'd')

elif command == 'WIN':
    pyautogui.press('win')

elif command.startswith('TYPE'):
    _, phrase = command.split()
    pyautogui.typewrite(phrase)

elif command.startswith('WAIT'):
    _, sec = command.split()
    time.sleep(int(sec))

elif command == 'ENTER':
    pyautogui.press('enter')

elif command == 'SPACE':
    pyautogui.press('space')

elif command.startswith('CTRL'):
    _, key = command.split()
    pyautogui.hotkey('ctrl', key)

elif command == 'EOF':
    break

else:
    break
