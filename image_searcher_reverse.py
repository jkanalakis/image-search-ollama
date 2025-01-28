import streamlit as st

from image_indexer import ImageIndexer

st.title("Image Reverse Search")

st.markdown("Search for a specific image by providing a similar image.", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose an image",
    accept_multiple_files=False,
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    retrieved_docs = ImageIndexer.retrieve_documents_by_image(uploaded_file)

    for doc in retrieved_docs:
        st.image(
            ImageIndexer.get_image_path_by_id(doc.id), 
            caption=doc.page_content
        )