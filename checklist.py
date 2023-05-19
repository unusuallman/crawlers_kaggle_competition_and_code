import os
import re


def checklist(code_massage, competition_massage):
    # TODO 获得 codes_title
    code_name = code_massage[1]

    # TODO 获得 competition_name
    competition_name = competition_massage[1]

    if not os.path.exists(f"wjh_crawlsers/data/check.txt"):
        return False
    else:
        with open("wjh_crawlsers/data/check.txt", "r") as check:
            if not re.search(f"{competition_name}/{code_name}", check.read()):
                return True
            else:
                return False
