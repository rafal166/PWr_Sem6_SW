def count_characters(text):
	countRes = {};
	for character in text:
		if not character in countRes :
			countRes[character] = 0
		countRes[character] += 1
	return countRes

# zad 1
text = input("Podaj tekst do przeliczenia:")
print(count_characters(text))