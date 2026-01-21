# Importing necessary libraries
from rembg import remove
import streamlit as st

# Supported image file types
SUPPORTED_FILE_TYPES = ["png", "jpg", "jpeg"]


def main():
    """
    Main function to run the Streamlit app
    for the Image Background Removal Tool.
    """

    st.markdown(
        """
        ## 🖼️ Image Background Removal Tool ✅
        **A Rembg Powered Image Background Removal Tool**  
        Try this!!!
        <hr>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Choose and upload image file here",
        type=SUPPORTED_FILE_TYPES
    )

    if uploaded_file is not None:
        if st.button("Remove Background"):
            with st.spinner("Removing background..."):
                # Read image bytes
                image_bytes = uploaded_file.read()

                # Remove background
                output_bytes = remove(image_bytes)

            # Display images side by side
            col1, col2 = st.columns(2)

            with col1:
                st.image(
                    image_bytes,
                    caption="Original Image",
                    use_column_width=True
                )

            with col2:
                st.image(
                    output_bytes,
                    caption="Image with Background Removed",
                    use_column_width=True
                )

                st.download_button(
                    label="Download Image",
                    data=output_bytes,
                    file_name="output.png",
                    mime="image/png"
                )


if __name__ == "__main__":
    main()
