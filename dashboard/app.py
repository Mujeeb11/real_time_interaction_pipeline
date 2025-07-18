import streamlit as st
from pymongo import MongoClient
from config.settings import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["user_metrics"]
collection = db["aggregated"]

st.title("📊 Real-Time Interaction Dashboard")

# Show user-level stats
st.subheader("👤 User Interactions")
user_data = list(collection.find({"user_id": {"$exists": True}}).limit(10))
for doc in user_data:
    st.write(f"{doc['user_id']}: {doc['interaction_count']} interactions")

# Show item-level stats
st.subheader("🛍️ Item Interactions")
item_data = list(collection.find({"item_id": {"$exists": True}}).limit(10))
for doc in item_data:
    st.write(f"{doc['item_id']}: {doc['interaction_count']} interactions")