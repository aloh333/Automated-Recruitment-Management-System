# 각 사이트의 카테고리 개수 세기
import os
import json

CATEGORY_PATH = "./category"

with open(os.path.join(CATEGORY_PATH, "wanted_category.json"), 'rt', encoding='cp949') as f:
    data = json.load(f)
    values = [*data.values()]
    values = '//'.join(values)
    values_list = values.split('//')
    print(len(values_list))

with open(os.path.join(CATEGORY_PATH, "jobplanet_category.json"), 'rt', encoding='UTF-8') as f:
    data = json.load(f)
    values = [*data.values()]
    values = '//'.join(values)
    values_list = values.split('//')
    print(len(values_list))

