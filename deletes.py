import os


def delete_folder(competition_massage):
    # 获得 competition_name
    competition_name = competition_massage[1]

    # 如果不存在代码 删除 competition 文件夹
    os.system(f"rm -r -f wjh_crawlsers/data/crawlers_data/{competition_name}")

    # 输出没有代码信息
    print('--' * 30)
    print(f"{competition_name} code not found!")
    print(f"{competition_name} folder removed!")
    print('--' * 30)


def delete_files(path, code_title):
    # 如果不存在代码 删除 competition 文件夹
    os.system(f"rm -r -f {path}")

    # 输出文件已经删除信息
    print(f"{code_title}.ipynb file removed!")
    print('--' * 30)
