#Read an integer N.
#Without using any string methods, try to print the following:
#123...N Note that "N" represents the values in between.


print("Enter an integer")
n = int(input())
for i in range(n):
	print(i+1, end=' ')