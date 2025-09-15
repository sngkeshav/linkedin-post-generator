# LinkedIn Post Generator

This project helps preprocess and analyze LinkedIn posts using **LangChain** and **Groq’s LLaMA 3.3 70B Versatile** model.  
It extracts metadata (line count, language, tags), unifies tags, and prepares posts for further use.  
The project also provides a **Streamlit UI** for running the pipeline interactively.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone git@github.com:sngkeshav/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2. Set up a virtual environment and install dependencies
```bash
python3 -m venv venv
source venv/bin/activate   # for macOS / Linux
venv\Scripts\activate      # for Windows PowerShell
pip install -r requirements.txt
```

### 3. Set up environment variables
```bash
# Create a .env file in the project root and add your API key:
API_KEY=your_api_key_here
```

### ▶️ Running the Application
```bash
# After activating your virtual environment:
streamlit run main.py