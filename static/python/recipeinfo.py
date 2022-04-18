import requests
import json

class NoMorePointsError(Exception):
  pass

def recipeinfo(id):
  recipeinfo = []
  PARAMS = {"id": id, "includeNutrition": False}
  api_key = "29ade52775f44a26a6b1e00601ba97b5"
  response = requests.get(f"https://api.spoonacular.com/recipes/{id}/information?apiKey={api_key}", params=PARAMS)
  jsonresponse = response.json()
  try:
    recipeinfo.append(jsonresponse["title"])
  except:
    raise NoMorePointsError("You have used up all of your 150 points.")
  with open("a.json","w") as a:
    json.dump(jsonresponse, a, indent=4)
  recipeinfo.append(jsonresponse["image"])
  recipeinfo.append(jsonresponse["sourceUrl"])
  recipeinfo.append(jsonresponse["readyInMinutes"])
  recipeinfo.append(jsonresponse["servings"])
  recipeinfo.append(jsonresponse["instructions"])
  recipeinfo.append(jsonresponse["summary"])
  recipeinfo.append(jsonresponse["vegetarian"])
  recipeinfo.append(jsonresponse["vegan"])
  recipeinfo.append(jsonresponse["glutenFree"])
  recipeinfo.append(jsonresponse["dairyFree"])
  recipeinfo.append(jsonresponse["veryHealthy"])
  recipeinfo.append(jsonresponse["cheap"])
  recipeinfo.append(jsonresponse["veryPopular"])
  print("sustainable" in jsonresponse.keys())
  bad = False
  try:
    recipeinfo.append(jsonresponse["sustatainable"])
  except:
    bad = True
  if bad:
    recipeinfo.append(False)
  
  #print(recipeinfo)
  return recipeinfo 