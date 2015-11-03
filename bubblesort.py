import random


def randomlist(amount):
	for i in range(0,amount):
		print random.randint(0,100000)
		



def bubblesort(list):
	print(list)
	temp = 0
	for num in range (len(list)-1,0,-1):
		for i in range(num):
			if list[i] > list[i+1]:
				temp = list[i]
				list[i] = list[i+1]
				list[i+1] = temp

list =[3,1,5,6]
bubblesort(list)
print list

list2 =[6,5,3,1,8,7,2,4]
bubblesort(list2)
print list2 

randomlist(10)



	# temp =0 
	# if list[i] < list[i+1]:
	# 	pass
	# 	i += 1
	# elif list[i] > list[i+1]:
	# 	temp = 	list[i+1]
	# 	list[i+1] = list [i]
	# 	temp = list[i]
	# 	i += 1

	# print list	



	

	