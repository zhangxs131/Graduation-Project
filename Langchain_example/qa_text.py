from langchain.llms import OpenAI
from langchain import PromptTemplate
# The vectorstore we'll be using
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.document_loaders import JSONLoader
import sys

llm=OpenAI(temperature=0,openai_api_key="1676891502535790599",openai_api_base="https://aigc.sankuai.com/v1/openai/native")

loader = JSONLoader(sys.argv[1],json_lines=True,jq_schema='.instruction+.output')
docs = loader.load()

print(docs[0])

num_total_characters = sum([len(x.page_content) for x in docs])

print (f"Now you have {len(docs)} documents that have an average of {num_total_characters / len(docs):,.0f} characters (smaller pieces)")


embedding_model_name = '../../pretrain_model/text2vec-large-chinese'
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

# Embed your documents and combine with the raw text in a pseudo db. Note: This will make an API call to OpenAI
docsearch = FAISS.from_documents(docs, embeddings)
docsearch.save_local('cache/vector_store_local')
#qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())


# query = "吃出异物 烟头 应该属于高风险还是低风险"
# result=qa.run(query)
# print(result)
search_result =docsearch.similarity_search_with_score(query='吃出异物 烟头', k=5)
print(search_result)