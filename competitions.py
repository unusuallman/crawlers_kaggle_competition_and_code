import json

import requests

from headers import headers


def competition(page):
    # TODO 用于获取比赛的名称
    competition_url = "https://www.kaggle.com/api/i/competitions.CompetitionService/ListCompetitions"

    # TODO 获取 headers
    competition_headers = headers()

    # TODO data 中的参数来源于网页 无需更改
    date = {
        "selector": {
            "competitionIds": [],
            "listOption": "LIST_OPTION_DEFAULT",
            "sortOption": "SORT_OPTION_NEWEST",
            "hostSegmentIdFilter": 0,
            "searchQuery": "",
            "prestigeFilter": "PRESTIGE_FILTER_UNSPECIFIED",
            "participationFilter": "PARTICIPATION_FILTER_UNSPECIFIED",
            "tagIds": [],
            "requireSimulations": False,
            "requireKernels": False,
        },
        "pageToken": f"{page}",
        "pageSize": 20,
        "readMask": "competitions,totalResults"
    }

    # TODO 将 字典 转换为 json格式
    competition_data = json.dumps(date)

    # TODO 通过 post请求 获取数据
    competition_response = requests.post(competition_url, data=competition_data, headers=competition_headers)

    # TODO 将 json格式 转换为字典
    competition_list = json.loads(competition_response.text)

    # TODO 为获取 competition_message 的各项信息做预处理
    competition_message = []

    # TODO 获取 competition_message 的 id 和 name
    for i in competition_list["competitions"]:
        competition_id = i["id"]
        competition_name = i["competitionName"]  # 规范化的
        competition_title = i["title"]  # 不规范的
        competition_message.append([competition_id, competition_name, competition_title])

    # TODO 返回参数list
    return competition_message
