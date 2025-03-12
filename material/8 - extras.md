# Extras

## Redirecting

```Python
from flask import Flask, request, render_template, redirect, url_for

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)


def save_to_json(data):
    import json
    import pathlib

    cwd = pathlib.Path.cwd()
    jsond = cwd / "data.json"
    jsond.write_text(json.dumps(data))


@app.route('/form', methods=["GET", "POST"])
def form_route():
    if request.method == "GET":
        return render_template("form.html")

    if request.method == "POST":
        save_to_json(request.form)

        return redirect(url_for("form_route", data_saved=True))
```