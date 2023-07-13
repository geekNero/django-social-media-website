import httpx
import urllib
from fake_useragent import UserAgent


def fetch_images(request_list: list) -> list:
    user_agent = UserAgent()
    headers = {'User-Agent': str(user_agent)}
    image_list = []
    with httpx.Client(headers=headers) as client:
        for req in request_list:
            per_page = 1
            page = req[1]
            parameter = {"query": req[0], "per_page": per_page, "page": page}
            query = urllib.parse.urlencode(parameter)
            url = f"https://unsplash.com/napi/search/photos?{query}"
            response = client.get(url)
            try:
                response.raise_for_status()
            except Exception as e:
                return e
            response = response.json()
            if len(response['results']) > 0:
                for i in range(len(response['results'])):
                    image_list.append({
                        "url": response['results'][i]['urls']['raw'],
                       "desc": response['results'][i]['description'],
                        "hashtag": req[0]
                       })
    return image_list
