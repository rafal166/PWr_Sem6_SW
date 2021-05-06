import operator as op
operators={'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

running = True

print("Kalkulator RPN. Aby zakonczyć podaj znak \"q\"")

while running:
	stack = []
	print("Podaj dane:")
	data = input()
	
	if data.find('q') != -1:
		running = False
		continue

	if len(data) < 5:
		print("Podano nieprawidłowe dane")
		continue

	for item in data.split(" "):
		if item in operators:
			res = operators[item](stack.pop(),stack.pop())
		else:
			res = float(item)
		
		stack.append(res)
	
	if len(stack) == 1:
		print(stack.pop())

print("Koniec programu")