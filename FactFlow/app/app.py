import streamlit as st, pickle, sys, os
sys.path.append(os.path.abspath('../src'))

from preprocessing import clean_text
from web_agent import retrieve
from summarizer import summarize_hits

st.set_page_config(page_title="FactFlow", page_icon="🧠", layout="wide")
st.title("🧠 FactFlow — Fake News Detection + Evidence Summarizer")

# Load model + vectorizer
with open('../models/fake_news_model.pkl','rb') as f: model = pickle.load(f)
with open('../models/vectorizer.pkl','rb') as f: vectorizer = pickle.load(f)

st.text_area("Enter claim/article text:", key="input")

if st.button("Analyze"):
    text = st.session_state.input.strip()
    if not text:
        st.warning("Please enter something.")
    else:
        cleaned = clean_text(text)
        vec = vectorizer.transform([cleaned])
        pred = model.predict(vec)[0]
        prob = model.predict_proba(vec)[0][1]
        label = "🟥 Fake" if pred==1 else "🟩 Real"
        st.markdown(f"### Prediction: {label} (Fake Probability: {prob*100:.2f}%)")

        with st.spinner("Retrieving supporting evidence..."):
            hits = retrieve(text)
            summaries = summarize_hits(hits[:3])
            for s in summaries:
                st.write(f"**{s['title']}**")
                st.write(s['summary'])
                st.write(f"[Read more]({s['href']})")