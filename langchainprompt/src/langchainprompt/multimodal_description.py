import base64

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import sys
try:
    # pyrefly: ignore [missing-import]
    from langchain.messages import HumanMessage
except (ImportError, ModuleNotFoundError):
    from langchain_core.messages import HumanMessage
from IPython.display import display, Image, Markdown

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


load_dotenv(override=True)

# Chemin vers l'image
path = "rag.png"

# Afficher l'image
display(Image(filename=path))


# Encoder l'image en Base64
def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


img = encode_image(path)


# Modèle multimodal
llm = ChatOpenAI(
    model="gpt-5.2",
    temperature=0
)


# Envoyer le texte + l'image au modèle
response = llm.invoke([
    HumanMessage(content=[
        {
            "type": "text",
            "text": "Qu'est-ce que tu vois dans cette image ?"
        },
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{img}"
            }
        }
    ])
])


# Afficher la réponse
display(Markdown(response.content))
print(response.content)