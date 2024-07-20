import os
import time	

colourRed = '\033[31m'
colourOrange = '\033[33m'
colourGreen = '\033[32m'
colourWhite = '\033[0m'

def fileModification(directory, oldExtension, newExtension):
	startTime = time.time()
	filesModified = 0
	for fileName in os.listdir(directory):
		filePath = os.path.join(directory, fileName)
		newFileName = fileName[:-len(oldExtension)] + newExtension
		newFilePath = os.path.join(directory, newFileName)
		if fileName == "__main__.py":
			print(colourOrange + "Skipped modifying main.py")
		elif os.path.isdir(filePath) or os.path.islink(filePath):
			print(colourOrange + "Skipped modifying subdirectory")
		elif os.path.isfile(newFilePath):
			print(colourRed + "Skipped modifying " + fileName + " because a file named " + newFileName + " already exists")
		elif fileName[-len(oldExtension):] != oldExtension:
			print(colourOrange + "Skipped modifying " + fileName + " because it is not a " + oldExtension +" file")
		else:
			os.rename(filePath, newFilePath)
			print(colourGreen + "Modified name of " + fileName + " to " + newFileName)
			filesModified = filesModified + 1
	endTime = time.time()
	elapsedTime = endTime - startTime
	print(colourWhite + "Modified " + str(filesModified) + " file extensions in " + str(elapsedTime) + " seconds")

def main():
	print("Welcome to File-Extension-Modifier by Dan-Foord")
	inputDirectory = input("Please enter the path of the directory in which you would like to modify the file extensions")
	inputOldExtension = input("Please enter the file extension that you would like to change from")
	inputNewExtension = input("Please enter the file extension that you would like to change to")
	input("Changing files in " + inputDirectory + " from " + inputOldExtension + " to " + inputNewExtension + ". Press enter to continue.")
	fileModification(inputDirectory, inputOldExtension, inputNewExtension)

if __name__ == "__main__":
    main()