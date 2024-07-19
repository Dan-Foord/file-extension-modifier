import os

filesModified = 0
for name in os.listdir():
	if name == "conversion.py":
		print("Skipped python script rename")
	else:
		os.rename(name, name + ".jpg")
		print("Modified name of " + name)
		filesModified = filesModified + 1
print("Modified " + str(filesModified) + " files to .jpg format")
