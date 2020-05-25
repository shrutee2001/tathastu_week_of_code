#initializing tuple
test_tup = ([7,5,4],[8,4,2],[5,7,0])

#printing original tuple
print("The original tuple is : " +str(test_tup))

result=tuple((sorted(sub) for sub in test_tup))

#printing tuple after sorting
print("The tuple after sorting lists: " +str(result))
