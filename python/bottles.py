
allBottles = 10

for num in range(allBottles):
	bottles  = allBottles - num
	print(bottles, "green bottles hanging on the wall,")
	print(bottles, "green bottles hanging on the wall,")
	print("and if one green bottle should accidentally fall,")
	print("they'll be", bottles-1, "green bottles hanging on the wall.")
	print()
	bottles = bottles - 1

print('All gone')