# AI File Organizer using MCP 

An AI-powered file organization assistant built using **Python**, **MCP (Model Context Protocol)**, and **Groq API**.

This project automatically organizes files into categorized folders using natural language commands powered by AI.

---

# Features ✨

- Automatically organizes files by extension
- AI-powered command handling
- MCP-based tool architecture
- Groq LLM integration
- Built completely in Python
- Environment variable support using `.env`

---

# 🧠 How It Works

```text
User Command
     ↓
Groq AI
     ↓
MCP Server
     ↓
Python File Tools
     ↓
Filesystem Automation
```

Example:

```text
User:
Organize my files

AI:
ORGANIZE

✅ Folder organized successfully!
```

---

# 📁 Project Structure

```text
AI-FILE-ORGANIZER-MCP/
│
├── client.py
├── server.py
├── organizer.py
├── requirements.txt
├── .gitignore
├── .env
│
├── tools/
│   ├── __init__.py
│   └── file_tools.py
│
└── test_folder/
  #your files & folders comes here
```

---

# ⚙️ Tech Stack

- Python
- MCP (Model Context Protocol)
- Groq API
- dotenv

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/kaviyadharshini2805/AI-FILE-ORGANIZER-MCP.git
```

---

## 2. Navigate to Project

```bash
cd ai-file-organizer-mcp
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

#  Setup Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Get your API key from:
- Groq Console

---

#  Run the Project

## Start AI Client

```bash
python client.py
```

Then type:

```text
Organize my files
```

---

# 📂 Supported File Types

| Extension | Folder |
|---|---|
| .jpg / .png / .jpeg | Images |
| .pdf | PDFs |
| .txt | Documents |
| .py | Code |

---

# Example Output

```text
Moved catbg.jpg → Images
Moved code.py → Code
Moved KvzAI.pdf → PDFs
Moved notes.txt → Documents
```

---

#  What I Learned

- MCP basics
- Python automation
- Filesystem operations
- AI API integration
- Environment variable handling
- Modular project structuring
- AI-powered automation workflows

---

#  Future Improvements 👍🏻

- Streamlit Web UI
- Drag-and-drop folder uploads
- Semantic file search
- Voice commands
- Duplicate file detection
- Real MCP tool calling
- Scheduler for automatic cleanup

---

# Contributing 🫱🏻‍🫲🏻


Pull requests and suggestions are welcome!

---

#  Acknowledgements

- Groq API
- MCP
- Python

---

# Screenshots
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/9aed6b3d-6075-4c68-b9f1-c0e145e4e784" />
<img width="1918" height="1073" alt="image" src="https://github.com/user-attachments/assets/114bceee-7bc3-4553-995a-08c1f1024220" />
<img width="1916" height="1075" alt="image" src="https://github.com/user-attachments/assets/2d723aca-97a1-4782-9bdd-6b5a673aff49" />
