import requests
from bs4 import BeautifulSoup


def scrape_url(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            final  = []
            for label in soup.find_all('article', class_='Box-row'):
                string = str(label.text).strip()
                string = string.replace('\n', '')
                final.append(string.split('  ')[0])
            return final
        else:
            return f"Failed to retrieve the webpage. Status code: {response.status_code}"

    except Exception as e:
        print(f"An error occurred: {e}")

def return_last_issue(url):
    return scrape_url(url)[0]

def main():
    url_to_scrape = "https://github.com/CircuitVerse/CircuitVerse/contribute"
    
    for ele in scrape_url(url_to_scrape):
        print(ele)
        
if __name__ == "__main__":
    main()