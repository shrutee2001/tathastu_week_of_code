tup=(10,10,5,2,1,0,5,6,3,2,4,10,1,9)
print("Choose elements from given tuple",tup)

def count(tup,num): 
	return tup.count(num)


enq=int(input("Enter first element "))
enq1=int(input("Enter second element "))
enq2=int(input("Enter third element "))

print(enq ,"occur",count(tup,enq),"times")
print(enq1 ,"occur",count(tup,enq1),"times")
print(enq2 ,"occur",count(tup,enq2),"times")	
