# templates and endpoints

Edit `app.py` to look like the following:

```Python
from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)


@app.get("/")
def index():
    return render_template("default.html")

```

Now run the Flask application, and visit the page.

Rendering a template runs the html file through the Jinja template engine.
Flask creates a Jinja environment when creating the Flask instance.

This Jinja environment has access to various resources from Flask. 
These resources are called the standard context. 

It includes the Flask `config`, the request,
an object called `g` that's able to globally pass values around request context 
(don't worry about this too much just now), `session` (cookies), 
the `url_for()` function and the `get_flashed_messages()` function.

Let's add the css file and robot gif to the `default.html` template using the
`url_for()` function

Edit `default.html` to look like the following:

```Jinja2
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic HTML Page</title>

    <link rel="stylesheet" href="{{ url_for('static', filename='main.css') }}">

</head>
<body>
    <header>
        <h1>Welcome to My Basic HTML Page</h1>
    </header>
    <main>
        <p class="custom-css">
            This is a simple HTML page example with a header, main content, and a footer.
        </p>
        <img src="{{ url_for('static', filename='robot.gif') }}" alt="robot"/>
    </main>
    <footer>
        <p>&copy; 2023 Your Name. All rights reserved.</p>
    </footer>
</body>
</html>

```

The `url_for()` function isn't only used for static files in templates. You
can get the url for any registered endpoint, for example:

```Python
from flask import Flask, url_for

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

@app.get("/this/is/a/long/url/path/that/i/may/change/later")
def my_route():
    return "This is a long url path that I may change later"

@app.get("/")
def index():
    return url_for("my_route")
```

In the example above visiting index will return the url path for the 
`my_route()` function, or endpoint is how it's being defined.
