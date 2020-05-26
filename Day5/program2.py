def Greatest(lst): 
	size=len(lst)

	max_from_right=lst[size-1]
	lst[size-1]= -1

	for i in range(size-2,-1,-1): 
		temp=lst[i]
		lst[i]=max_from_right

		if max_from_right<temp: 
			max_from_right=temp


def printlist(lst): 
    for i in range(0,len(lst)): 
        print(lst[i])


n=int(input("Enter number of elements: "))
lst=list(map(int,input("\nEnter the elements: ").strip().split()))[:n]
Greatest(lst)
print("Modified list is: ")
printlist(lst)        			
