import wikipedia

def wiki():
  a = (wikipedia.summary("sushi food").split(".")[0:5])
  string = ""
  for i in a:
    string += i
    string += "."
  string +=".."
  return string

