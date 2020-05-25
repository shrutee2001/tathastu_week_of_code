#Using Frozensets
my_dict=[{'Mango':5},{'Grapes':4},{'Mango':5},{'Apple':3}]
print('Original list : '+str(my_dict))
final_lst={frozenset(item.items()) : item for item in my_dict}.values()
print("Resultant list is: "+str(final_lst))
