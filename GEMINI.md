You are a developer agent. Your task is to help build a Study Notes Summarizer & Quiz Generator web app with the following specs:

- Users upload a PDF document.
- The backend extracts text from the PDF (using PyPDF library in Python).
- Upon upload, the agent generates a clean and meaningful summary of the content.
- The summary can be displayed in any UI style (card, block, container, etc.) according to student preferences.
- After summarization, the user can click a "Create Quiz" button.
- The agent reads the original PDF content (not the summary) and generates quiz questions—either 5 MCQs or a mix of quiz types, including options and marking the correct answer.
- The agent should integrate with Context7 MCP server and Gemini CLI for prompt handling.

Your output must:
1. Generate a workflow with clear backend steps and streamlit frontend features.
2. Provide example code snippets for:
    - PDF upload and text extraction (Python, using PyPDF)
    - Interfacing backend with Gemini CLI and Context7 MCP
    - Next.js component for PDF upload, summary/quiz display, and quiz creation button
3. Explain how the backend communicates with Gemini CLI to get summaries/quizzes and returns results to the UI.


