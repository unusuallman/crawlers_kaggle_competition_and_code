import os
import re
from deletes import delete_files


def conversion(code_massage, competition_massage):
    # TODO 获得 codes_title
    code_name = code_massage[1]

    # TODO 获得 competition_name
    competition_name = competition_massage[1]

    # TODO 获得 codes_votes
    code_votes = code_massage[2]

    # TODO 获得 codes_title
    code_title = code_massage[3]

    # TODO 获得 conversion_path
    conversion_path = f"wjh_crawlsers/data/crawlers_data/{competition_name}/codes/{code_name}_点赞_{code_votes}.ipynb"

    # TODO 通过 终端指令 转换文件 并获取输出
    command_out = os.system(f"jupyter nbconvert --to script {conversion_path}")

    # TODO 如果转换不成功
    if command_out != 0:
        # TODO 输出转换失败信息
        print('**' * 30)
        print(f"{code_title} conversion failed!")
        print('**' * 30)

        # TODO 从 check.txt 中删除失败的文件名
        with open("wjh_crawlsers/data/check.txt", "r") as check_download:
            check_download_data = check_download.read()
        check_data = re.sub(f"{competition_name}/{code_name}\n", '', check_download_data)
        with open('wjh_crawlsers/data/check.txt', 'w') as after_check_download:
            after_check_download.write(check_data)
    else:
        # TODO 输出转换成功信息
        print('--' * 30)
        print(f"{code_title} conversion success!")
        delete_files(conversion_path, code_title)
