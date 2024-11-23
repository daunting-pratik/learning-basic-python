list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,8,8,8,8,8,8,8,]

#add value to last of the list
list.append(63)

#inster at a certain postion
list.insert(0,50) #positon 0 and value 1 will be inserted

#remove the value from the list
list.remove(3) #value 3 will be removed from the list
print(list)

#remove last value from the list
list.pop()

# find the postion of the value in the list
print(list.index(8))



#checking weather the value is in the list or not
print(8 in list) # output will be True
print(1 in list)   # output will be False



#count the number of times the value is in the list
print(list.count(8)) #will count the number of times 8 is in the list




#shorting the list acending order
list.sort()
print(list)

#shorting the list decending order
list.reverse()
print(list)
#empty the list
list.clear()



print(list)
