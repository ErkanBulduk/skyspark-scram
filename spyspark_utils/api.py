import requests
import urllib3
import requests
import spyspark_utils.utils as utils
urllib3.disable_warnings()

def readByFilter(url, token, project, filter, limit:int = None, contentType=None):
    """
    Request Read by filter: "https://skyfoundry.com/doc/docHaystack/Filters"
        • filter: Filter name
        • limit: optional Number that specifies maximum number of entities to return in response
    """
    _headers = {
        "authorization": f'BEARER authToken={token}',
    }
    _headers["accept"] = utils.checkContentType(contentType)
    _url = f"{url}/api/{project}/read"
    _param = { "filter": filter}
    if limit: _param["limit"] = limit
    req = requests.get(
        _url,
        headers=_headers,
        verify=False,
        params=_param
    )
    return req.content

def readByID(url, token, project, id, contentType=None):
    """
    Request Read by id:
        • id: a Ref identifier
    """
    _headers = {
        "authorization": f'BEARER authToken={token}',
    }
    _headers["accept"] = utils.checkContentType(contentType)
    _url = f"{url}/api/{project}/read"
    _param = { "id": id }
    req = requests.get(
        _url,
        headers=_headers,
        verify=False,
        params=_param
    )
    return req.content

def hisRead(url, token, project, id, range, contentType=None):
    """
    id: Ref identifier of historized point
    range: Str encoding of a date-time range
    """
    _headers = {
        "authorization": f'BEARER authToken={token}',
    }
    _headers["accept"] = utils.checkContentType(contentType)
    _url = f"{url}/api/{project}/hisRead"
    _range = utils.datetime_toZinc(range)
    req = requests.get(
        _url,
        headers=_headers,
        verify=False,
        params={
            "id": id,
            "range": _range,
        }
    )
    return req.content