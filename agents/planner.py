import os
from llm.config import get_llm_response
def plan_task(user_query):
    prompt = f"""
    You are an intelligent assistant. 
    User Query: "{user_query}"

    Pick the best tool:
    1. search_github - For code, repos, or developer info.
    2. get_weather - For weather, temperature, or forecasts.
    3. general_query - For greetings, general knowledge, or random questions.
    If neither of the first two tools fit, choose "general_query".
    Query: {user_query}

    Respond with ONLY the tool name.
    """
    response = get_llm_response(prompt).lower()
    
    if "github" in response: return "search_github"
    if "weather" in response: return "get_weather"
    return "general_query" # This is our new "Fallback"