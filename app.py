import streamlit as st
from PIL import Image 
from rembg import remove 

def main():
    st.title("AI Background Remover")
    uploaded_file = st.file_uploader(label="Upload an image",type=["jpg","png","jpeg"],accept_multiple_files=False)
    if st.button("Execute🌟"):
        if uploaded_file:
            img = Image.open(uploaded_file)
            res = bg_remove(img)
            col1,col2 = st.columns(2,gap="large")
            with col1:
                st.write("## Original Image")
                st.image(img)
            with col2:
                st.write("## Result Image")
                st.image(res)
        else:
            st.error("Please upload an image")

def bg_remove(image):
    return remove(image)

if __name__ == "__main__":
    main()