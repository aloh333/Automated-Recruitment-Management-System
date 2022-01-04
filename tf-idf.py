# wofreq_dt_und_1000.csv를 읽어와서 tf-idf를 수행함.

from math import log
import os

DATA_PATH_TERM = "./data/term-frerquency"
DATA_PATH_TF_IDF = "./data/tf-idf"

"""

# df.txt 작성
terms_df = []
result = []

# csv 파일에서 한 줄씩 읽어와서 각 단어별로 document frequency를 구함.
with open(os.path.join(DATA_PATH_TERM, "data_key169(term_frequency).csv"), 'rt', encoding='UTF8') as f:
    freq = [0 for i in range(169)]  # document frequency를 세기 위해.
    for line in f.readlines():
        if line.startswith('시스템'):
            terms2 = line.split(',')
            for term in terms2:
                terms_df.append(term)

            terms_df.pop()  # 마지막 텀에 '\n'이 포함되서 그냥 빼줌.

        else:
            freqs = line.split(',')
            freqs.pop()  # 마지막 텀에 '\n'이 포함되서 그냥 빼줌.
            for i in range(len(freqs)):
                if int(freqs[i]) >= 1:
                    freq[i] += 1

    result = freq

# term들의 document frequency를 단어와 빈도수로 저장함.
f = open(os.path.join(DATA_PATH_TF_IDF, "df.txt"), 'w', encoding='UTF8')
for i in range(len(terms_df)):
    f.write(f'{terms_df[i]}\t{result[i]}\n')
"""

# idf.txt 작성
terms_idf = []
idfs = []

# df.txt를 읽어와서 idf를 구함.
with open(os.path.join(DATA_PATH_TF_IDF, "df.txt"), 'rt', encoding='UTF8') as f:
    for line in f.readlines():
        term = line.split('\t')[0]
        df = line.split('\t')[1]
        idf = log(21880/(int(df) + 1))
        terms_idf.append(term)
        idfs.append(idf)

"""
# term들의 inverse document frequency를 단어와 빈도수로 저장함.
f = open(os.path.join(DATA_PATH_TF_IDF, "idf.txt"), 'w', encoding='UTF8')
for i in range(len(terms)):
    f.write(f'{terms_idf[i]}\t{idfs[i]}\n')
    
"""

# tf-idf.csv 작성
tf_idfs = []

with open(os.path.join(DATA_PATH_TERM, "data_key169(term_frequency).csv"), 'r', encoding='UTF8') as f:
    for line in f.readlines():
        if line.startswith('시스템'):
            pass

        else:
            freqs = line.split(',')
            freqs.pop()  # 마지막 텀에 '\n'이 포함되서 그냥 빼줌.

            tf_idfs_per_line = []
            for i in range(len(freqs)):
                tf_idf = int(freqs[i]) * idfs[i]
                tf_idfs_per_line.append(tf_idf)

            tf_idfs.append(tf_idfs_per_line)


# 행: 채용공고 데이터, 열: 단어 빈도수
import csv

f = open(os.path.join(DATA_PATH_TF_IDF, "data_key169(tf_idf).csv"), 'w', encoding='UTF8', newline='')
wr = csv.writer(f)
wr.writerow(terms_idf)
for data in tf_idfs:
    wr.writerow(data)
f.close()