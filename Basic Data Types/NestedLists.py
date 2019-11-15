matrix = []
matrix = [[j for j in range(5)] for i in range(5)]
# [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
# the first logic  in []  will count from 0 to 5 as the range is 5
# the second logic for for loop will create the nested list up to 5 list

print("This will print the Matrix", matrix)

#Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here,
#Input Format
#Four integers  and  each on four separate lines, respectively.
#Constraints
#Print the list in lexicographic increasing order.

#Sample input
#2 2 2 2

#Sample Output
#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

#print("Enter 4 integers")
#x, y, z, n = (int(input()) for _ in range(4))
#print("This will print the Hackerrank exercise on List Comprehension",
	  #[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c !=n])

e, f, g= (int(input())for _ in range(3))
print([[a,b]for a in range(e+1) for b in range(f+1) if e+f !=g])