import time

import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
# The vectorstore we'll be using
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.document_loaders import JSONLoader
import sys
import json
from tqdm import tqdm
from sklearn.metrics import classification_report
import random

llm = ChatOpenAI(model_name="gpt-4", temperature=0.3,openai_api_key=1638852301697749012,openai_api_base="https://aigc.sankuai.com/v1/openai/native")


res=llm.predict('介绍一下gpt4')
print(res)
