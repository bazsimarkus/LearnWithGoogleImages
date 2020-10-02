from googleapiclient.discovery import build
from googleApiCredentials import *

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(searchType="image", q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']