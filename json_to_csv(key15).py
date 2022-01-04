# 사람인, 잡플래닛, 원티드 데이터를 하나의 csv 파일로 만들기
import os
import json

DATA_PATH = "./data/integration"
DATA_PATH_WANTED = "./data/wanted"
fields_s = ["index", "id", "제목", "기업명", "지역", "industry", "카테고리", "근무형태", "경력", "학력", "급여", "키워드", "url"]
fields_j_w = ["직무", "주요업무", "자격요건", "우대사항", "복리후생"]
fields_j_7 = ["직무", "제목", "기업이름", "주요업무", "자격요건", "우대사항", "복리후생"]
fields_main = ["id", "카테고리", "주요업무", "자격요건", "우대사항", "복리후생", "제목", "기업명", "지역", "산업", "근무형태", "경력",
               "학력", "급여", "키워드"]

category = []
major_task = []
qualification = []
prefer_treatment = []
benefit = []
title = []
company = []
location = []
industry = []
job_type = []
career = []
education = []
salary = []
keyword = []


def open_data(path):
    with open(os.path.join(DATA_PATH, path), 'rt', encoding='UTF8') as f:
        datas = json.load(f)
        for data in datas:
            # 카테고리
            if "직무" in data:
                category.append(data["직무"])
            elif "카테고리" in data:
                category.append(data["카테고리"])
            else:
                category.append('0')

            # 주요업무
            if "주요업무" in data:
                major_task.append(data["주요업무"])
            else:
                major_task.append('0')

            # 자격요건
            if "자격요건" in data:
                qualification.append(data["자격요건"])
            else:
                qualification.append('0')

            # 우대사항
            if "우대사항" in data:
                prefer_treatment.append(data["우대사항"])
            else:
                prefer_treatment.append('0')

            # 복리후생
            if "복리후생" in data:
                benefit.append(data["복리후생"])
            else:
                benefit.append('0')

            # 제목
            if "제목" in data:
                title.append(data["제목"])
            else:
                title.append('0')

            # 기업명
            if "기업이름" in data:
                company.append(data["기업이름"])
            elif "기업명" in data:
                company.append(data["기업명"])
            else:
                company.append('0')

            # 지역
            if "지역" in data:
                location.append(data["지역"])
            else:
                location.append('0')

            # 산업
            if "산업" in data:
                industry.append(data["산업"])
            else:
                industry.append('0')

            # 근무형태
            if "근무형태" in data:
                job_type.append(data["근무형태"])
            else:
                job_type.append('0')

            # 경력
            if "경력" in data:
                career.append(data["경력"])
            else:
                career.append('0')

            # 학력
            if "학력" in data:
                education.append(data["학력"])
            else:
                education.append('0')

            # 급여
            if "급여" in data:
                salary.append(data["급여"])
            else:
                salary.append('0')

            # 키워드
            if "키워드" in data:
                keyword.append(data["키워드"])
            else:
                keyword.append('0')


def write_csv(path):
    f = open(os.path.join(DATA_PATH, path), 'w', encoding='UTF8')
    for i in range(len(category) + 1):
        if i == 0:
            f.write('id\t카테고리\t주요업무\t자격요건\t우대사항\t복리후생\t제목\t기업명\t지역\t산업\t근무형태\t경력\t학력\t급여\t키워드\n')
        else:
            f.write(f'{i - 1}\t{category[i - 1]}\t{major_task[i - 1]}\t{qualification[i - 1]}\t{prefer_treatment[i - 1]}\t{benefit[i - 1]}\t'
                    f'{title[i - 1]}\t{company[i - 1]}\t{location[i - 1]}\t{industry[i - 1]}\t{job_type[i - 1]}\t{career[i - 1]}\t{education[i - 1]}\t'
                    f'{salary[i - 1]}\t{keyword[i - 1]}\n')


# open_data("saramin+jobplanet+wanted.json")
# write_csv("data_key15.txt")

# 원티드 추가 데이터만 정리해줌.
open_data('wanted.json')
write_csv('wanted.txt')