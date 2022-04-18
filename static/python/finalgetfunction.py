from static.python.check_food import check_food
from static.python.findrecipe import findrecipe
from static.python.recipeinfo import recipeinfo

def finalgetfunction(filename):
	tags = check_food(filename)
	jsonstuff = findrecipe(tags)
	print(jsonstuff)
	i = 0
	bigreturnlist = []
	#print("here")  
	while i < 9:
		returnlist = recipeinfo(jsonstuff[i]["id"])
		#print("here")
		bigreturnlist.append(returnlist)
		i += 1
	return bigreturnlist

#print(finalgetfunction("applesbanas.jpeg"))