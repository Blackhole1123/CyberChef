import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./festive-freedom-309323-0124a1c976ae.json"
from google.cloud import vision
def check_food(filename):
  os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./festive-freedom-309323-0124a1c976ae.json"
  from google.cloud import vision

  client = vision.ImageAnnotatorClient()
  path = "./static/images/" + filename
  file_name = os.path.abspath(path)
  # Loads the image into memory
  with io.open(file_name, 'rb') as image_file:
      content = image_file.read()
  image = vision.Image(content=content)
  #General
  response = client.label_detection(image=image)
  general_list = []
  labels = response.label_annotations
  objects = client.object_localization(
        image=image).localized_object_annotations
  response = client.text_detection(image=image)
  texts = response.text_annotations
  
  for text in texts:
    #print("here")
    general_list.append(text.description)

  for object in objects:
    general_list.append(object.name)
  i = 0
  for label in labels:
    general_list.append(label.description)
    if i > len(objects) and i > 2:
        break
    else:
        i += 1

  
  #print(general_list)
  return general_list

#check_food("applesbanas.jpeg")
  
