# k-means clustering을 통해 나온 135개의 클러스터가 저장된 리스트를 통해 각 채용공고의 카테고리 빈도수를 확인(tf-idf 버전)
import csv
import os

DATA_PATH_K = "./data/k-means clustering"

# k-means 0 ~ 134의 채용공고 번호를 kmeans 리스트에 넣어줌.
kmeans = []
f = open(os.path.join(DATA_PATH_K, 'kclust(135_tf_idf_2).csv'), 'r', encoding='UTF8')
rdr = csv.reader(f)
for line in rdr:
    kmeans.append(line)
f.close()

# kmeans의 채용공고 번호를 통해 카테고리 번호로 변환한다.
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

# 카테고리 클러스터링 최다 빈도수를 뽑아옴.
from collections import Counter


def find_max(word):
    counter = Counter(word)
    max_count = -1
    for letter in counter:
        if counter[letter] > max_count:
            max_count = counter[letter]
            max_letter = letter
    return max_letter, max_count


f = open(os.path.join(DATA_PATH_K, "k-means_freq_tf_idf.txt"), 'w', encoding='UTF8')
f.write('category,frequency\n')
for i in range(len(category)):
    counts = find_max(category[i])
    f.write(str(counts))
    f.write('\n')
f.close()
