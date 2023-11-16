import pandas as pd
from langchain.llms import OpenAI
from langchain import PromptTemplate
# The vectorstore we'll be using
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.document_loaders import JSONLoader
import sys
from tqdm import tqdm
from sklearn.metrics import classification_report


embedding_model_name = '../../pretrain_model/text2vec-large-chinese'
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
docsearch = FAISS.load_local('cache/vector_store_local', embeddings)


def predict(query,k=5):

    search_result =docsearch.similarity_search_with_score(query=query, k=k)
    result_dir={'高风险':1,'低风险':0}
    result=[]
    for doc in search_result:
        result.append(result_dir[doc[0].page_content[-3:]])

    if sum(result)>k//2:
        return 1
    else:
        return 0

def main():
    test_file=sys.argv[1]
    df=pd.read_csv(test_file)
    text=df['text'].tolist()
    label=df['label'].tolist()
    pred=[]
    for i in tqdm(text):
        pred.append(predict(i))

    assert len(label)==len(pred)
    report=classification_report(label,pred)
    print(report)

if __name__=='__main__':
    main()

