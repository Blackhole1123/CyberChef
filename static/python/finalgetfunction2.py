from static.python.check_food import check_food
from static.python.findrecipe import findrecipe
from static.python.recipeinfo import recipeinfo

def finalgetfunction2(filename):
	tags = check_food(filename)
	jsonstuff = findrecipe(tags)
	#print(jsonstuff)
	i = 0
	bigreturnlist = []
	#print("here")
	while i < 2:
		returnlist = recipeinfo(jsonstuff[i]["id"])
		#print("here")
		bigreturnlist.append(returnlist)
		i += 1
	return bigreturnlist
