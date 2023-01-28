import streamlit as st
import pandas as pd
import json
import pyperclip
from PIL import Image

def create_faq_schema(file):
    # Read the spreadsheet with questions and answers
    df = pd.read_excel(file)

    # Create a dictionary for the FAQ schema
    faq_schema = {
        "@context": "http://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }

    # Iterate over each row in the spreadsheet
    for index, row in df.iterrows():
        # Get the question and answer from the row
        question = row["question"]
        answer = row["answer"]

        # Create a dictionary for the question-answer pair
        question_answer = {
            "@type": "Question",
            "name": question,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": answer
            }
        }

        # Append the question-answer pair to the mainEntity
        faq_schema["mainEntity"].append(question_answer)

    return json.dumps(faq_schema, indent=4)


st.set_page_config(page_title="FAQ creator", page_icon=":question:")

st.title("Convert Excel files to SEO FAQ markup")
st.subheader("Improve search visibility, save time")
st.write("Convert Excel FAQs to SEO-friendly schema with ease. Improve search visibility and save time.")


file_path = st.file_uploader("Select xlsx file:", type=["xlsx"])

try:
    if file_path:
        convert_button = st.button("Convert & Copy to Clipboard ")
        if convert_button:
            faq_schema_json = create_faq_schema(file_path)
            st.success("The FAQ schema was created successfully and copied to the clipboard.", icon="✅")
            st.markdown("validate your structured data here : https://validator.schema.org/")
            st.json(faq_schema_json)
            pyperclip.copy(faq_schema_json)
            pyperclip.paste()
            st.markdown("If you have any questions, contact me on linkedin: https://www.linkedin.com/in/ma-foroutan/ ")
    else:
        st.warning('Please select an Excel file (.xlsx) with two columns, labeled "question" and "answer" respectively.')
except KeyError:
    st.error('Please select an Excel file (.xlsx) with two only columns, labeled "question" and "answer" respectively.')
    image = Image.open('error.jpg')
    st.image(image, caption='How the first row of your Excel file should look.')
    st.markdown("If you have any questions, contact me on linkedin: https://www.linkedin.com/in/ma-foroutan/ ")
except ImportError:
    st.error('Please select an Excel file (.xlsx) with two only columns, labeled "question" and "answer" respectively.')
    image = Image.open('error.jpg')
    st.image(image, caption='How the first row of your Excel file should look.')
    st.markdown("If you have any questions, contact me on linkedin: https://www.linkedin.com/in/ma-foroutan/ ")
