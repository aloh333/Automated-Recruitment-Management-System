# k-means clustering을 통해 나온 135개의 클러스터가 저장된 리스트를 통해 각 채용공고의 카테고리 빈도수를 확인
import csv
import os

DATA_PATH = "./data/integration"
DATA_PATH_K = "./data/k-means clustering"

# k-means 0 ~ 134의 채용공고 번호를 kmeans 리스트에 넣어줌.
kmeans = []
f = open(os.path.join(DATA_PATH_K, 'k-means_clustering.csv'), 'r', encoding='UTF8')
rdr = csv.reader(f)
for line in rdr:
    kmeans.append(line)
f.close()

print(len(kmeans[0]))
"""
# 채용공고의 카테고리만 뽑아옴.
split_category = []
f = open(os.path.join(DATA_PATH, 'data_key15(category_number_sorting).txt'), 'r', encoding='UTF8')
for line in f.readlines():
    if line.startswith('id'):
        pass
    else:
        str_category = []
        line = line.split('\t')
        if ' ' in line[1]:
            split_category.append(line[1].split(' '))
        else:
            str_category.append(line[1])
            split_category.append(str_category)

f.close()

# ' '으로 붙어있던 카테고리는 나눠서 가져옴.
f = open(os.path.join(DATA_PATH_K, "category_per_data.csv"), 'w', encoding='UTF8', newline='')
wr = csv.writer(f)
for data in split_category:
    wr.writerow(data)

f.close()
"""

category = []
f = open(os.path.join(DATA_PATH_K, 'category_per_data.csv'), 'r', encoding='UTF8')
line = f.readlines()
# print(line[int(kmeans[0][3])][:-1].split(',')[0])
for i in range(len(kmeans)):
    category2 = []
    for j in range(len(kmeans[i])):
        if ',' in line[int(kmeans[i][j])][:-1]:
            numbers = line[int(kmeans[i][j])][:-1].split(',')
            for number in numbers:
                category2.append(number)
        else:
            category2.append(line[int(kmeans[i][j])][:-1])
    category.append(category2)
f.close()
print(len(category[0]))
"""
from collections import Counter


def find_max(word):
    counter = Counter(word)
    max_count = -1
    for letter in counter:
        if counter[letter] > max_count:
            max_count = counter[letter]
            max_letter = letter
    return max_letter, max_count


f = open(os.path.join(DATA_PATH_K, "k-means_frequency.txt"), 'w', encoding='UTF8')
f.write('category,frequency\n')
for i in range(len(category)):
    counts = find_max(category[i])
    f.write(str(counts))
    f.write('\n')
f.close()
"""