
import json
import jieba
from rouge_chinese import Rouge
import numpy as np
import sys


def get_data():
    with open(sys.argv[1],'r',encoding='utf-8') as f:
        con=json.load(f)

    pred=con['predict_summary']
    refer=con['refer']

    pred=[v for k,v in pred.items()]
    refer=[v for k,v in refer.items()]
    # pred.pop(2)
    # refer.pop(2)

    assert len(pred)==len(refer)
    return pred,refer

def main():
    pred,refer=get_data()
    rouge=Rouge()
    score_dict={"rouge-1":[],"rouge-2":[],"rouge-l":[]}
    for p,r in zip(pred,refer):
        p=list(jieba.cut(p))
        r=list(jieba.cut(r))


        scores=rouge.get_scores(" ".join(p)," ".join(r))[0]

        for k,v in scores.items():
            score_dict[k].append(round(v["f"]*100,4))

    score={k:float(np.mean(v)) for k,v in score_dict.items()}
    print(score)


if __name__=='__main__':
    main()