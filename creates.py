import os


def create_folder(competition_massage):
    # 获得 competition_name
    competition_name = competition_massage[1]

    # 定义 competition 文件路径
    competition_path = f"wjh_crawlsers/data/crawlers_data/{competition_name}"

    # 判断 competition 文件是否存在
    if not os.path.exists(competition_path):
        # 如果不存在 直接创建 competition/codes 文件夹
        os.makedirs(f"wjh_crawlsers/data/crawlers_data/{competition_name}/codes")

        # 输出创建信息
        print('--' * 30)
        print(f"{competition_name} 项目文件夹已经创建!")
