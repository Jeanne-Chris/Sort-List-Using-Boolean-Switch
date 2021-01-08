# We usually do the sorting of one type list like...
numList = [7894, 4304, 9084, 0, 7844, 9893, 1545, 2000, 8943, 42, 332, 9, 10]
numList.sort()
print("numList: ", numList)

# It is also possible to sort a list through a boolean switch and iteration testing of values
# and return the same result.
newLst = [7894, 4304, 9084, 0, 7844, 9893, 1545, 2000, 8943, 42, 332, 9, 10]
switch = True

while switch:
	switch = False
	for i in range(len(newLst) - 1):
		if newLst[i] > newLst[i + 1]:
			switch = True
			newLst[i], newLst[i + 1] = newLst[i + 1], newLst[i]

print("newList: ", newLst)

