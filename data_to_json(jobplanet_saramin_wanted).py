# 잡플래닛과 원티드, 그리고 사람인을 리스트에 json 으로 변환하는 코드

import os
import json
import re

DATA_PATH_JOBPLANET = "./data/jobplanet"
DATA_PATH_SARAMIN = "./data/saramin"
DATA_PATH_WANTED = "./data/wanted"
fields = ["직무", "주요업무", "자격요건", "우대사항", "복리후생"]
fields2 = ["직무", "제목", "기업이름", "주요업무", "자격요건", "우대사항", "복리후생"]
fields3 = ["index", "id", "제목", "기업명", "지역", "industry", "카테고리", "근무형태", "경력", "학력", "급여", "키워드"]
fields4 = ["제목", "주요업무", "자격요건", "우대사항", "복리후생"]
dict1 = []


def csv_to_json(path):
    with open(os.path.join(DATA_PATH_SARAMIN, path), 'rt', encoding='UTF8') as f:
        for line in f.readlines():
            # txt 파일의 첫 번째 문장 없애기
            if line.startswith('0'):
                pass
            else:
                job_posting = line.split('\t')
                print(job_posting)
                i = 0
                dict2 = {}
                while i < len(fields3):
                    if i == 0:
                        pass
                    elif i == 1:
                        pass
                    elif i == 5:
                        pass
                    elif i == 6:
                        job_posting[i] = job_posting[i].strip().split(',')
                        job_posting[i] = '//'.join(job_posting[i])
                        dict2[fields3[i]] = job_posting[i]
                    else:
                        dict2[fields3[i]] = job_posting[i]
                    i = i + 1
                dict1.append(dict2)


def json_to_list(path):
    with open(os.path.join(DATA_PATH_JOBPLANET, path), 'rt', encoding='UTF8') as f:
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
                        line = re.sub(', ', '//', line)
                        line = re.sub(',', '', line)
                        line = re.sub('\t', '', line)
                    else:  # 한 문장에 ':'가 하나만 있을 경우
                        line = line[1]
                        line = line.strip()
                        line = re.sub('"', '', line)
                        line = re.sub(', ', '//', line)
                        line = re.sub(',', '', line)
                        line = re.sub('\t', '', line)

                # 잡플래닛 key 값 7개일때
                if len(lines) == 7:
                    dict2[fields2[i]] = line
                else:
                    dict2[fields[i]] = line

                i += 1
            dict1.append(dict2)
            l += 1


# 잡플래닛_01 직무 내용이 제목임.
def json_to_list_title(path):
    with open(os.path.join(DATA_PATH_JOBPLANET, path), 'rt', encoding='UTF8') as f:
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

                # 잡플래닛 key 값 7개일때
                if len(lines) == 7:
                    dict2[fields2[i]] = line
                else:
                    dict2[fields4[i]] = line

                i += 1
            dict1.append(dict2)
            l += 1

"""
# json_to_list_title("jobplanet_key5_01.txt")
json_to_list("jobplanet_key5_02.txt")
json_to_list("jobplanet_key7.txt")

# 사람인 데이터 쓰기
csv_to_json("saramin.txt")

# json 으로 써주는 코드
out_file = open("./data/integration/saramin+jobplanet+wanted.json", "w", encoding="UTF8")
json.dump(dict1, out_file, ensure_ascii=False, indent="\t")
out_file.close()
"""

# 원티드 추가 데이터만 정리해줌.
json_to_list("wanted.json")

out_file = open('data/wanted/wanted.json', 'w', encoding='UTF8')
json.dump(dict1, out_file, ensure_ascii=False, indent='\t')
out_file.close()

