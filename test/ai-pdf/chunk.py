import pdfplumber
from qdrant_client.http.models import PointStruct
from openai import OpenAI

client = OpenAI()
from qdrant_client import QdrantClient

fulltext = ""
with pdfplumber.open("build_db_in_go.pdf") as pdf:
    # loop over all the pages
    for page in pdf.pages:
        fulltext += page.extract_text()

text = fulltext

chunks = []
while len(text) > 500:
    last_period_index = text[:500].rfind('.')
    if last_period_index == -1:
        last_period_index = 500
    chunks.append(text[:last_period_index])
    text = text[last_period_index+1:]
chunks.append(text)


points = []
i = 1
for chunk in chunks:
    i += 1

    print("Embeddings chunk:", chunk)
    response = client.embeddings.create(input=chunk,
    model="text-embedding-ada-002")
    embeddings = response.data[0].embedding

    points.append(PointStruct(id=i, vector=embeddings, payload={"text": chunk}))


qdrant_client = QdrantClient(
    host="localhost",
)

operation_info = qdrant_client.upsert(
    collection_name="test_collection",
    wait=True,
    points=points
)

print("Operation info:", operation_info)
