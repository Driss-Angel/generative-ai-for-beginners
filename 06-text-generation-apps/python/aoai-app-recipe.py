from openai import AzureOpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure Azure OpenAI service client 
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"], 
  api_key=os.environ['AZURE_OPENAI_KEY'],  
  api_version = "2023-10-01-preview"
  )

deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']

no_recipes = input("食谱数量（例如 5： ")

ingredients = input("成分列表（例如鸡肉、土豆和胡萝卜：")

filter = input("过滤器（例如素食、严格素食或无麸质：")

# interpolate the number of recipes into the prompt an ingredients
prompt = f"向我显示包含以下成分的菜肴的 {no_recipes} 食谱：{ingredients}。每个食谱，列出所有使用的成分，没有{filter}："
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature = 0.1)


# print response
print("食谱:")
print(completion.choices[0].message.content)

old_prompt_result = completion.choices[0].message.content
prompt_shopping = "制作一份购物清单，请不要包含我家里已有的食材："

new_prompt = f"给定家里的食材 {ingredients} 以及这些生成的食谱：{old_prompt_result}、{prompt_shopping}"
messages = [{"role": "user", "content": new_prompt}]
completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature=0)

# print response
print("\n=====Shopping list ======= \n")
print(completion.choices[0].message.content)

