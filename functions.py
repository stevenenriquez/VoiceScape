import pyautogui
import time
import subprocess
from coordinates import *
from multiprocessing import Process

AUTOHOTKEY_PATH = "C:\Program Files\AutoHotkey\AutoHotKey.exe"

def speak(text):
	pyautogui.typewrite(text)
	pyautogui.press('enter')

def turn(direction):
	if direction == 'left':
		pyautogui.keyDown('right')
		time.sleep(.9)
		pyautogui.keyUp('right')
	if direction == 'right':
		pyautogui.keyDown('left')
		time.sleep(.9)
		pyautogui.keyUp('left')
	if direction == 'around':
		pyautogui.keyDown('left')
		time.sleep(1.8)
		pyautogui.keyUp('left')

def walk(direction, distance):

	goto = direction + str(distance)

	current_pos = pyautogui.position()
	pyautogui.moveTo(*eval(goto), .5)
	pyautogui.click()
	pyautogui.moveTo(current_pos)

def end():
	pyautogui.typewrite('Bye!')
	pyautogui.press('enter')

def turnaround():
	pyautogui.keyDown('left')
	time.sleep(7.2)
	pyautogui.keyUp('left')

def bow():
	pyautogui.press('f3')
	pyautogui.press('f4')

	platebody = pyautogui.locateCenterOnScreen('pics/platebody.png', region=(1662,557, 300, 550))
	platelegs = pyautogui.locateCenterOnScreen('pics/platelegs.png', region=(1662,557, 300, 550))
	medhelm = pyautogui.locateCenterOnScreen('pics/medhelm.png', region=(1662,557, 300, 550))
	shield = pyautogui.locateCenterOnScreen('pics/shield.png', region=(1662,557, 300, 550))
	sword = pyautogui.locateCenterOnScreen('pics/sword.png', region=(1662,557, 300, 550))

	for i in (sword, medhelm, platebody, platelegs, shield):
		pyautogui.click(*(i), duration=0.4)
		time.sleep(.1)
		pyautogui.click()


	pyautogui.press('f10')
	pyautogui.press('f11')
	pyautogui.click(1792,802, duration=0.5)
	pyautogui.typewrite('Hope you enjoyed!')
	pyautogui.press('enter')

def dance():
	x = 1705
	y = 950
	current_pos = pyautogui.position()
	pyautogui.keyDown('down')
	pyautogui.press('f10')
	pyautogui.press('f11')
	pyautogui.typewrite('Check this out!')
	pyautogui.press('enter')
	Process(target=turnaround).start()
	#pyautogui.scroll(-5000)
	pyautogui.scroll(5000)
	#pyautogui.scroll(-5000)
	#pyautogui.scroll(5000)
	pyautogui.keyUp('down')
	pyautogui.moveTo(x, y, .5)
	for i in range(4):
		pyautogui.click(x + (40 * i), y, duration=.5)
		time.sleep(1.1)
	pyautogui.moveTo(current_pos)

def fire():
	pyautogui.press('f1')
	pyautogui.press('esc')
	tinderbox = pyautogui.locateCenterOnScreen('pics/tinderbox.png')
	log = pyautogui.locateCenterOnScreen('pics/log.png')
	pyautogui.moveTo(*(tinderbox), .5)
	pyautogui.click()
	pyautogui.moveTo(*(log), .5)
	pyautogui.click()

def suitup():
	pyautogui.press('f4')
	pyautogui.press('esc')
	time.sleep(.1)

	pyautogui.moveTo(1800, 650, .5)

	platebody = pyautogui.locateCenterOnScreen('pics/platebody.png', region=(1662,557, 300, 550))
	platelegs = pyautogui.locateCenterOnScreen('pics/platelegs.png', region=(1662,557, 300, 550))
	medhelm = pyautogui.locateCenterOnScreen('pics/medhelm.png', region=(1662,557, 300, 550))
	shield = pyautogui.locateCenterOnScreen('pics/shield.png', region=(1662,557, 300, 550))
	sword = pyautogui.locateCenterOnScreen('pics/sword.png', region=(1662,557, 300, 550))

	pyautogui.press('esc')
	pyautogui.press('f4')
	time.sleep(.1)

	equiptment = pyautogui.locateCenterOnScreen('pics/equiptment.png', region=(1662,557, 300, 550))
	
	for i in (equiptment, platebody, platelegs, medhelm, shield, sword):
		pyautogui.click(*(i), duration=0.4)
		time.sleep(.1)
		pyautogui.click()

	eqexit = pyautogui.locateCenterOnScreen('pics/eqexit.png')

	pyautogui.click(*(eqexit), duration=0.8)

	pyautogui.typewrite('Ready for battle!')
	pyautogui.press('enter')

def chop():
	directions = (up1, right1, down1, left1)
	for direction in directions:
		pyautogui.rightClick(*direction, duration=2)
		tree_coords = pyautogui.locateCenterOnScreen('pics/tree.png')
		if tree_coords:
			pyautogui.click(*tree_coords, duration=0.5)
			break
		else:
			pyautogui.click()

def initialize():
	subprocess.call([AUTOHOTKEY_PATH, 'max_window.ahk'])

	current_pos = pyautogui.position()
	pyautogui.click(1724, 45, duration=0.5)
	pyautogui.moveTo(current_pos)

	pyautogui.keyDown('up')
	time.sleep(2)
	pyautogui.keyUp('up')

	pyautogui.scroll(5000)
	pyautogui.scroll(-2000)



		