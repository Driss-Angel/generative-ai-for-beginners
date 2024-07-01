from openai import AzureOpenAI
import os
import dotenv

# 加载dotenv
dotenv.load_dotenv()

# 配置Azure OpenAI服务客户端
client = AzureOpenAI(
  azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"], 
  api_key=os.environ['AZURE_OPENAI_KEY'],  
  api_version="2023-10-01-preview"
)

deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']

# 添加你的完成代码
persona = input("告诉我你想扮演的历史人物: ")
question = input("问一个关于这个历史人物的问题: ")
prompt = f"""
你将扮演历史人物 {persona}。

每当被问到某些问题时，你需要记住时间线和事件的事实，并且只提供准确的答案。不要自己创造内容。如果你不知道某些事情，请说你不记得。

请回答这个问题: {question}
"""
messages = [{"role": "user", "content": prompt}]  
# 生成回答
completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0)

# 打印回答
print(completion.choices[0].message.content)