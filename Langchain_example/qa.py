from langchain.llms import OpenAI
from langchain import PromptTemplate
# The vectorstore we'll be using
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

# The LangChain component we'll use to get the documents
from langchain.chains import RetrievalQA

# The easy document loader for text
from langchain.document_loaders import TextLoader

# The embedding engine that will convert our text to vectors
from langchain.embeddings.openai import OpenAIEmbeddings


# Note, the default model is already 'text-davinci-003' but I call it out here explicitly so you know where to change it later if you want
# llm = OpenAI(temperature=0, model_name='text-davinci-003', openai_api_key=openai_api_key)
llm=OpenAI(temperature=0,openai_api_key="1676891502535790599",openai_api_base="https://aigc.sankuai.com/v1/openai/native")

loader = TextLoader('test.csv')
doc = loader.load()
print (f"You have {len(doc)} document")
print (f"You have {len(doc[0].page_content)} characters in that document")


text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=400)
docs = text_splitter.split_documents(doc)
# Get the total number of characters so we can see the average later
num_total_characters = sum([len(x.page_content) for x in docs])

print (f"Now you have {len(docs)} documents that have an average of {num_total_characters / len(docs):,.0f} characters (smaller pieces)")


embedding_model_name = '/Users/zhangxiaosong/code/pretrain_model/text2vec-large-chinese'
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

# Embed your documents and combine with the raw text in a pseudo db. Note: This will make an API call to OpenAI
docsearch = FAISS.from_documents(docs, embeddings)


# context = """
# 吃到烟头 有风险
# 包装袋子里发现烟头 无风险
# """
#
# question = "那么 发现包装盒子中有烟头了 场景是否有风险 "
#
# output = llm(context + question)
#
# # I strip the text to remove the leading and trailing whitespace
# print (output.strip())

search_result =docsearch.similarity_search_with_score(query='吃出异物 烟头', k=2)
print(search_result)