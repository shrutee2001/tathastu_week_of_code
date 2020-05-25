def charcount(word): 
	dict={}
	for i in word: 
		dict[i]=dict.get(i,0)+1
	return dict	



def words_generated(lwords,charset): 
	for word in lwords:
		k=1
		char=charcount(word)
		for key in char: 
			if key not in charset: 
				k=0
			else: 
			    if charset.count(key)!=char[key]: 
			    	k=0
		if k==1: 
		    print(word)	    	



if __name__ == "__main__": 
	input=['go','bat','me','eat','goal','boy','run']
	charset=['e','o','b','a','m','g','l']
	words_generated(input,charset)
  
  
  
 
