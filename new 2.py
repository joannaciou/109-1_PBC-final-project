# import requests 套件包
import requests
import json

# 輸入的部分
address = input('輸入網址: ')
row_num = int(input('第幾列: '))
star = float(input('幾顆星: '))

# GET請求抓資料
page = requests.get(address).text
prepage = ')]}\''
text = page.replace(prepage, '')

soup = json.loads(text)

conlist = soup[2]

a = 0
com_list = []
for i in conlist:
    if a <= 2:
        com_list.append(str(i[3]))
        a += 1
    else:
        break

import csv

"""檔名記得改"""
with open("C:\\Users\\a9700\\Desktop\\溫州街.csv", encoding="utf-8", newline='') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    row_list = []
    for row in rows:
        row_list.append(row)

# 加入評論
row_list[row_num - 1].append(com_list)
row_list[row_num - 1].append(star)

"""檔名記得改"""
with open("C:\\Users\\a9700\\Desktop\\溫州街.csv", 'w', newline='', encoding="utf-8") as csvfile:
    # 寫回csv檔
    writer = csv.writer(csvfile)
    writer.writerows(row_list)