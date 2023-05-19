import os
import random
import time

from checklist import checklist
from codes import code
from competitions import competition
from conversions import conversion
from creates import create_folder
from deletes import delete_folder
from descriptions import description
from downloads import download


def crawler():
    for page_token in random.sample(range(0, 30), 30):  # 用 random 模块生成 30 个不重复的数字
        for competition_massage in competition(page_token * 20):  # 放大参数并循环获取 competition_message

            create_folder(competition_massage)  # 创建 competition 文件夹

            description(competition_massage)  # 为 competition 文件夹下创建 项目描述 文件

            time.sleep(3)  # 程序休眠 3 秒 防止过多请求被封ip 环节 description 循环

            for code_massage in code(competition_massage):  # 循环获取 code_message

                if code_massage:  # 如果 code_massage 不为空

                    if checklist(code_massage, competition_massage):

                        download(code_massage, competition_massage)  # 下载 ipynb 文件

                        time.sleep(3)  # 程序休眠 3 秒 防止过多请求被封ip 环节 download 循环

                    else:
                        continue

                    conversion(code_massage, competition_massage)  # 转换 ipynb 文件 为 py 文件 并删除 ipynb 文件 以及记录转换失败的文件

                else:
                    delete_folder(competition_massage)  # 删除 competition 文件夹

            time.sleep(3)  # 程序休眠 3 秒 防止过多请求被封ip 环节 code 循环

        time.sleep(3)  # 程序休眠 3 秒 防止过多请求被封ip 环节 competitions 循环


if __name__ == '__main__':
    os.system('mkfile -n 10m wjh_crawlsers/data/check.txt')
    while True:
        try:
            crawler()
        except Exception as e:
            print(e)
            continue
