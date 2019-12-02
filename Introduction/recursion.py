def rec(a):
    if a == 0:
        return 1
    return rec(a-1) + (a-2)

def countWays(b):
    return rec(a + 1)

a = int(input('Enter a value: '))
listOfNo = [*range(a)]
print('Saved possible values in a list: ', listOfNo)
print('Number of ways to the stairs: ', countWays(listOfNo))
