import requests


NCT_API = "https://graph.nhaccuatui.com/api/v1/search/song"


def search_music(keyword, pagesize=10):

    params = {
        "keyword": keyword,
        "pageindex": "1",
        "pagesize": pagesize,
        "correct": "true",
    }

    response = requests.post(
        NCT_API,
        params=params
    )

    return response.json()
