import requests 
import csv 
import random
from bs4 import BeautifulSoup 

url = "https://www.irates.am/hyR/feed" 

# Add headers to pretend we are a browser by using a random user agent
with open('user_agents.txt') as file:
    user_agents_list = [line.strip() for line in file if line.strip()]

random_user_agent = random.choice(user_agents_list)

headers = {'User-Agent': random_user_agent} 

# Get the html page 
response = requests.get(url=url,  headers=headers, timeout=(5,15))
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

# Find all news
news_items = soup.find_all('div', class_='listing-right')
print(f"Found {len(news_items)} news items:\n")

# Open file ONCE for writing
with open('irates.csv', 'w', encoding='utf-8', newline='') as f: 
    writer = csv.writer(f)
    
    # Write header
    writer.writerow(['Number', 'Title', 'Description', 'Date', 'Time', 'Link'])
    
    # Extract info from each news item
    for i, item in enumerate(news_items, 1):
        # Get title
        title_div = item.find('h2')
        title = title_div.get_text(strip=True) if title_div else "No title"

        #Get description 
        descr_div = item.find('div', class_='listing-descr')
        description = descr_div.get_text(strip=True) if descr_div else "No description"
        
        # Get link
        if title_div:
            link_tag = title_div.find('a')
            if link_tag:
                link = "https://irates.am/" + link_tag['href']
            else:
                link = "No link"
        else:
            link = "No link"
        
        # Get date and time
        date_span = item.find('span', class_='listing-date')
        time_span = item.find('span', class_='listing-time')
        date = date_span.get_text(strip=True) if date_span else "No date"
        news_time = time_span.get_text(strip=True) if time_span else "No time"
        
        # Print to console
        print(f" {i}. {title}\n")
        print(f" News summary: {description}")
        print(f" Date: {date} {news_time}")
        print(f" Link: {link}")
        
        # Write to CSV
        writer.writerow([i, title, description, date, news_time, link])

print("Data saved to irates.csv")
