import requests

def count_words_at_url(url,word):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            count = 0
            for i in resp.text.split():
                if i.lower() == word.lower():
                    count+=1
            return count
    except requests.ConnectionError:
        return -1
