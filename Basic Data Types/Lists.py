#List Comprehension
#basic syntax is [ expression for item in list if conditional ]
#equivalent to
# for item in list:
    # if conditional:
        # expression
# https://www.pythonforbeginners.com/basics/list-comprehensions-in-python

listOfWords = ["this","is","a","list","of","words"]
items = [word for word in listOfWords]
print(items) #print the list
print(' '.join(items)) #print and join all of the string in one sentence. split it  with space


#Nested Lists
matrix = []
matrix = [[j for j in range(5)] for i in range(5)]
 #[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
 # the first logic  in []  will count from 0 to 5 as the range is 5
 # the second logic for for loop will create the nested list up to 5 list
print("Nested Lists")
print(matrix)

