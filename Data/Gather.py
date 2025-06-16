from bs4 import BeautifulSoup
import requests

thunder_data = 'https://www.espn.com/nba/team/stats/_/name/okc/season/2025/seasontype/2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
data = requests.get(thunder_data, headers=headers)



soup = BeautifulSoup(data.content, 'html.parser')
print(soup.prettify())
