# category mapping 한 데이터를 명사 형태소 분석하고 단어 등장 빈도수 순으로 뽑아서 벡터로 만듬. (K-Means 클러스터링)


import os
import re
from eunjeon import Mecab

DATA_PATH = "./data/integration"
DATA_PATH_TERM = "./data/term-frerquency"
fields = ["id", "카테고리", "주요업무", "자격요건", "우대사항", "복리후생", "제목", "기업명", "지역", "산업", "근무형태", "경력", "학력", "급여", "키워드"]

m = Mecab()
mecab_tok = []

words = []
frequency = []


# 데이터에서 명사 형태소만 뽑아옴.
with open(os.path.join(DATA_PATH, "data_key15(category_number_sorting).txt"), 'rt', encoding='UTF8') as f:
    for line in f.readlines():
        if line.startswith('id'):
            pass
        else:
            line = line.split('\t')
            con = f'{line[2].strip()} {line[3].strip()} {line[4].strip()} {line[5].strip()} {line[6].strip()} ' \
                  f'{line[7].strip()} {line[8].strip()} {line[9].strip()} {line[10].strip()} {line[11].strip()} ' \
                  f'{line[12].strip()} {line[13].strip()} {line[14].strip()}'
            con = re.sub('[^a-zA-Z0-9 ㄱ-ㅎ | 가-힣]', ' ', con)
            mec = m.nouns(con)

            mecab_tok.append(mec)
            # print(mec)


# 단어 빈도수에 따라서 맵핑
token = mecab_tok
word2index = {}
bow = []
for voca_list in token:
    for voca in voca_list:
        if voca not in word2index.keys():
            word2index[voca] = len(word2index)
            bow.insert(len(word2index) - 1, 1)
        else:
            index = word2index.get(voca)
            bow[index] = bow[index] + 1


# 빈도수가 1000 미만인 것은 없애줌.
itemlist = [*word2index.items()]
itemlist2 = []
bow2 = []
for j in range(len(bow)):
    if bow[j] < 1000:
        pass
    else:
        bow2.append(bow[j])
        itemlist2.append(itemlist[j])


# 단어를 다시 0 부터 순서대로 나열함. (딕셔너리)
word2index2 = dict(itemlist2)
keylist = [*word2index2.keys()]
word2index3 = {}
for k in range(len(keylist)):
    word2index3[keylist[k]] = k

words = keylist
frequency = bow2

print(words)
print(len(words))
"""
# 빈도수 1000 미만일때 단어와 빈도수로 저장함.
f = open(os.path.join(DATA_PATH_TERM, "term_frequency(key169).txt"), 'w', encoding='UTF8')
for i in range(len(words)):
    f.write(f'{words[i - 1]}\t{frequency[i - 1]}\n')


data_per_line = []
for voca_list in token:
    word2index_per_line = {}
    bow_per_line = []
    for voca in voca_list:
        if voca not in word2index_per_line.keys():
            word2index_per_line[voca] = len(word2index_per_line)
            bow_per_line.insert(len(word2index_per_line) - 1, 1)
        else:
            index = word2index_per_line.get(voca)
            bow_per_line[index] = bow_per_line[index] + 1

    keylist_per_line = [*word2index_per_line.keys()]
    word2index2_per_line = {}
    for i in range(len(keylist_per_line)):
        word2index2_per_line[keylist_per_line[i]] = bow_per_line[i]

    freq_per_line = []  # 한 채용공고 당 최종 빈도수
    for j in range(len(words)):
        freq_per_line.append(0)
        for key in keylist_per_line:
            if words[j] == key:
                freq_per_line[j] = word2index2_per_line[key]

    data_per_line.append(freq_per_line)


# 행: 채용공고 데이터, 열: 단어 빈도수
import csv

f = open(os.path.join(DATA_PATH_TERM, "data_key169(term_frequency).csv"), 'w', encoding='UTF8', newline='')
wr = csv.writer(f)
wr.writerow(words)
for data in data_per_line:
    wr.writerow(data)
f.close()
"""
"""
# 10개만 출력해봄.
import pandas as pd

data = pd.read_csv(os.path.join(DATA_PATH_TERM, "data_key169(term_frequency).csv"), encoding='utf8')
print(data.shape)
print(data.head(10))
"""