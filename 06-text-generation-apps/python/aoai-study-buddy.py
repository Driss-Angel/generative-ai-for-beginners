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
question = input("问你的学习伙伴关于Python语言的问题: ")
prompt = f"""
你是Python语言的专家。

每当被问到某些问题时，你需要以以下格式提供回答。

- 概念
- 显示概念实现的示例代码
- 对示例的解释以及如何实现这个概念，使用户更好地理解。

请回答这个问题: {question}
"""
messages = [{"role": "user", "content": prompt}]  
# 生成回答
completion = client.chat.completions.create(model=deployment, messages=messages)

# 打印回答
print(completion.choices[0].message.content)