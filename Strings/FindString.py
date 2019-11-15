from collections import Counter

# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.
# Example: ABCBCBA, Substring: BCB output: 2


def countSubstring(word, substring):
	#list comprehension
	# x: x = slice the word and store it in a dictionary
	# for x = this is to query the string in the dictionary
	total = Counter([word[x : x + len(substring)] for x in range(len(word))])
	return total[substring]
word = input('Enter a word: ')
sub = input('Enter Substring: ')
print(countSubstring(word, sub))

