import re
import csv
from io import StringIO
import json

# 读取SQL文件内容（假设数据保存在data.sql中）
with open('data.sql', 'r', encoding='utf-8') as f:
    sql_lines = f.readlines()

results = []

# 正则表达式匹配INSERT语句中的VALUES部分
insert_pattern = re.compile(r'INSERT INTO.*?VALUES\s*\((.*)\);', re.IGNORECASE)

for line in sql_lines:
    # 提取VALUES后面的部分
    match = insert_pattern.search(line)
    if not match:
        continue
    values_str = match.group(1)

    # 使用csv reader解析字段值（单引号作为引号字符）
    reader = csv.reader(StringIO(values_str), delimiter=',', quotechar="'", skipinitialspace=True)
    try:
        row = next(reader)
    except Exception as e:
        print(f"解析行时出错：{line}")
        continue

    # 检查字段数量是否匹配
    if len(row) != 9:
        print(f"跳过字段数量不匹配的行：{line}")
        continue

    # 提取各字段值并处理
    try:
        record = {
            'id': int(row[0].strip()),
            'category_main': row[1].strip(),
            'category': row[2].strip(),
            'title': row[3].strip(),
            'url': row[4].strip(),
            'date': row[5].strip(),
            'content': row[6].strip(),
            'image_urls': row[7].strip().split(),  # 按空格分割为列表
            'is_posted': bool(int(row[8].strip()))
        }
    except (ValueError, IndexError) as e:
        print(f"处理字段时出错：{line}")
        continue

    # 筛选category为“教务处”的记录
    if record['category'] == '教务处':
        results.append(record)

# 将结果写入JSON文件
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"共筛选出{len(results)}条记录，已保存至output.json")
