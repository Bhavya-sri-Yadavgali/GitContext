from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    """
    def login_user(username, password):
        user = find_user(username)
        if verify_password(password, user.password_hash):
            return create_session(user)
    """,

    """
    def verify_password(password, password_hash):
        return bcrypt.checkpw(password, password_hash)
    """,

    """
    def create_session(user):
        token = generate_jwt(user.id)
        return token
    """,

    """
    def send_email(to, subject, body):
        smtp.send(to, subject, body)
    """
]

query = "How is a user's password checked?"

document_embeddings = model.encode(documents)
query_embedding = model.encode(query)

similarities = cos_sim(query_embedding, document_embeddings)[0]

results = []

for i, score in enumerate(similarities):
    results.append((i, float(score)))

results.sort(key=lambda x: x[1], reverse=True)

for index, score in results:
    print(f"Score: {score:.4f}")
    print(documents[index])
    print("-" * 50)