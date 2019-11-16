#Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer .
# You have to print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to .
# Here, Input Format Four integers  and  each on four separate lines, respectively.
# Constraints
# Print the list in lexicographic increasing order.

x, y, z, n = (int(input()) for _ in range(4))
print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c !=n])
