from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
import os
import sys
import pandas as pd


prompt_templte="请根据下面英文原文生成中文军事简讯，也就是进行格式规范的跨语言摘要任务。\n" \
                   "原文:{} \n" \
                   "简讯:"
prompt_templte_en="Please generate a Chinese military briefing based on the original English text below, that is, a cross-language summary task with standardized formats. \n" \
                  "original:{} \n" \
                  "summary:"

# PROMPT=PromptTemplate(template=prompt_templte,input_varialbes=['text'])
llm = OpenAI(model_name="gpt-3.5-turbo-16k-0613", temperature=0.3,openai_api_key=1638852301697749012,openai_api_base="https://aigc.sankuai.com/v1/openai/native")
# chain = load_summarize_chain(llm,chain_type='map_reduce',verbose=True,map_prompt=PROMPT,combine_prompt=PROMPT)
# llm = ChatOpenAI(model_name="gpt-4", temperature=0.3, openai_api_key=1638852301697749012,
#                      openai_api_base="https://aigc.sankuai.com/v1/openai/native")

def read_data(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        data=json.load(f)
    return data

def gen_summary(text):
    res = llm.predict(prompt_templte.format(text))
    return res

def main():
    data=read_data(sys.argv[1])
    source_text=[t['原文'] for  t in data]
    reference_summary=[t['整编内容'] for  t in data]
    predict_summary=[]

    for i in range(len(source_text)):
        res=gen_summary(prompt_templte.format(source_text[i]))
        print(res)
        predict_summary.append(res)

    df=pd.DataFrame(data={'predict_summary':predict_summary,'refer':reference_summary})
    df.to_csv('save_gpt3.5_0613.csv',index=None)


if __name__=='__main__':
    main()