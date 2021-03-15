import os
import sys

def count_characters(text):
	countRes = {};
	for character in text:
		if not character in countRes :
			countRes[character] = 0
		countRes[character] += 1
	return countRes

f = open(os.path.join(sys.path[0], "demofile.txt"), "r")
textFromFile = f.read()
print(textFromFile)

print(count_characters(textFromFile))