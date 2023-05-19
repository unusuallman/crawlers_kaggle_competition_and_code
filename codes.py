import json

import requests

from headers import headers


def code(competition_massage):
    # TODO 获取 competition_id
    competition_id = competition_massage[0]

    # TODO 获取代码的 API链接
    code_url = "https://www.kaggle.com/api/i/kernels.KernelsService/ListCompetitionKernels"

    # TODO 获取 headers
    code_headers = headers()

    # TODO data 中的参数来源于网页 无需更改
    data = {
        "listKernelsRequest": {
            "kernelFilterCriteria": {
                "search": "",
                "listRequest": {
                    "competitionId": f'{competition_id}',
                    "sortBy": "VOTE_COUNT",
                    "pageSize": 5,
                    "group": "EVERYONE",
                    "page": 1,
                    "modelInstanceIds": [],
                    "excludeKernelIds": [],
                    "tagIds": "",
                    "excludeResultsFilesOutputs": False,
                    "wantOutputFiles": False
                }
            },
            "detailFilterCriteria": {
                "deletedAccessBehavior": "RETURN_NOTHING",
                "unauthorizedAccessBehavior": "RETURN_NOTHING",
                "excludeResultsFilesOutputs": False,
                "wantOutputFiles": False, "kernelIds": [],
                "outputFileTypes": [],
                "includeInvalidDataSources": False
            }
        }
    }

    # TODO 将 字典 转换为 json格式
    code_data = json.dumps(data)

    # TODO 通过 post请求 获取数据
    code_response = requests.post(code_url, data=code_data, headers=code_headers)

    # TODO 将 json格式 转换为 字典
    code_list = json.loads(code_response.text)

    # TODO 为获取 code_message 的各项信息做预处理
    code_message = []

    # TODO 判断是否有 code 存在
    if code_list["unpinnedKernels"]:

        # TODO 从 list_code 中获取各类信息
        for i in code_list["unpinnedKernels"]["kernels"]:
            code_id = i["scriptVersionId"]  # ID
            code_votes = i["totalVotes"]  # 票数
            code_name = i["currentUrlSlug"]  # 参名
            code_title = i["title"]  # 标题
            code_message.append([code_id, code_name, code_votes, code_title])

    # TODO 返回信息列表
    return code_message
