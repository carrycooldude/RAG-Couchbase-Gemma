from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator

# Connect to Couchbase
def get_couchbase_cluster():
    cluster = Cluster("couchbase://localhost", ClusterOptions(PasswordAuthenticator("Administrator", "Password")))
    bucket = cluster.bucket("rag_db")
    collection = bucket.default_collection()
    return collection

if __name__ == "__main__":
    collection = get_couchbase_cluster()
    print("✅ Couchbase connected!")