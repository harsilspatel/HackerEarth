l, r, k = map(int, input().split())

if l%k != 0:
	minumumDivisibleInt = l - (l%k) + k
else:
	minumumDivisibleInt = l
	
maximumDivisibleInt = r - (r%k)
	
divisibleNumbers = ((maximumDivisibleInt - minumumDivisibleInt) / k) + 1
print(int(divisibleNumbers))