# Multi-Agent AI Assistant 🤖
  
**Project Category:** Generative AI / Multi-Agent Systems (2026)

## 📌 Project Overview
This project is a sophisticated Multi-Agent AI Assistant that utilizes a **Planner-Executor-Verifier** architecture. It is designed to handle specialized tasks—such as fetching real-time weather data and searching GitHub repositories—while also maintaining a natural conversational flow for general user queries.

By decoupling the "Thinking" (Planning), "Acting" (Execution), and "Auditing" (Verification) phases, the system ensures high reliability and minimizes LLM hallucinations.



## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Core LLM:** Google Gemini 2.5 Flash (via Google AI Studio)
* **External APIs:**
    * **OpenWeatherMap API:** Real-time global meteorological data.
    * **GitHub REST API:** Code repository and developer data.
* **Libraries:** `requests`, `python-dotenv`

## 📂 Project Structure
```text
ai_assistant/
├── .env                 # Secret keys (Gemini, Weather API)
├── main.py              # Entry point of the application
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── agents/
│   ├── planner.py       # Logic for task classification & tool selection
│   ├── executor.py      # Logic for tool invocation & data retrieval
│   └── verifier.py      # Logic for data validation & final formatting
├── llm/
│   └── config.py        # Centralized Gemini API & endpoint configuration
└── tools/
    ├── weather_tool.py  # OpenWeatherMap API implementation
    └── github_tool.py   # GitHub repository search implementation



