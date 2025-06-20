# 🧪 Scientific Research Assistant

The **Scientific Research Assistant** is an intelligent, interactive application designed to assist researchers, reviewers, and academics in streamlining the peer review and literature analysis process. This assistant provides functionalities such as literature summarization, peer review generation, and citation intelligence — all powered by OPEN AI's gpt-4o [large language model (LLMs)].

---

## 🔍 Core Functionalities

### 1. 📚 Literature Summarization
- Upload or fetch papers (PDFs, DOIs, or PubMed links).
- Extract and summarize sections such as:
  - Abstract, Introduction, Methods, Results, Conclusion
- Accepts **custom prompts** like:
  - “Summarize limitations”
  - “Extract statistical methods”
- **Tools & Libraries**:
  - `PyMuPDF` or `pdfminer.six` for PDF parsing
  - `LangChain` or `LlamaIndex` for chunking, embedding, and retrieval

---

### 2. 🧑‍⚖️ Peer Review Assistant
- Accepts full manuscript or preprint.
- Generates section-wise critique:
  - Highlights strengths, weaknesses, and suggestions
- Customizable tone: `Neutral`, `Critical`, or `Supportive`
- Supports checklist-based review (e.g., **CONSORT**, **PRISMA**)

---

### 3. 🔗 Citation Analysis
- Extract and list all references from the manuscript.
- For each citation:
  - Check **recency**, **impact factor**, and **PubMed status**
  - Analyze author and regional diversity
  - Identify missing recent/relevant literature
- **APIs & Tools**:
  - `CrossRef API`, `Semantic Scholar API`, `OpenAlex`, `PubMed E-utilities`

---

## 📦 Installation

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set your API key
export OPENAI_API_KEY=your_key_here

# Run the app
streamlit run main.py
