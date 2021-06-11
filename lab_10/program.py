print('Program sprawdzający czy podany ciąg znaków jest palindromem. ')

while True:
	data = input('Podaj dane do sprawdzenia: ')
	data = data.replace(' ','')
	dataToCheck = data[::-1]
	if data == dataToCheck:
		print('Palindrom!')
	else:
		print('Nie palindrom!')
