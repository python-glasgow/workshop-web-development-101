# Passing around values

## Passing values to the template

Any keyword argument passed after the template name will be available in
the template.

Add the following route into `app.py`

```python
@app.get('/values-to-template')
def pass_to_template():
    stringv = "value"
    intv = 1
    floatv = 1.1
    boolv = True
    listv = ["value1", "value2", "value3"]
    dictv = {"key1": "value1", "key2": "value2", "key3": "value3"}

    return render_template(
        "values.html",
        stringv=stringv,
        intv=intv,
        floatv=floatv,
        boolv=boolv,
        listv=listv,
        dictv=dictv,
        )
```

## Getting a value from the URL path

Add the following route into `app.py`

```python
@app.get('/path/value/<my_value>')
def get_from_path(my_value):
    return f"The value you passed from the URL is: {my_value}"
```

Flask will parse out the values from the URL and pass them in the same order
to the function. The names must also be the same.

Here's an example of two values in the URL path:

```python
@app.get('/path/value/<first_value>/<next_value>')
def get_from_path(first_value, next_value):
    return f"1st: {first_value}, Next: {next_value}"
```

## Getting values from URL args

URL args are defined after the path, like so `/args?name=David`

`?` is always used to show the start of URL args. `&` is used to add more, 
like so:

`/args?name=David&using=flask&likes=cheesecake`

Add the following to the top of `app.py`

```Python
from flask import request
```

Now add the following route:

```Python
@app.get('/args')
def get_from_url_args():
    all_url_args = request.args

    if request.args.get('name'):
        return f"Hello, {request.args.get('name')}! <br> {all_url_args}"

    return f"all_url_args: {all_url_args}"
```

As you can see `request.args` is based on the dictionary type, which means
you can use the `.get()` method.

So, as an example you can think of the following:

`/args?category=cheesecake&flavour=vanilla&page=2`

as:

```Python
request.args = {
    "category": "cheesecake",
    "flavour": "vanilla",
    "page": "2"
}
# this would be an example of getting the page, but if the
# 'page' is not found it sets the default to "1"
page = request.args.get("page", "1")
```

## Getting values from a form

In this example we will need to create a route that accepts a POST request.

Ensure that `request` is being imported from `flask`

```Python
from flask import request
```

Add the following route:

```Python
@app.route('/form', methods=["GET", "POST"])
def form_route():
    if request.method == "GET":
        return render_template("form.html")

    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        return render_template(
            "form_values.html", 
            first_name=first_name, 
            last_name=last_name
        )

    return "error"
```

Visiting the `/form` route you'll be able to send data from the html form to
the same route.
