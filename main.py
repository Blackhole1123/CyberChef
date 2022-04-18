from static.python.finalgetfunction  import finalgetfunction
import random
from static.python.finalgetfunction2 import finalgetfunction2
from flask import Flask, render_template, request, flash, redirect, session
from waitress import serve
from werkzeug.utils import secure_filename
import os

import static.python.get_restraunt

# Config
UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'heic', 'webm', 'tiff', 'svg', 'heif'}

app = Flask('app')
app.secret_key = 'qwsedfgre3w2efghbtr4erfghgtre4r'

# Functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routing
@app.errorhandler(404)
def e404(e):
  try:
    theme = session["theme"]
  except:
    session["theme"] = "styles.css"
    theme = "styles.css"
  return render_template("404.html", title = "You Got Lost", theme=theme+"?v="+str(random.randint(10000,99999)))
@app.errorhandler(500)
def e500(e):
  try:
    theme = session["theme"]
  except:
    session["theme"] = "styles.css"
    theme = "styles.css"
  return render_template("500.html", title="Website Down", theme=theme+"?v="+str(random.randint(10000,99999)))


@app.route('/')
def index():
  try:
    theme = session["theme"]
  except:
    session["theme"] = "styles.css"
    theme = "styles.css"
  return render_template('index.html', title="Home", theme=theme+"?v="+str(random.randint(10000,99999)))
@app.route('/about')
def tutorial():
  try:
    theme = session["theme"]
  except:
    session["theme"] = "styles.css"
    theme = "styles.css"
  return render_template('about.html', title="About", theme=theme+"?v="+str(random.randint(10000,99999)))


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file1' not in request.files:
            flash('No file part')
            return "Invalid File"
        file = request.files['file1']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "Invalid File"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            file = os.path.join(UPLOAD_FOLDER, filename)
            stringstuff = os.path.basename(file)
            return redirect("results/" + stringstuff)
        return "Invalid File"

@app.route('/2', methods=['POST'])
def upload_file2():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file1' not in request.files:
            flash('No file part')
            return "Invalid File"
        file = request.files['file1']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "Invalid File"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            file = os.path.join(UPLOAD_FOLDER, filename)
            stringstuff = os.path.basename(file)
            return redirect("results2/" + stringstuff)
        return "Invalid File"


@app.route("/results/<filename>")
def results(filename):
  try:
    theme = session["theme"]
  except:
    session["theme"] = "styles.css"
    theme = "styles.css"
  results = finalgetfunction(filename)
  return render_template('results.html', recipies=results, title="Get Recipe based on Ingredients", theme=theme+"?v="+str(random.randint(10000,99999)))

@app.route("/results2/<filename>")
def results2(filename):
  try:
    theme = session["theme"]
  except:
    session["theme"] = "styles.css"
    theme = "styles.css"
  results = finalgetfunction2(filename)
  return render_template('results.html', recipies=results, title="Get Recipe based on Pictures", theme=theme+"?v="+str(random.randint(10000,99999)))

@app.route("/settings")
def settings():
  try:
    theme = session["theme"]
  except:
    session["theme"] = "styles.css"
    theme = "styles.css"
  return render_template("settings.html", title="Settings", theme=theme+"?v="+str(random.randint(10000,99999)))

@app.route("/settings")
def profile():
  try:
    theme = session["theme"]
  except:
    session["theme"] = "styles.css"
    theme = "styles.css"
  return render_template("profile.html", title="Settings", theme=theme+"?v="+str(random.randint(10000,99999)))
@app.route("/changeTheme")
def changeTheme():
  if (request.args.get("t") == "l"):
    session["theme"] = "styles.css"
    return ""
  else:
    session["theme"] = "dark.css"
    return  ""
serve(app, host='0.0.0.0', port=8080) 