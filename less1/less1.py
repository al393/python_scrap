import requests


def test():
    url = "https://www.google.ru"
    headers = {

    }
    res = requests.get(url, headers=headers)
    print(res)


if __name__ == '__main__':
    test()

