from collections import Counter 

votes=['selena','camila','taylor','taylor','selena','taylor','taylor','lipa','lipa','lipa','selena','lipa','camila']
vote_count=Counter(votes)
max_votes=max(vote_count.values())
lst=[i for i in vote_count.keys() if vote_count[i]==max_votes]
print(sorted(lst)[0])
