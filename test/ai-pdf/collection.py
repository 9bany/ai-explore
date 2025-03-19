from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from qdrant_client.http import models

qdrant_client = QdrantClient(
    host="localhost",
)

qdrant_client.recreate_collection(
    collection_name="test_collection_2",
    vectors_config=models.VectorParams(size=4096, distance=models.Distance.COSINE),
)

print("Create collection reponse:", qdrant_client)

collection_info = qdrant_client.get_collection(collection_name="test_collection")

print("Collection info:", collection_info)