from dotenv import load_dotenv
from langchain_groq import ChatGroq
try:
    # pyrefly: ignore [missing-import]
    from langchain.messages import SystemMessage, HumanMessage
except (ImportError, ModuleNotFoundError):
    from langchain_core.messages import SystemMessage, HumanMessage
from IPython.display import display, Markdown

load_dotenv(override=True)

llm2 = ChatGroq(model="openai/gpt-oss-120b")

resp2 = llm2.invoke([
    SystemMessage(
        content="You are a helpful assistant. The output should be in Markdown."
    ),
    HumanMessage(
        content="C'est quoi un Agent AI ?"
    )
])

display(Markdown(resp2.content))
print(resp2.content)
