def convert(num): 
	
	if (num==0): 
		return 0 
	
	digit=num%10

	if (digit==0): 
	    digit=5

	return (convert(int(num/10))*10+digit)  	



num=int(input('Enter integer value: '))
print(convert(num))           


