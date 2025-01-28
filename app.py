import streamlit as st

page = st.navigation(
    [st.Page(title="Image Upload", page="image_uploader.py", icon="🖼️"),
    st.Page(title="Image Search", page="image_searcher.py", icon="🔍"),
    st.Page(title="Image Reverse Search", page="image_searcher_reverse.py", icon="🔎")]
)

page.run()