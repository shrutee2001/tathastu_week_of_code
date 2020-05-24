#Check for Even or odd
def Iseven(num):
    if num%2==0:
        return True
    return False
    
#check for prime
def IsPrime(N): 

    a=2
    k=N//2
    while k>=a:
	    if N%a==0: 
		    return False 
      a+=1
	  k=N//a
    return True 

#check for Palindrome
def IsPalindrome(n): 
	N=str(n)
	L=len(N)
	for i in range (L//2):
		if N[i]!=N[L-1-i]: 
		    return False
	return True

#check for Armstrong
def	IsArmstrong(num): 
    sum=0
    temp=num
    while temp>0: 
        digit=temp%10
    	  sum+=digit**3
    	  temp//=10
    if num==sum: 
        return True
    return False    	



def check():
	X=int(input("Enter the number:"))
	if(Iseven(X)):
		print(X,"is an even number")
	else:
	    print(X,"is an odd number")	
	if(IsPrime(X)):
	    print(X,"is a Prime number")  
	if(IsPalindrome(X)):
    	    print(X,"is a Palindrome number")  
	if(IsArmstrong(X)): 
	    print(X,"is an armstrong number") 



check()	    
