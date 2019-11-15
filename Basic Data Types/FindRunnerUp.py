#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
arr = list(map(int, input('Enter values').split()))
listnew=[]
for i in arr:
         if i not in listnew:
            listnew.append(i)
print(listnew)#displays all the entered values before sorting
listnew.sort(reverse=True) #this will sort by reverse
print(listnew) #displays the newly sorted values
print('First Runner up is ', listnew[0])
print('Second Runner up is ', listnew[1]) #this will determine the second highest number
print('Last place is ', listnew[-1])
