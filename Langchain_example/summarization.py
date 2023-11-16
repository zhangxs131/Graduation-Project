from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Note, the default model is already 'text-davinci-003' but I call it out here explicitly so you know where to change it later if you want
# llm = OpenAI(temperature=0, model_name='text-davinci-003', openai_api_key=openai_api_key)
llm=OpenAI(temperature=0,openai_api_key="1676891502535790599",openai_api_base="https://aigc.sankuai.com/v1/openai/native")


# Create our template

template = """
请使用中文对下面文本进行摘要，具有一定的科技简讯规范，使得简讯叙述明确。
{text}
中文简讯：
"""

# Create a LangChain prompt template that we can insert values to later
prompt = PromptTemplate(
    input_variables=["text"],
    template=template,
)

confusing_text = """
“哦。”魂环，魂兽，这两个崭新的名称不断在唐三心中回荡着。虽然他也不敢肯定自己的猜测是否正确，但玄天功一直无法突破瓶颈，这魂环显然是一个突破口。

此时，杰克已经回过神来，低头看向唐三，惊讶的道：“小三，你不会就是大师说的那个先天满魂力，武魂蓝银草的小子吧。”

唐三点了点头，道：“是我。”

老杰克蹲下身体，面对面的看着唐三，“小三，没想到你的天赋这样出色，可惜，你却有那样一个爸爸，没有好的武魂传承给你。否则的话，说不定你真的能成为咱们村子里第二个魂圣呢。你告诉爷爷，你愿不愿意去专门的学校学习魂师的修炼方法。只有那里才有关于武魂最准确的各种知识。”

唐三此时已经对武魂产生了浓厚的兴趣，尤其是这武魂与他自身的玄天功有关，但他依旧没有直接肯定的答复，“杰克爷爷，这要问我爸爸才行。”

杰克恍然醒悟过来，是啊，孩子再懂事也终究是个孩子，怎么说也要征询唐昊的意见才行。

眼中流露出几分坚定的光芒，尽管他实在不愿意去见那个邋遢鬼，但为了村子里能够再出一名魂师，他也顾不得这许多了。

“走吧，小三，爷爷送你回家。”老杰克先潜回了其他孩子，让他们的父母领走，这才带着唐三回到了铁匠铺。

上午，是唐昊例行的睡觉时间，铁匠铺里静悄悄的。

“唐昊，唐昊。”老杰克可不管唐昊是否在睡觉，对于这个邋遢铁匠，他实在是憎恶的很。如果不是他锻造的农具价格低廉的很，他早就想把唐昊踢出村子了。

一边叫着唐昊，老杰克目光四处掠过，本想找把椅子坐下，但看着那些破破烂烂的东西，他实在没勇气拉过来一把。他年纪已经不小了，可不想在这里摔个筋折骨断。

“谁在大呼小叫的。”唐昊略微带着怒气的声音响起，里间门帘撩开，缓步走了出来。

他首先看到了自己的儿子，这才将目光转移到杰克身上，“老杰克，干什么”

杰克没好气的道：“今天是你儿子武魂觉醒的日子，你不知道有多么重要别人家都是父母一起陪同着，可你到好，还是老样子。”

唐昊仿佛没听到杰克的讽刺一般，目光再次看向儿子，“小三，你的武魂觉醒了是什么”

唐三道：“爸爸，是蓝银草。”

“蓝银草”不知道为什么，一向对任何外物都不太感兴趣的唐昊听到这三个字的时候，身体突然颤抖了一下，眼中也流露出一丝特殊的光芒。

唐昊的表情变化只有唐三注意到了，老杰克自然不会管一个邋遢铁匠的表情如何，直接说道：“虽然是蓝银草，但小三可是先天满魂力。唐昊，我决定了，今年村子里那一个工读生的名额，就给小三了。让他到诺丁城初级魂师学院去学习。路费村子里包了。”

“蓝银草，蓝银草。”唐昊喃喃的念叨了两句，猛的抬起头，眼中流露出唐三从未见过的坚定光芒，沉声道：“不行。”

“你说什么我没听错吧。”杰克掏了掏自己的耳朵，吃惊的看着唐昊，“你应该知道这个机会有多么宝贵，我们圣魂村哪怕是曾经出过一个魂圣，一年也只有一个名额，其他村子，更是两三个村子才能共享一个名额，你知不知道这可是好机会。说不定，小三以后就能成为人上人。”

唐昊冷冷的看了杰克一眼，“人上人有什么用我只知道，他要是走了，就没人给我做饭吃了。蓝银草，你认为蓝银草武魂能够修炼成什么那只是个废武魂。”

老杰克怒声道：“可他是先天满魂力，只要能得到一个魂环，哪怕是品质最差的魂环，也立刻能够成为一名魂师。魂师，你知道么我们村子里已经很多年没有出过一个魂师了。”

唐昊淡然道：“这才是你真正的目的吧。说了不行，就是不行。你可以走了。”

“唐昊。”老杰克胸中怒火已经燃烧到了极限。

唐昊依旧是一副懒洋洋的样子，“不用那么大声，我还不聋。我说了，你可以走了。”

“杰克爷爷，您别生气。我还是不去学习魂师的能力了。爸爸说得对，蓝银草只是废武魂，谢谢您的好意。”

杰克虽然极度憎恶唐昊，但却非常喜欢懂事的唐三，满腔的怒火渐渐平复下来，长叹一声，“好孩子，爷爷不生气。好了，爷爷要走了。”说着，转身朝外面走去。

唐三赶忙相送。爸爸可以不理会，但杰克是村长，对他又很好，礼数上他绝不会少。

杰克走到铁匠铺门口停下脚步，转身看向唐昊，语重心长的道：“唐昊，你的一生也就这样完了，但小三还小，难道你不认为应该给他一种谋生手段么不要耽误了他，成为魂师，至少他以后不会像你这么落魄。如果你改变主意的话就来找我吧。距离今年诺丁魂师初级学院的报名时间还有三个月。”:
"""
# 字符数
num_tokens = llm.get_num_tokens(confusing_text)

print (f"There are {num_tokens} tokens in your file")


text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=5000, chunk_overlap=350)
docs = text_splitter.create_documents([confusing_text])

# Get your chain ready to use
chain = load_summarize_chain(llm=llm, chain_type='map_reduce')



# print ("------- Prompt Begin -------")
#
# final_prompt = prompt.format(text=confusing_text)
# print(final_prompt)
#
# print ("------- Prompt End -------")



# output = llm(final_prompt)
# print (output)
print (f"You now have {len(docs)} docs intead of 1 piece of text")
print(docs)

output = chain.run(docs)
print(output)