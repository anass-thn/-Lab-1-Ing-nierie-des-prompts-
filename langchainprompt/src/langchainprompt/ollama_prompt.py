from langchain_ollama import ChatOllama
from IPython.display import display, Markdown

# Initialisation du modèle local
llm = ChatOllama(model="llama3.2:3b")

# Envoi du prompt au modèle
response = llm.invoke([
    {
        "role": "system",
        "content": "You are a helpful assistant. The output should be in Markdown."
    },
    {
        "role": "user",
        "content": "C'est quoi un Agent AI ?"
    }
])

# Affichage de la réponse en Markdown
display(Markdown(response.content))
print(response.content)