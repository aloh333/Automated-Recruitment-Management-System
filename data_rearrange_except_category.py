# integration 데이터를 카테고리와 컨텐츠와 명사 형태소 분석으로 재배열함.

import os
import re
from eunjeon import Mecab

DATA_PATH = "./data/integration"
DATA_PATH_WANTED = "./data/wanted"
DATA_W_PATH = "./data/term-frerquency"
fields = ["id", "카테고리", "주요업무", "자격요건", "우대사항", "복리후생", "제목", "기업명", "지역", "산업", "근무형태", "경력", "학력", "급여", "키워드"]

m = Mecab()
category = []
content = []
mecab_tok = []

"""
with open(os.path.join(DATA_PATH, "data_key15.txt"), 'rt', encoding='UTF8') as f:
    for line in f.readlines():
        line = line.split('\t')

        cat = line[1]
        cat = cat.strip().split(',')
        cat = cat[0]  # 카테고리 2개 이상인 것은 첫 번째 거 하나만 가져옴.

        con = f'{line[2].strip()} {line[3].strip()} {line[4].strip()} {line[5].strip()} {line[6].strip()} {line[7].strip()} ' \
              f'{line[8].strip()} {line[9].strip()} {line[10].strip()} {line[11].strip()} {line[12].strip()} {line[13].strip()}' \
              f'{line[14].strip()}'
        con = re.sub('[^a-zA-Z0-9 ㄱ-ㅎ | 가-힣]', ' ', con)
        mec = m.nouns(con)
        mec = ' '.join(mec)

        category.append(cat)
        content.append(con)
        mecab_tok.append(mec)


f = open(os.path.join(DATA_W_PATH, "doc2vec.txt"), 'w', encoding='UTF8')
for i in range(len(category)):
    if i == 0:
        f.write(f'category\tcontent\tmecab_tok\n')
    else:
        f.write(f'{category[i]}\t{content[i]}\t{mecab_tok[i]}\n')
"""

with open(os.path.join(DATA_PATH_WANTED, "wanted.txt"), 'rt', encoding='UTF8') as f:
    for line in f.readlines():
        line = line.split('\t')

        cat = line[1]
        cat = cat.strip().split(',')
        cat = cat[0]  # 카테고리 2개 이상인 것은 첫 번째 거 하나만 가져옴.

        con = f'{line[2].strip()} {line[3].strip()} {line[4].strip()} {line[5].strip()} {line[6].strip()} {line[7].strip()} ' \
              f'{line[8].strip()} {line[9].strip()} {line[10].strip()} {line[11].strip()} {line[12].strip()} {line[13].strip()}' \
              f'{line[14].strip()}'
        con = re.sub('[^a-zA-Z0-9 ㄱ-ㅎ | 가-힣]', ' ', con)
        mec = m.nouns(con)
        mec = ' '.join(mec)

        category.append(cat)
        content.append(con)
        mecab_tok.append(mec)


f = open(os.path.join(DATA_W_PATH, "doc2vec.txt"), 'w', encoding='UTF8')
for i in range(len(category)):
    if i == 0:
        f.write(f'category\tcontent\tmecab_tok\n')
    else:
        f.write(f'{category[i]}\t{content[i]}\t{mecab_tok[i]}\n')