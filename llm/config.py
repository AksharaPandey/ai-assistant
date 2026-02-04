import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm_response(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    # UPDATED FOR FEB 2026: Using the current stable gemini-2.5-flash model
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        
        if response.status_code == 200:
            # Check for valid candidates in response
            if 'candidates' in data and len(data['candidates']) > 0:
                return data['candidates'][0]['content']['parts'][0]['text']
            return "unknown"
        else:
            # Extract specific error message if available
            error_msg = data.get('error', {}).get('message', 'Unknown API Error')
            print(f"DEBUG API ERROR: {error_msg}")
            return "error"
            
    except Exception as e:
        print(f"DEBUG CONNECTION ERROR: {e}")
        return "error"