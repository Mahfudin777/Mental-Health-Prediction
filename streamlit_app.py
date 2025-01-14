import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
import altair as alt
import joblib
from googletrans import Translator
st.title("💬 Mental Health Detection")

# Load the prediction model
pipe_lr = joblib.load(open("model/text_prediction.pkl", "rb"))


def predict_text(docx):
    results = pipe_lr.predict([docx])
    return results[0]

def get_prediction_proba(docx):
    results = pipe_lr.predict_proba([docx])
    return results

def main():
    st.title("Mental Health Detection")
    st.subheader("Detect Mental Health In Text")

    with st.form(key='my_form'):
        raw_text = st.text_area("Type Here")
        submit_text = st.form_submit_button(label='Submit')
    

    if submit_text:
        col1, col2 = st.columns(2)

        # Make predictions
        prediction = predict_text(raw_text)
        probability = get_prediction_proba(raw_text)
        confidence = np.max(probability)
        proba_df = pd.DataFrame(probability, columns=pipe_lr.classes_)
        proba_df_clean = proba_df.T.reset_index()
        proba_df_clean.columns = ["status", "probability"]

        # Insert prediction into the database


        with col1:
            st.success("Original Text")
            st.write(raw_text)

            st.success("Prediction")
            st.success("Status: {}".format(prediction))
            st.success("Confidence: {:.2f}".format(confidence))
            st.write(proba_df_clean)

        with col2:
            st.success("Prediction Probability")
            fig = alt.Chart(proba_df_clean).mark_bar().encode(x='status', y='probability', color='status')
            st.altair_chart(fig, use_container_width=True)

if __name__ == '__main__':
    main()

