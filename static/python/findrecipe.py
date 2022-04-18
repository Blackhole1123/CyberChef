import requests
import json

def findrecipe(ingredientlist):
	ingredientstring=''
	ingredientstring += ingredientlist[0]
	for ingredient in ingredientlist:
		if ingredient == ingredientlist[0]:
			continue;
		ingredientstring += ','
		ingredientstring+=ingredient
	PARAMS = {'ingredients':ingredientstring, 'number':9, "limitLicense":True,
	"ranking": 1, "ignorePantry": False}
	api_key = "29ade52775f44a26a6b1e00601ba97b5"
	response = requests.get(f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}", params=PARAMS)
	return response.json()
