import pyautogui
from pynput import keyboard

def main():

	with keyboard.Listener(on_press=on_press) as listener:
		listener.join()

def on_press(key):

	try:
		# get position at cursor
		if key.char == "p":
			print(pyautogui.position())
			pyautogui.press('backspace')
		if key.char == "x":
			return False
	except:
		pass

if __name__ == "__main__":
	main()