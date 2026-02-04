from tools.github_tool import search_github
from tools.weather_tool import get_weather
from llm.config import get_llm_response

def execute_task(decision, user_query):
    if decision == "search_github":
        return search_github(user_query)
    elif decision == "get_weather":
        return get_weather(user_query)
    else:
        # Fallback: Just let the LLM answer the question
        return get_llm_response(f"Answer this user query politely: {user_query}")