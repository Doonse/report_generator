import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


from langchain_openai import AzureChatOpenAI
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)
from langchain.chains import LLMChain


# Configuration for Azure OpenAI
api_version = os.getenv("API_VERSION")
endpoint = os.getenv("ENDPOINT")
api_key = os.getenv("API_KEY")


agent = AzureChatOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
    deployment_name="gpt-35"
)

# Define the templates
system_template = """
You are an assistant which reads and understands contents of a given code, and creates a detailed summary of tasks in hand.
The user will only pass code and you MUST generate the summary of the code.
Return ONLY the summary and nothing else.
"""

# template = ChatPromptTemplate.from_messages([
#     ("system", {system_template}),
#     ("human", "Hello, how are you doing?"),
#     ("ai", "I'm doing well, thanks!"),
#     ("human", "{user_input}"),
# ])


human_template = '{category}'

system_message = SystemMessagePromptTemplate.from_template(
    system_template
)

human_message = HumanMessagePromptTemplate.from_template(
    human_template
)

# Create the ChatPromptTemplate properly
prompt = ChatPromptTemplate.from_messages([system_message, human_message])

# Create and run the LLMChain with the proper input
chain = LLMChain(prompt=prompt, llm=agent)



# Example usage
# code_snippet = """ {user_input_code} """
code_snippet = """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(add(5, 3))
print(subtract(5, 3))
"""


# Run the chain and get the result
result = chain.run(category=code_snippet)
print(result)
