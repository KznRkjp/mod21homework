import requests

def count_words_at_url(url,word):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            count = 0
            for i in resp.text.split():
                if i.lower() == word.lower():
                    count+=1
            return count
    except requests.ConnectionError:
        return -1
