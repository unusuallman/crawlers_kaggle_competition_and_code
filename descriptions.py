import json

import requests

from headers import headers


# TODO 用于获取比赛的名称
def description(competition_massage):
    # TODO 获得 competition_name
    competition_name = competition_massage[1]

    # TODO 获取比赛的描述
    description_url = "https://www.kaggle.com/api/i/competitions.legacy.LegacyCompetitionService/GetCompetition"

    # TODO 获取headers
    description_headers = headers()

    # TODO 获取每一个 competition 的 id
    data = {"competitionIdOrName": f"{competition_name}"}

    # TODO 将字典转换为json格式
    description_data = json.dumps(data)

    # TODO 通过post请求获取数据
    description_response = requests.post(description_url, data=description_data, headers=description_headers)

    # TODO 将json格式转换为 list
    description_list = json.loads(description_response.text)

    # TODO 获取 description
    for content in description_list["pages"]:

        # TODO 准备写入数据的路径
        with open(f"wjh_crawlsers/data/crawlers_data/{competition_name}/项目描述.txt", "ab+") as f:

            # TODO 写入数据
            f.write(content["content"].encode("utf-8"))

    # TODO 输出提示
    print(f'{competition_name} 项目描述已写入!')
    print('--' * 30)
