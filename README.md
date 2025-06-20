# 🧪 Scientific Research Assistant

The **Scientific Research Assistant** is an intelligent, interactive application designed to assist researchers, reviewers, and academics in streamlining the peer review and literature analysis process. This assistant provides functionalities such as literature summarization, peer review generation, and citation intelligence — all powered by large language models (LLMs).

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

## 🧰 Suggested Tech Stack

### Frontend
- 🧪 **Streamlit** for rapid MVP prototyping
- ⚛️ **React + FastAPI** for production deployments

### Backend
- 🔁 `LangChain`, `LlamaIndex`, or `Haystack` for LLM integration
- 📁 `FAISS` or `ChromaDB` for vector store and citation retrieval
- 🗄️ `PostgreSQL` or `SQLite` for metadata and storage

### Language Models
- 🔥 **OpenAI GPT-4o** or **GPT-4-turbo**
- 🧠 **Claude 3** (Anthropic) for high-fidelity summarization
- 🦙 **Mistral** or **LLaMA3** for private/local model deployment

---

## 🚀 Project Roadmap

### ✅ Phase 1 (MVP): Local PDF Summarizer
- Upload scientific paper (PDF)
- Output structured summary (IMRaD format)
- Highlight key findings & limitations

### ✅ Phase 2: Peer Review Generator
- Add review input fields: journal name, tone, length
- Generate full-text peer review
- Option to batch upload multiple papers

### ✅ Phase 3: Citation Intelligence
- Extract and analyze references from PDF
- Enrich metadata via APIs
- Flag:
  - Self-citations
  - Missing landmark papers
  - Weak or outdated references

### ✅ Phase 4: Export & Personalization
- Export output as `.docx` or `.pdf`
- Save and version control summaries & reviews
- Enable “review style presets” (e.g., NIH reviewer, clinician, statistician)

---

## 🔒 Optional Advanced Features
- On-device LLMs via **Ollama**, **Mixtral**, or **LLaMA3**
- Chat with a research paper using **RAG** over vectorized content
- Cross-paper comparison (for systematic reviews)
- Integration with **Zotero** or **EndNote** for citation syncing

---

## 📦 Installation (Coming Soon)

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
