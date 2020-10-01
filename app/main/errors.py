from flask import flask, render_template

app = flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")
    
@app.errorhandler(404)
def not_found(e):
  return render_template('customerror_page.html'), 404

# repaet to handle 403 401 etc................................................