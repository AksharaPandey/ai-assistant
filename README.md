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
```

## 🚀 Getting Started

### 1️⃣ Prerequisites
Ensure you have Python 3.10 or higher installed. You can verify this by running:

```bash
python --version
```
### 2️⃣ Installation

Clone the repository and install the necessary dependencies using the following commands:

```Bash
pip install -r requirements.txt
```
### 3️⃣ Setup Environment Variables 🔑

This project uses environment variables to keep API keys secure.

Create a .env file in the root directory.

Add your keys as follows:

Code snippet
```bash
GEMINI_API_KEY=your_actual_gemini_key
WEATHER_API_KEY=your_actual_weather_key
```
### 4️⃣ Running the Application

To start the assistant and begin interacting with the agents, run the main entry point:

```Bash
python main.py
```


