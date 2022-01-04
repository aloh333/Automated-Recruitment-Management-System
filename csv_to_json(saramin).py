# 사람인 데이터를 json으로 변환하는 코드
import os
import json

DATA_PATH = "./data/saramin"
fields = ["index", "id", "제목", "기업명", "지역", "industry", "카테고리", "근무형태", "경력", "학력", "급여", "키워드"]
dict1 = []


with open(os.path.join(DATA_PATH, "saramin.txt"), 'rt', encoding='UTF8') as f:
    for line in f.readlines():
        # txt 파일의 첫 번째 문장 없애기
        if line.startswith('0'):
            pass
        else:
            job_posting = line.split('\t')
            print(job_posting)
            i = 0
            dict2 = {}
            while i < len(fields):
                if i == 0:
                    pass
                elif i == 1:
                    pass
                elif i == 5:
                    pass
                elif i == 6:
                    job_posting[i] = job_posting[i].strip().split(',')
                    job_posting[i] = ', '.join(job_posting[i])
                    dict2[fields[i]] = job_posting[i]
                else:
                    dict2[fields[i]] = job_posting[i]
                i = i + 1
            dict1.append(dict2)


out_file = open("data/saramin/saramin.json", "w", encoding="UTF8")
json.dump(dict1, out_file, ensure_ascii=False, indent="\t")
out_file.close()
