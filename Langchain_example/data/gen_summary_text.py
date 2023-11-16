import json
import sys

import openai
import textwrap

openai.api_key=1638852301697749012
openai.api_base="https://aigc.sankuai.com/v1/openai/native"

def read_data(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        data=json.load(f)
    return data

def gen_summary(text):
    mes=[{'role':'system','content':'你是一个英文到中文的军事文章摘要专家'}]
    mes.append({'role':'user','content':text})

    responses= openai.Completion.create(
        engine='gpt-4',
        messages=mes
    )
    summary = responses.choices[0].text.strip()
    return summary

def main():
    data=read_data(sys.argv[1])
    source_text=[t['原文'] for  t in data]
    reference_summary=[t['整编内容'] for  t in data]

    prompt_templte="请根据下面英文原文生成中文军事简讯，也就是进行格式规范的跨语言摘要任务。\n" \
                   "原文:{} \n" \
                   "简讯:"
    prompt_templte_en="Please generate a Chinese military briefing based on the original English text below, that is, a cross-language summary task with standardized formats. \n" \
                      "original:{} \n" \
                      "summary:"

    for i in range(len(source_text)):
        res=gen_summary(prompt_templte.format(source_text[i]))
        print(textwrap.fill(res,width=80))

if __name__=='__main__':
    main()
