import os
import time
import functions
import importlib

file_dir = "C:/Users/Steven/Dropbox/GH/command.txt"

def main():

	while True:

		try:
			file = open(file_dir, 'r')

			importlib.reload(functions)

			command = tuple(line.strip() for line in file)
			print(command)
			
			file_command = command[0]

			if file_command == "end":
				functions.end()
				closeListener(file)
				break
			if file_command == "say":
				file_content = command[1]
				functions.speak(file_content)
			if file_command == "turn":	
				file_content = command[1]
				functions.turn(file_content)
			if file_command == "walk":
				file_content = command[1]
				direction, distance, _ = file_content.split()
				functions.walk(direction, distance)
			if file_command == "dance":
				functions.dance()
			if file_command == "bow":
				functions.bow()
			if file_command == "fire":
				functions.fire()
			if file_command == "suit":
				functions.suitup()
			if file_command == "tree":
				functions.chop()
			if file_command == "init":
				functions.initialize()

			# closing/deleting file
			closeListener(file)

		except FileNotFoundError:
			pass
		except IOError as e:
			print(e)
		except Exception as e:
			print(e)
			closeListener(file)
			for file in os.listdir("C:/Users/Steven/Dropbox/GH/"):
				try:
					os.remove("C:/Users/Steven/Dropbox/GH/" + file)
				except:

def closeListener(file):
	time.sleep(.1)
	file.close()
	os.remove(file_dir)

if __name__ == "__main__":
	main()

