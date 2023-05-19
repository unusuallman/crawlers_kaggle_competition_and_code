import re

import requests


def headers():
    # TODO 获得cookies的更新
    session = requests.session()
    cookies_dict = session.get("https://www.kaggle.com").cookies.get_dict()
    cookies_dict["ACCEPTED_COOKIES"] = "true"
    cookies_str = ""
    for key, value in cookies_dict.items():
        cookies_str += key + "=" + value + ";"

    # TODO 用正则表达式提取 cookie 中的 XSRF-TOKEN
    token = re.findall(r'XSRF-TOKEN=(.*?);', cookies_str)[0]

    # TODO 组成 headers
    herders = {
        "keep-alive": "false",
        "cookie": f"{cookies_str}",
        "x-xsrf-token": f"{token}",
    }
    return herders
