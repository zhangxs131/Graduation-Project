import os

os.environ["SERPAPI_API_KEY"] = '8fcc987ca02be15c16bb60b0a7ee2e3fe48ff489d4304a2728badf146860b8e6'
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import AgentType

# 加载 OpenAI 模型
llm=OpenAI(temperature=0,openai_api_key="1676891502535790599",openai_api_base="https://aigc.sankuai.com/v1/openai/native")

 # 加载 serpapi 工具
tools = load_tools(["serpapi"])

# 如果搜索完想再计算一下可以这么写
# tools = load_tools(['serpapi', 'llm-math'], llm=llm)

# 如果搜索完想再让他再用python的print做点简单的计算，可以这样写
# tools=load_tools(["serpapi","python_repl"])

# 工具加载后都需要初始化，verbose 参数为 True，会打印全部的执行详情
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 运行 agent
res=agent.run("今天是几号？")

print(res)