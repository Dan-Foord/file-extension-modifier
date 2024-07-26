import os
import time	

colourRed = '\033[31m'
colourOrange = '\033[33m'
colourGreen = '\033[32m'
colourWhite = '\033[0m'

def displayArt():
	logoArt = r"""
    ___ _ _                                                 _                  
   / __|_) |                           _                   (_)                 
 _| |__ _| | _____ _____ _____ _   _ _| |_ _____ ____   ___ _  ___  ____ _____ 
(_   __) | || ___ (_____) ___ ( \ / |_   _) ___ |  _ \ /___) |/ _ \|  _ (_____)
  | |  | | || ____|     | ____|) X (  | |_| ____| | | |___ | | |_| | | | |     
  |_|  |_|\_)_____)     |_____|_/ \_)  \__)_____)_| |_(___/|_|\___/|_| |_|     
                                                                               
                 _ _    ___ _                                                  
                | (_)  / __|_)                                                 
 ____   ___   __| |_ _| |__ _ _____  ____                                      
|    \ / _ \ / _  | (_   __) | ___ |/ ___)                                     
| | | | |_| ( (_| | | | |  | | ____| |                                         
|_|_|_|\___/ \____|_| |_|  |_|_____)_|                                         
                                                                                                  
	"""
	print(logoArt)

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')

def fileModification(directory, oldExtension, newExtension):
	startTime = time.time()
	filesModified = 0
	
	for fileName in os.listdir(directory):

		filePath = os.path.join(directory, fileName)

		if oldExtension != "":
			newFileName = fileName[:-len(oldExtension)] + newExtension
		else:
			newFileName = fileName + newExtension

		newFilePath = os.path.join(directory, newFileName)

		if fileName == "__main__.py":
			print(colourOrange + "Skipped modifying __main__.py")
		elif os.path.isdir(filePath) or os.path.islink(filePath):
			print(colourOrange + "Skipped modifying subdirectory")
		elif os.path.isfile(newFilePath):
			print(colourRed + "Skipped modifying " + fileName + " because a file named " + newFileName + " already exists")
		elif oldExtension != "" and not fileName.endswith(oldExtension):
			print(colourOrange + "Skipped modifying " + fileName + " because it is not a " + oldExtension + " file")
		elif oldExtension == "" and "." in fileName:
			print(colourOrange + "Skipped modifying " + fileName + " because it already has a file extension")
		else:
			os.rename(filePath, newFilePath)
			print(colourGreen + "Modified name of " + fileName + " to " + newFileName)
			filesModified = filesModified + 1

	endTime = time.time()
	elapsedTime = endTime - startTime
	print(colourWhite + "Modified " + str(filesModified) + " file extensions in " + str(elapsedTime) + " seconds")

def main():
	clearScreen()
	displayArt()
	print("Welcome to file-extension-modifier by Dan-Foord")
	input("DISCLAIMER: This tool is limited to modifying file extensions in a given directory\nIt does not convert the contents of the file and it does not work within subdirectories or symlinks\nPress enter to continue")

	clearScreen()
	
	while True:
		inputDirectory = input("Please enter the path of the directory in which you would like to modify the file extensions\nLeave blank to execute the script in the current working directory\n")
		if os.path.isdir(inputDirectory):
			break
		elif inputDirectory == "":
			inputDirectory = os.getcwd()
			break
		else:
			print("Invalid path, please try again")
			clearScreen()

	clearScreen()

	while True:
		inputOldExtension = input("Please enter the file extension that you would like to change from, e.g. .txt\nLeave blank if the files that you want to modify have no file extension\n")
		if inputOldExtension[0:1] == ".":
			break
		elif inputOldExtension == "":
			break
		else:
			clearScreen()
			print("Invalid file extension, please try again")
	
	clearScreen()
	
	while True:
		inputNewExtension = input("Please enter the file extension that you would like to change to, e.g. .asc\nLeave blank to remove the file extension altogether\n")
		if inputNewExtension[0:1] == ".":
			break
		elif inputNewExtension == "":
			break
		else:
			clearScreen()
			print("Invalid file extension, please try again")
	
	clearScreen()

	input("Changing files in " + inputDirectory + " from " + inputOldExtension + " to " + inputNewExtension + ". Press enter to continue.")
	fileModification(inputDirectory, inputOldExtension, inputNewExtension)

if __name__ == "__main__":
    main()