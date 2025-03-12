# Extending and including

Add the following route:

```Python
@app.get("/part")
def part():
    return render_template("part.html")
```

Open the `part.html` file in the `templates` folder.

The `part.html` file extends from `main.html`, it uses a content block
to replace the information found in the content block with the same name
in `main.html`

Open the `main.html` file in the `templates/extend` folder.
