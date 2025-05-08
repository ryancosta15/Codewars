def remove_every_other(my_list):
	l = int(len(my_list))
	for x in range(0,l//2):
		my_list.pop(x+1)
	return my_list
