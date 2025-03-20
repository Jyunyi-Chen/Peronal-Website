import io
import fitz
import zipfile
import streamlit as st

from PIL import Image

st.title("PDF to PNG Converter")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    with st.spinner("Converting PDF to PNGs ..."):
        pdf_bytes = uploaded_file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap(dpi=200)
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                st.image(img, caption=f"Page {page_num+1}", use_container_width=True)

                img_bytes = io.BytesIO()
                img.save(img_bytes, format="PNG")
                zip_file.writestr(f"page_{page_num+1}.png", img_bytes.getvalue())

        zip_buffer.seek(0)
        st.download_button(
            label="📥 Download All PNGs as ZIP",
            data=zip_buffer,
            file_name="converted_images.zip",
            mime="application/zip"
        )
