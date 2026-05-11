from flask import Flask

app = Flask(__name__)

@app.route("/app-homepage")
def hello_world():
    return """<!DOCTYPE html>
<html>
<head>
    <title>My Test Page</title>
</head>
<body>

<h1>Hello World!</h1>
<p>If you can see this, your HTML file is working. 🎉</p>

<button onclick="alert('Button works!')">Click Me</button>

</body>
</html>"""