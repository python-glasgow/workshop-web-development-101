import requests


def do_request():
    r = requests.post(
        "http://127.0.0.1:5001",
        json={"car": "ford"}
    )
    print(r.json())


if __name__ == '__main__':
    do_request()
