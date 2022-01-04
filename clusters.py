import os
import csv

DATA_PATH = "./data"


# 데이터 파일을 읽은 함수
def readfile(filename):
    f = open(os.path.join(DATA_PATH, filename), 'r', encoding='utf-8')
    rdr = csv.reader(f)

    lines = [line for line in rdr]

    # 첫번째 가로줄은 세로줄 제목임.
    colnames = lines[0]  # csv 파일의 첫번째 line
    rownames = []
    data = []

    for i in range(len(lines[1:])):
        rownames.append(i)

    for line in lines[1:]:
        data.append([float(x) for x in line])

    return rownames, colnames, data


from math import sqrt


def pearson(v1, v2):
    # 단순 합 계산
    sum1 = sum(v1)
    sum2 = sum(v2)

    # 제곱의 합 계산
    sum1Sq = sum([pow(v, 2) for v in v1])
    sum2Sq = sum([pow(v, 2) for v in v2])

    # 곱의 합 계산
    pSum = sum([v1[i] * v2[i] for i in range(len(v1))])

    # 피어슨 계수 r 계산
    num = pSum - (sum1 * sum2 / len(v1))
    den = sqrt((sum1Sq - pow(sum1, 2) / len(v1)) * (sum2Sq - pow(sum2, 2) / len(v1)))
    if den == 0:
        return 0

    return 1.0 - num / den


import random


def kcluster(rows, distance=pearson, k=4):
    # 각 점의 최대, 최소값을 구함.
    global bestmatches
    ranges = [(min([row[i] for row in rows]), max([row[i] for row in rows]))
             for i in range(len(rows[0]))]

    # 임의로 선정한 k개의 중심점을 생성함.
    clusters = [[random.random() * (ranges[i][1] - ranges[i][0]) + ranges[i][0]
                 for i in range(len(rows[0]))] for j in range(k)]

    lastmatches = None
    for t in range(100):
        print(f'Iteration {t}')
        bestmatches = [[] for i in range(k)]

        # 각 가로줄별로 가장 근접한 중심점을 찾음.
        for j in range(len(rows)):
            row = rows[j]
            bestmatch = 0
            for i in range(k):
                d = distance(clusters[i], row)
                if d < distance(clusters[bestmatch], row):
                    bestmatch = i
            bestmatches[bestmatch].append(j)

        # 이전과 같은 결과라면 완료함.
        if bestmatches == lastmatches:
            break
        lastmatches = bestmatches

        # 중심점을 멤버들의 평균으로 이동함.
        for i in range(k):
            avgs = [0.0] * len(rows[0])
            if len(bestmatches[i]) > 0:
                for rowid in bestmatches[i]:
                    for m in range(len(rows[rowid])):
                        avgs[m] += rows[rowid][m]
                for j in range(len(avgs)):
                    avgs[j] /= len(bestmatches[i])
                clusters[i] = avgs

    return bestmatches

