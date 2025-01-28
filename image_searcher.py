import streamlit as st

from image_indexer import ImageIndexer

st.title("Image Search")

st.markdown("Search for a specific image based on a short description.", unsafe_allow_html=True)

query = st.text_input("Enter query:")

if query:
    retrieved_docs = ImageIndexer.retrieve_document_by_query(query)

    for doc in retrieved_docs:
        st.image(ImageIndexer.get_image_path_by_id(doc.id), caption=doc.page_content)