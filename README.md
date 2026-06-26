# AI File Organizer using MCP

An AI-powered file organization assistant built using **Python**, **Model Context Protocol (MCP)**, and the **Groq API**. The application organizes files into categorized folders through natural language commands, demonstrating how Large Language Models can interact with external tools using the MCP architecture.

---

## Overview

This project showcases an AI-driven approach to file management by combining natural language understanding with filesystem automation. User requests are processed by a Large Language Model, routed through an MCP server, and executed using Python-based file management tools.

Instead of manually sorting files, users simply provide a natural language command, and the AI interprets the request before automatically organizing files into appropriate directories.

---

## Features

- Organizes files automatically based on file extensions
- Supports natural language commands
- Built using the Model Context Protocol (MCP)
- Integrates the Groq API for AI-powered command interpretation
- Modular Python architecture
- Environment variable management using `.env`
- Easily extensible for additional tools and file types

---

## System Architecture

```text
          User Command
                │
                ▼
          Groq Language Model
                │
                ▼
            MCP Server
                │
                ▼
      Python File Management Tools
                │
                ▼
      Filesystem Organization

```

## Workflow

1. The user enters a natural language command.
2. The Groq LLM interprets the request.
3. The MCP server maps the request to the appropriate tool.
4. Python executes the required filesystem operations.
5. Files are automatically moved into categorized folders.
6. The result is returned to the user.

---

## Example

### User Input

```text
Organize my files
```

### Output

```text
Folder organized successfully.
```

---

## Project Structure

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
    └── Files to be organized
```

---

## Technology Stack

- Python
- Model Context Protocol (MCP)
- Groq API
- python-dotenv

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/kaviyadharshini2805/AI-FILE-ORGANIZER-MCP.git
```

### Navigate to the Project Directory

```bash
cd AI-FILE-ORGANIZER-MCP
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project directory.

```env
GROQ_API_KEY=your_api_key_here
```

Obtain your API key from the Groq Console.

---

## Running the Application

Start the client application:

```bash
python client.py
```

Then enter a command such as:

```text
Organize my files
```

---

## Supported File Types

| File Extension | Destination Folder |
|----------------|--------------------|
| `.jpg`, `.jpeg`, `.png` | Images |
| `.pdf` | PDFs |
| `.txt` | Documents |
| `.py` | Code |

Additional file types can be added by extending the file organization logic.

---

## Example Output

```text
Moved catbg.jpg   → Images
Moved code.py     → Code
Moved Resume.pdf  → PDFs
Moved notes.txt   → Documents
```

---

## Learning Outcomes

This project provided practical experience with:

- Model Context Protocol (MCP)
- AI-powered tool calling
- Filesystem automation using Python
- Groq API integration
- Environment variable management
- Modular software architecture
- Natural language command processing
- Building AI-assisted automation workflows

---

## Future Enhancements

- Streamlit-based web interface
- Drag-and-drop folder uploads
- Semantic file search
- Voice-controlled commands
- Duplicate file detection
- Advanced MCP tool orchestration
- Scheduled automatic file organization
- Support for custom user-defined categories

---

## Contributing

Contributions are welcome. Feel free to submit issues, feature requests, or pull requests to improve the project.

---

## Acknowledgements

- Groq API
- Model Context Protocol (MCP)
- Python

---

## Screenshots

### Command Interface

<img width="1919" height="1079" alt="AI File Organizer Interface" src="https://github.com/user-attachments/assets/9aed6b3d-6075-4c68-b9f1-c0e145e4e784" />

### File Organization Process

<img width="1918" height="1073" alt="Organization Process" src="https://github.com/user-attachments/assets/114bceee-7bc3-4553-995a-08c1f1024220" />

### Organized Output

<img width="1916" height="1075" alt="Organized Files" src="https://github.com/user-attachments/assets/2d723aca-97a1-4782-9bdd-6b5a673aff49" />

### Project Execution

<img width="1918" height="1078" alt="Project Execution" src="https://github.com/user-attachments/assets/df5b00ac-5e85-4be7-b704-0fdedc3d84fb" />

---

## License

This project is intended for educational and learning purposes.
