import requests

from headers import headers


# TODO 用于下载code
def download(code_massage, competition_massage):
    # TODO 获得 codes_id
    code_id = code_massage[0]

    # TODO 获得 codes_title
    code_name = code_massage[1]

    # TODO 获得 codes_votes
    code_votes = code_massage[2]

    # TODO 获得 codes_title
    code_title = code_massage[3]

    # TODO 获得 competition_name
    competition_name = competition_massage[1]

    # TODO 获取下载链接
    download_url = "https://www.kaggle.com/kernels/scriptcontent/" + f"{code_id}" + "/download"

    # TODO 获取headers
    download_headers = headers()

    # TODO 通过get请求获取数据
    download_response = requests.get(download_url, headers=download_headers)

    # TODO 准备写入数据的路径
    with open(f"wjh_crawlsers/data/crawlers_data/{competition_name}/codes/{code_name}_点赞_{code_votes}.ipynb", "wb+") as f:
        # TODO 写入数据
        f.write(download_response.content)

    # TODO 用 正则表达 匹配 定义文件 是否在 check.txt 中
    with open('wjh_crawlsers/data/check.txt', 'a+') as first_check_download:
        first_check_download.write(f"{competition_name}/{code_name}\n")

    # TODO 输出提示
    print('--' * 30)
    print(f"{code_title}" + " download success!")
    print('--' * 30)
