import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get product title
def get_title(soup):
    try:
        title = soup.find("span", {"id": "productTitle"}).get_text(strip=True)
        return title
    except AttributeError:
        return "Title not available"

# Function to get product price
def get_price(soup):
    try:
        price = soup.find("span", {"class": "a-price-whole"}).get_text(strip=True)
        return price
    except AttributeError:
        return "Price not available"

# Function to get product rating
def get_rating(soup):
    try:
        rating = soup.find("span", {"class": "a-icon-alt"}).get_text(strip=True)
        return rating
    except AttributeError:
        return "Rating not available"

# Function to get product review count
def get_review_count(soup):
    try:
        review_count = soup.find("span", {"id": "acrCustomerReviewText"}).get_text(strip=True)
        return review_count
    except AttributeError:
        return "Review count not available"

# Function to get product availability
def get_availability(soup):
    try:
        availability = soup.find("div", {"id": "availability"}).find("span").get_text(strip=True)
        return availability
    except AttributeError:
        return "Availability not available"

# Function to scrape a product page
def scrape_product(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US, en;q=0.5"
    }

    # Send HTTP request
    webpage = requests.get(URL, headers=headers)
    
    # Check if the request was successful
    if webpage.status_code != 200:
        return ["Failed to retrieve page", "N/A", "N/A", "N/A", "N/A"]

    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(webpage.content, "lxml")
    
    # Extract product information
    product_title = get_title(soup)
    product_price = get_price(soup)
    product_rating = get_rating(soup)
    product_review_count = get_review_count(soup)
    product_availability = get_availability(soup)

    # Return the product details
    return [product_title, product_price, product_rating, product_review_count, product_availability]

# Main script
if __name__ == "__main__":

    # List of URLs to scrape
    urls = [
        "https://www.amazon.com/Janasya-Indian-Lehenga-Dupatta-J0484-LCD-XL/dp/B0BLYQZTL6/",
        "https://www.amazon.com/Generic-Designer-Readymade-Navratri-Partywear/dp/B0CRNRLJ8J/",
        "https://www.amazon.com/STELLACOUTURE-indian-lehenga-flared-stitched/dp/B0CX5Q2172/",
        "https://www.amazon.com/Ethnovog-Embroidered-Sequins-Umbrella-Gorgeous/dp/B0D8J6NXW1/",
        "https://www.amazon.com/Nivah-Fashion-Georgette-Embroidered-Anarkali/dp/B081L5PW1M/",
        "https://www.amazon.com/Afibi-Length-Blending-Chiffon-Design/dp/B01FP2SXHE/",
        "https://www.amazon.com/Traditional-Partywear-Navratri-Wedding-Stitched/dp/B0CTQ5CKFG/",
        "https://www.amazon.com/TRENDMALLS-Embroidery-Lehenga-Dupatta-L144-New-Bridal-Latest-Wedding-Sequnce-Lehenga-White-Designer-Free/dp/B0C53VLJX4/",
        "https://www.amazon.com/STELLACOUTURE-indian-lehenga-flared-stitched/dp/B0D7HZSPXV/",
        "https://www.amazon.com/TRENDMALLS-Georgette-Embroidery-Anarkali-USTM-G62-Morpeach-L/dp/B0BB1YVJB4/",
        "https://www.amazon.com/stylishfashion-Bollywood-Designer-Pakistani-Beautiful/dp/B0CBQ17ZFD/",
        "https://www.amazon.com/TRENDMALLS-Embroidery-Sequence-Women-L66-White-XXL-Wedding-Bridal-Latest-Lehenga-Choli/dp/B0D6Y7HYH4/"
    ]

    # Create an empty list to store product data
    data = []

    # Loop over each URL and scrape product details
    for url in urls:
        product_data = scrape_product(url)
        data.append(product_data)  # Append each product's data to the list

    # Create a DataFrame using the collected data
    df = pd.DataFrame(data, columns=["Title", "Price", "Rating", "Review Count", "Availability"])

    # Save the data to a CSV file
    df.to_csv("amazon_products.csv", index=False)
    print("Data saved to amazon_products.csv")


 
