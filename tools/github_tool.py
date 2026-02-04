import requests

def search_github(query):
  url = f"https://api.github.com/search/repositories?q={query}&per_page=3"

  try:
    header={'User-Agent': 'AI-Assistant'}
    response = requests.get(url, headers=header)
    response.raise_for_status()
    
    if response.status_code == 200:
      data = response.json()
      repositories = data.get('items', [])
      
      results = []
      for repo in repositories:
        repo_info = {
          'name': repo['name'],
          'full_name': repo['full_name'],
          'description': repo['description'],
          'url': repo['html_url'],
          'stars': repo['stargazers_count'],
          'language': repo['language']
        }
        results.append(repo_info)
      
      return results
    else:
      print(f"GitHub API returned status code {response.status_code}")
      return []
  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    return []