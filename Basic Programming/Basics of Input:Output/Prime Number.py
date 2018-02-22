import math
inputInt = int(input())
primeNumbers = []
isPrime = True

for dividend in range(2, inputInt + 1):
	isPrime = True
	for divisor in range(2, int(math.sqrt(dividend)+1)):
		if (dividend % divisor == 0):
			isPrime = False
			break
		
	if (isPrime == True):
		primeNumbers.append(dividend)

print(*primeNumbers)