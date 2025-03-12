# Routes and static file routes

In the terminal, run the following:

```bash
flask --help
```

In the `Commands:` list you should see a command called `routes`

Run this command in the terminal:

```bash
flask routes
```

This will give you a list of the current routes you have registered, including
the static route that is automatically created if you define a static folder.
This can be disabled if you set `static_folder` to `None`

The Flask static route has protections around it to stop common
vulnerabilities around serving static files.

The function name below the decorator becomes the name for the endpoint
(you can change this, but it's not common to do)

```text
     [\/ Method]
@app.get("/")
def index [<-- Endpoint name] ():
    return "Hello, world!" [<-- Sent to client]
```

There's a couple of different ways to define a route in Flask, like using the
`.route()` method with `methods` as a keyword argument.

```Python
@app.route("/", methods=["GET", "POST"])
def my_example_route():
    ...
```

The alternative being:

```Python
@app.get("/")
def example_route__get():
    ...

@app.post("/")
def example_route__post():
    ...
```

Let's run the Flask server and visit a static file:

```bash
flask run --debug
```

Now visit the following link:

[http://127.0.0.1:5000/static/robot.gif](http://127.0.0.1:5000/static/robot.gif)

Notice that Flask prepends `/static/` to this route, this is to make it clear
that it is a static file. You can change this by changing the `static_url_path`
value in the flask instance:

```Python
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/static-files",
    template_folder="templates"
)
```

## Task 👷‍♂️

1. Try creating more routes in `app.py` and get familiar with using the
   `flask routes` command.