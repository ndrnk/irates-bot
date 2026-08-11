import requests 
import csv 
from bs4 import BeautifulSoup 

url = "https://irates.am/hy/feed" 

# Add headers to pretend we are a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
} # 

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

# Find all news items
news_items = soup.find_all('li', class_='listing-descr')

print(f"Found {len(news_items)} news items:\n")

# Open file ONCE for writing
with open('irates.csv', 'w', encoding='utf-8', newline='') as f: 
    writer = csv.writer(f)
    
    # Write header
    writer.writerow(['Number', 'Title', 'Date', 'Time', 'Link'])
    
    # Extract info from each news item
    for i, item in enumerate(news_items, 1):
        # Get title
        title_span = item.find('span', class_='scroll-right-n')
        title = title_span.get_text(strip=True) if title_span else "No title"
        
    # Get link
        link_tag = item.find('a')
        if link_tag:
            link = "https://irates.am/" + link_tag['href']
        else:
            link = "No link"
        
        # Get date and time
        date_span = item.find('span', class_='feedDate')
        time_span = item.find('span', class_='feedTime')
        date = date_span.get_text(strip=True) if date_span else "No date"
        time = time_span.get_text(strip=True) if time_span else "No time"
        
        # Print to console
        print(f"{i}. {title}")
        print(f"   Date: {date} {time}")
        print(f"   Link: {link}\n")
        
        # Write to CSV
        writer.writerow([i, title, date, time, link])

print("Data saved to irates.csv")
