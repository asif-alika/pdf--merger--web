import streamlit as st
import PyPDF2
from io import BytesIO

st.set_page_config(page_title="PDF Merger by Asif", layout="centered")

st.title("📎 PDF Merger by Asif")
st.markdown("Merge multiple PDF files into one. Upload and click merge!")

uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files and len(uploaded_files) >= 2:
    if st.button("Merge PDFs"):
        merger = PyPDF2.PdfMerger()

        for uploaded_file in uploaded_files:
            merger.append(uploaded_file)

        output_pdf = BytesIO()
        merger.write(output_pdf)
        merger.close()
        output_pdf.seek(0)

        st.success("✅ PDFs merged successfully!")
        st.download_button(
            label="📥 Download Merged PDF",
            data=output_pdf,
            file_name="merged.pdf",
            mime="application/pdf"
        )
elif uploaded_files and len(uploaded_files) < 2:
    st.warning("⚠️ Please upload at least 2 PDF files to merge.")
