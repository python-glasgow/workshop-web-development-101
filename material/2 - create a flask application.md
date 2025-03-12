# Create a Flask application

Copy the following into `app.py`

```Python
from flask import Flask

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)


@app.get("/")
def index():
    return "Hello, world!"
```

Let's start the Flask application.

Flask will automatically look for a Flask instance in either a package called 
`app`, or a module called `app.py` when starting Flask from the terminal.

In the terminal, run:
```bash
flask run --debug
```

Now visit the link shown in the terminal.

To close the Flask application hold the `control` key then press `c`

**Extra development server options:**

Change the port:

```bash
flask run --port 7070 --debug
```

Change the app to run from `app_2.py`:

```bash
flask --app app_2 run --port 7070 --debug
```

Let others connect to your server (do not use in production):

```bash
flask run --port 7070 --host 0.0.0.0 --debug
```

For a complete guide on using the CLI, see:

https://flask.palletsprojects.com/en/stable/cli/
