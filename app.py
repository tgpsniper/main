from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def Index():
  return render_template('index.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/enrollment_form')
def enrollment_form():
  return render_template('enrollment_form.html')

@app.route('/history')
def history():
  return render_template('schHistory.html')

@app.route('/mission')
def mission():
  return render_template('schMission.html')

@app.route('/vision')
def vision():
  return render_template('schVision.html')

# @app.route('/enrollment_form')
# def enrollment_form():
#   return render_template('enrollment_form.html')

if __name__ == "__main__":
    app.run(debug=True)