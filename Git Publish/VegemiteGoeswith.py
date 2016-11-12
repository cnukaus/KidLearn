# todo 1:save and read dict1 from text file so it remembers
#2:update with length of dict1 later

import random
def find_combination_with(food='vegimite'):

	dict1={1:"toast", 2:"shouting", 3:"workfood",4:"sushi"}
	i=random.randint(1,4) 
	print 'today's recommendation: "+dict1[i]+' with '+food

find_combination_with()