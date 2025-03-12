# Working with JSON

## Responding with JSON

Add the following route to `app.py`

```Python
@app.get('/stock')
def stock():
    return [
        {
            "item_code": 9808798,
            "item": "Wacky inflatable man",
            "stock": 16
        },
        {
            "item_code": 5786876,
            "item": "Cheesecake Vanilla",
            "stock": 4
        },
    ]
```

Since Flask 1.1, any value returned from a route that's either a list, or a
dictionary will be parsed as JSON and sent as a JSON response.

Here's an example of returning a dictionary:

```Python
@app.get('/player')
def player():
    return {
        "name": "Gandalf",
        "class": "Wizard"
    }
```

