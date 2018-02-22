minimunDimensions = int(input())
photos = int(input())

for _ in range(photos):
	width, height = map(int, input().split())
	
	if ((width < minimunDimensions) or (height < minimunDimensions)):
		print("UPLOAD ANOTHER")
		continue
	
	elif (width == height):
		print("ACCEPTED")
		continue
	
	print("CROP IT")