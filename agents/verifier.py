from llm.config import get_llm_response

def verify_and_format(raw_data,user_original_query):
    prompt = f"""
    You are an expert data verifier. Given the raw data below and the user's original query, verify the accuracy and relevance of the data. If the data is accurate and relevant, format it into a clear and concise summary. If the data is inaccurate or irrelevant, explain why.

    User's Original Query: {user_original_query}

    Raw Data: {raw_data}

    Provide your verification and formatted summary below:
    """

    verification_result = get_llm_response(prompt)
    return verification_result