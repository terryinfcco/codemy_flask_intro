from flask import Flask, render_template

# Create the app
app = Flask(__name__)

# Set a route
@app.route('/')
def index():
    return render_template("index.html")

# Code from the Corey Schaefer series. Codemy windows code doesn't seem to work for me.
if __name__ == '__main__':
    app.run(debug=True)