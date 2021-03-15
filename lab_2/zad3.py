numbers = [9,9,9,19,19,1,1,1,0,4,3,2,5,2]

index = 0;
num = numbers[index]

for i in range(len(numbers)-1):
	if numbers[i] < num:
		num = numbers[i]
		index = i

print("Najmniejsza liczba", num)
print("Pozycja", index)