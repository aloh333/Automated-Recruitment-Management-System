# 잡플래닛 key 값 7개일때 리스트에 json 으로 변환하는 코드

import os
import json
import re

DATA_PATH = "./data/jobplanet"
fields = ["직무", "제목", "기업이름", "주요업무", "자격요건", "우대사항", "복리후생"]
dict1 = []


def json_to_list(path):
    with open(os.path.join(DATA_PATH, path), 'rt', encoding='UTF8') as f:
        data = f.read()
        # }{을 기준으로 split
        job_posting = data[2:-2].split('\n}{\n')

        l = 0
        while l < len(job_posting):
            lines = job_posting[l].split('\n')
            i = 0
            dict2 = {}
            print(lines)
            while i < (len(lines)):
                line = lines[i].strip()
                if len(line) != 0:
                    line = line.split(':')
                    if len(line) != 2:  # 한 문장에 ':'가 많이 있을 경우
                        line = ':'.join(line[1:])
                        line = line.strip()
                        line = re.sub('"', '', line)
                        line = re.sub(',', '', line)
                    else:  # 한 문장에 ':'가 하나만 있을 경우
                        line = line[1]
                        line = line.strip()
                        line = re.sub('"', '', line)
                        line = re.sub(',', '', line)

                dict2[fields[i]] = line

                i += 1
            dict1.append(dict2)
            l += 1

    # json 으로 써주는 코드
    out_file = open("data/integration/jobplanet+wanted.json", "w", encoding="UTF8")
    json.dump(dict1, out_file, ensure_ascii=False, indent="\t")
    out_file.close()


json_to_list("jobplanet_key7.txt")

