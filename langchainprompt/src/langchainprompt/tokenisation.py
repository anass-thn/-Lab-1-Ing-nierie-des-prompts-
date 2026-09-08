import tiktoken

# Choisir l'encodage utilisé par GPT-4o
encoding = tiktoken.encoding_for_model("gpt-4o")

print(encoding.name)

system_message = """
Perform Sentiment analysis of the review presented in the user message.
The result should be positive or negative.
Do not justify your response.
"""

# Transformer le texte en tokens
tokens = encoding.encode(system_message)

# Nombre de tokens
print(len(tokens))

# Afficher les IDs des tokens
print(tokens)

# Afficher le contenu de chaque token
for token in tokens:
    print(encoding.decode_single_token_bytes(token=token), end="")


# Fonction pour compter les tokens
def num_tokens_from_string(
    string: str,
    encoding_name: str = "o200k_base"
) -> int:
    """Returns the number of tokens in a text string."""

    encoding = tiktoken.get_encoding(encoding_name)

    num_tokens = len(encoding.encode(string))

    return num_tokens


# Exemple
print("\nNombre de tokens :", num_tokens_from_string("tiktoken is great!"))