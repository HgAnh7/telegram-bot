import requests


NCT_API = "https://graph.nhaccuatui.com/api/v1/search/song"
TIMEOUT = 10

def search_music(keyword, pagesize=10):

    params = {
        "keyword": keyword,
        "pageindex": "1",
        "pagesize": pagesize,
        "correct": "true",
    }

    try:
        response = requests.post(
            NCT_API,
            params=params,
            timeout=TIMEOUT
        )
        
        return response.json()
    except:
        return None
