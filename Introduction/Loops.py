#Read an integer N. For all non-negative integers , print N. See the sample for details.
#Sample Input 5
#Sample Output
#0
#1
#4
#9
#16

print("Enter an integer ")
n = int(input())
for i in range(n):
	print(int(i**2))