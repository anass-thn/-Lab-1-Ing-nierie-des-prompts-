import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
try:
    # pyrefly: ignore [missing-import]
    from langchain.messages import SystemMessage, HumanMessage
except (ImportError, ModuleNotFoundError):
    from langchain_core.messages import SystemMessage, HumanMessage
from IPython.display import display, Markdown

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv(override=True)

# Initialisation du modèle OpenAI (ex: gpt-4o-mini ou gpt-4o)
llm3 = ChatOpenAI(model="gpt-4o-mini")

# Envoi du prompt avec SystemMessage et HumanMessage
resp3 = llm3.invoke([
    SystemMessage(
        content="You are a helpful assistant. The output should be in Markdown."
    ),
    HumanMessage(
        content="C'est quoi un Agent AI ?"
    )
])

# Affichage du résultat
display(Markdown(resp3.content))
print(resp3.content)
