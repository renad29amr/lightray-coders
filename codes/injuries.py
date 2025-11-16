import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://www.planetfootball.com/premier-league/2024-25-premier-league-injury-table-man-utd-liverpool-arsenal-chelsea"  
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

data = []
current_club = None

pattern = re.compile(r"^(.*?)\s*\((.*?),\s*(.*?)\)$")

for tag in soup.find_all(['h2', 'p']):
    if tag.name == "h2":
        text = tag.get_text(strip=True)
        if "–" in text:
            current_club = text.split("–")[0].strip()
    
    if tag.name == "p" and current_club:
        lines = tag.get_text(strip=True).split("<br>")
        lines = re.split(r'\n|<br>|<br/>', tag.decode_contents())

        for line in lines:
            clean = BeautifulSoup(line, "html.parser").get_text(strip=True)
            if not clean:
                continue

            match = pattern.match(clean)
            if match:
                player = match.group(1).strip()
                injury = match.group(2).strip()
                date = match.group(3).strip()

                data.append([current_club, player, injury, date])

with open("premier_league_injuries.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Club", "Player", "InjuryType", "ReturnDate"])
    writer.writerows(data)

print("DONE! premier_league_injuries.csv")


