import streamlit as st
import pandas as pd
from io import BytesIO
from PIL import Image
from docx import Document  # Requires `pip install python-docx`

st.set_page_config(page_title="File Converter", layout="wide")

st.title("File Converter & Cleaner")
st.write("Upload files to preview, clean, and convert formats.")

# File uploader with more types
files = st.file_uploader(
    "Upload CSV, Excel, TXT, JSON, XML, Python, Images, Word files.", 
    type=["csv", "xlsx", "txt", "json", "xml", "py", "jpg", "png", "docx", "doc"],  
    accept_multiple_files=True
)

if files:
    for file in files:  
        ext = file.name.split(".")[-1].lower()  # Get file extension

        st.subheader(f"{file.name} - Preview")

        if ext in ["csv", "xlsx"]:  # Handle CSV & Excel
            df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)
            st.dataframe(df.head())

            # Remove duplicates
            if st.checkbox(f"Remove duplicates - {file.name}"):
                df = df.drop_duplicates()
                st.success("Duplicates removed")
                st.dataframe(df.head())

            # Fill missing values
            if st.checkbox(f"Fill missing values - {file.name}"):
                df.fillna(df.select_dtypes(include=["number"]).mean(), inplace=True)
                st.success("Missing values filled with column mean")
                st.dataframe(df.head())

            # Column selection
            selected_columns = st.multiselect(f"Select columns - {file.name}", df.columns, default=df.columns)
            df = df[selected_columns]
            st.dataframe(df.head())

            # Show chart
            if st.checkbox(f"Show chart - {file.name}") and not df.select_dtypes(include="number").empty:
                st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

            # Convert and download
            format_choice = st.radio(f"Convert {file.name} to:", ["csv", "excel"], key=file.name)

            if st.button(f"Download {file.name} as {format_choice}"):
                output = BytesIO()
                if format_choice == "csv":
                    df.to_csv(output, index=False)
                    mime = "text/csv"
                    new_name = file.name.replace(ext, "csv")
                else:
                    df.to_excel(output, index=False, engine='openpyxl')  # type: ignore
                    mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    new_name = file.name.replace(ext, "xlsx")

                output.seek(0)  # Reset buffer position
                st.download_button("Download file", filename=new_name, data=output, mime=mime)
                st.success("Processing Complete")

        elif ext in ["jpg", "png"]:  # Handle images
            img = Image.open(file)
            st.image(img, caption=file.name, use_column_width=True)  # Fixed the missing parenthesis here

        elif ext in ["docx", "doc"]:  # Handle Word documents
            doc = Document(file)
            text = "\n".join([para.text for para in doc.paragraphs])
            st.text_area(f"{file.name} - Content", text, height=300)

        elif ext == "py":  # Handle Python scripts
            content = file.read().decode("utf-8")
            st.code(content, language="python")

        elif ext == "txt":  # Handle Text files
            content = file.read().decode("utf-8")
            st.text_area(f"{file.name} - Content", content, height=300)

        elif ext == "json":  # Handle JSON files
            df = pd.read_json(file)
            st.dataframe(df.head())

        elif ext == "xml":  # Handle XML files
            df = pd.read_xml(file)
            st.dataframe(df.head())

        else:
            st.error(f"Unsupported file type: {file.name}")
