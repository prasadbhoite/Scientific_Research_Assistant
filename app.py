# main.py
import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from utils.llm import summarize_text, generate_review, analyze_citations

# Set Streamlit page config FIRST
st.set_page_config(page_title="🔬 Scientific Research Assistant", layout="wide")



# -- API Key Authentication --
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

st.title("🔒 Scientific Research Assistant Login")

if not st.session_state.api_key:
    api_key_input = st.text_input("Enter your OpenAI API key:", type="password")
    if st.button("Submit"):
        if api_key_input.startswith("sk-"):
            st.session_state.api_key = api_key_input
        else:
            st.error("Please enter a valid OpenAI API key.")
    st.stop()

# -- App Content After Auth --
st.title("🔬 Scientific Research Assistant")

uploaded_file = st.file_uploader("Upload a scientific paper (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        paper_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Extracted Content Preview")
    st.text_area("Raw Text (first 1000 chars)", paper_text[:1000], height=200)

    tab1, tab2, tab3 = st.tabs(["📚 Summary", "🧑‍⚖️ Peer Review", "🔗 Citation Analysis"])

    with tab1:
        st.subheader("📚 Literature Summary")
        if st.button("Generate Summary"):
            with st.spinner("Summarizing paper..."):
                summary = summarize_text(paper_text)
            st.success("Summary generated!")
            st.markdown(summary)

    with tab2:
        st.subheader("🧑‍⚖️ Peer Review Generator")
        tone = st.selectbox("Select Review Tone", ["Neutral", "Critical", "Supportive"])
        if st.button("Generate Review"):
            with st.spinner("Generating peer review..."):
                review = generate_review(paper_text, tone)
            st.success("Review generated!")
            st.markdown(review)

    with tab3:
        st.subheader("🔗 Citation Analysis")
        if st.button("Analyze Citations"):
            with st.spinner("Extracting and analyzing references..."):
                citations = analyze_citations(paper_text)
            st.success("Citation analysis complete!")
            st.markdown(citations)
