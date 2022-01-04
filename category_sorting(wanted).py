# 원티드 category mapping 한 데이터 중에서 카테고리에 맵핑된 숫자가 겹치는 경우 하나로 합쳐줌. 그리고 오름차순으로 정렬함.

import os

DATA_PATH = "./data/integration"
fields = ["id", "카테고리", "주요업무", "자격요건", "우대사항", "복리후생", "제목", "기업명", "지역", "산업", "근무형태", "경력", "학력", "급여", "키워드"]

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

# 데이터에서 카테고리만 뽑아와서 중복되는 값은 없애줌.
with open(os.path.join(DATA_PATH, "data_key15_wanted(category_numbering).txt"), 'rt', encoding='UTF8') as f:
    for line in f.readlines():
        if line.startswith('id'):
            pass
        else:
            line = line.split('\t')
            cat = line[1]
            id = line[0]
            cat = cat.split(' ')
            new_cat = []
            sorted_cat = []
            for i in cat:  # 중복 제거
                if int(i) not in new_cat:
                    new_cat.append(int(i))

            new_cat = sorted(new_cat)
            for j in new_cat:  # int를 str로 변환
                sorted_cat.append(str(j))

            category.append(' '.join(sorted_cat))
            major_task.append(line[2])
            qualification.append(line[3])
            prefer_treatment.append(line[4])
            benefit.append(line[5])
            title.append(line[6])
            company.append(line[7])
            location.append(line[8])
            industry.append(line[9])
            job_type.append(line[10])
            career.append(line[11])
            education.append(line[12])
            salary.append(line[13])
            keyword.append(line[14])

f = open(os.path.join(DATA_PATH, "data_key15_wanted(category_number_sorting).txt"), 'w', encoding='UTF8')
for i in range(len(category) + 1):
    if i == 0:
        f.write('id\t카테고리\t주요업무\t자격요건\t우대사항\t복리후생\t제목\t기업명\t지역\t산업\t근무형태\t경력\t학력\t급여\t키워드')
    else:
        f.write(f'{i - 1}\t{category[i - 1]}\t{major_task[i - 1]}\t{qualification[i - 1]}\t{prefer_treatment[i - 1]}\t{benefit[i - 1]}\t'
                f'{title[i - 1]}\t{company[i - 1]}\t{location[i - 1]}\t{industry[i - 1]}\t{job_type[i - 1]}\t{career[i - 1]}\t{education[i - 1]}\t'
                f'{salary[i - 1]}\t{keyword[i - 1]}')
