import csv

"""檔名記得改"""
with open("C:\\Users\\a9700\\Desktop\\溫州街.csv", encoding="utf-8", newline='') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    row_list = []
    for row in rows:
        row_list.append(row)

for i in range(1, len(row_list)):
    print('現在餐廳: ' + row_list[i][0])
    print('現在列數: ' + str(i+1))
    star = float(input('幾顆星: '))

    # 加入評論
    row_list[i].append(star)

    """檔名記得改"""
    with open("C:\\Users\\a9700\\Desktop\\溫州街.csv", 'w', newline='', encoding="utf-8") as csvfile:
        # 寫回csv檔
        writer = csv.writer(csvfile)
        writer.writerows(row_list)
    
    print('Good!')