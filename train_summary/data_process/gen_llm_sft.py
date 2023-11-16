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

# 获取“中文原文”和“整编内容”的list
zh_original_list = [item['中文原文'] for item in data]
zh_summary_list = [item['整编内容'] for item in data]



lines=500
count=0

if len(sys.argv)>2:
    lines=int(sys.argv[2])

count=0
for i in zh_original_list:
    if len(i)>lines:
         count+=1
print(count)

count=0
for i in zh_summary_list:
    if len(i)>2000-lines:
        count+=1
print(count)

# 填充到instruction和output
new_data = []
for original, summary in zip(zh_original_list, zh_summary_list):
    original=original[:lines]
    if len(original)<10:
        continue
    instruction = "请根据以下原文生成中文科技简讯摘要内容，中文原文：{} 简讯摘要：".format(original)
    output = summary
    new_data.append({"instruction": instruction, "input": "", "output": output})

# 保存为新的json文件
with open('train_sft.json', 'w', encoding='utf-8') as f:
    json.dump(new_data[:3500], f, ensure_ascii=False, indent=4)

# 保存为新的json文件
with open('dev_sft.json', 'w', encoding='utf-8') as f:
    json.dump(new_data[3500:], f, ensure_ascii=False, indent=4)
