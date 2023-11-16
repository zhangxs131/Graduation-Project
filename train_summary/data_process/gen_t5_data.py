import json
import sys


data=[]
# 读取json文件
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    content=f.readlines()
for i in content:
    data.append(json.loads(i))

# 输出list的行数
print("List的行数：", len(data))


# 保存为新的json文件
with open('train_1.json', 'w', encoding='utf-8') as f:
    json.dump(data[:3500], f, ensure_ascii=False, indent=4)

# 保存为新的json文件
with open('dev_1.json', 'w', encoding='utf-8') as f:
    json.dump(data[3500:], f, ensure_ascii=False, indent=4)

