for _ in range(int(input())):
	x = (input().split())
	length = int(x[0])
	rotation = int(x[1])
	array = list(map(int, input().split()))
	i = (length - rotation) % length
	for _ in range(length):
		print(array[i], end = ' ')
		i = (i+1) % length
	print()