import streamlit as st
from PIL import Image

def resize_image(input_image, size):
    try:
        img = Image.open(input_image)
        img = img.resize(size, Image.ANTIALIAS)
        return img
    except Exception as e:
        st.error(f"Error resizing image: {e}")
        return None

def main():
    st.title("Image Resizer")

    # File uploader to select image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "gif", "bmp"])
    
    if uploaded_file:
        # Display the uploaded image
        st.image(uploaded_file, caption="Original Image", use_column_width=True)

        # Input fields for width and height
        width = st.number_input("Width", min_value=1, value=300)
        height = st.number_input("Height", min_value=1, value=300)

        # Resize button
        if st.button("Resize Image"):
            resized_img = resize_image(uploaded_file, (width, height))
            if resized_img:
                # Display the resized image
                st.image(resized_img, caption="Resized Image", use_column_width=True)

                # Provide download link for resized image
                st.success("Image resized successfully!")
                st.download_button(
                    label="Download Resized Image",
                    data=resized_img.tobytes(),
                    file_name="resized_image.jpg",
                    mime="image/jpeg"
                )

if __name__ == "__main__":
    main()
