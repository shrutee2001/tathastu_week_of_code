from itertools import permutations 

import string 

  

s =input('enter your string:')

a = string.ascii_letters 

p = permutations(s) 

d = []
for i in list(p): 
    if (i not in d): 

        d.append(i) 

        print(''.join(i))
