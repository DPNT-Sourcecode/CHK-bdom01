from collections import Counter
from .offers import offers
import re

def checkout(skus: str) -> int:
    
    price_table = {
        'A': {'price': 50, 'offers': [(5, 200), (3, 130)]},
        'B': {'price': 30, 'offers': [(2, 45)]},
        'C': {'price': 20, 'offers': []},
        'D': {'price': 15, 'offers': []},
        'E': {'price': 40, 'offers': []},
        'F': {'price': 10, 'offers': []},
        'G': {'price': 20, 'offers': []},
        'H': {'price': 10, 'offers': [(10, 80), (5, 45)]},
        'I': {'price': 35, 'offers': []},
        'J': {'price': 60, 'offers': []},
        'K': {'price': 80, 'offers': [(2, 150)]},
        'L': {'price': 90, 'offers': []},
        'M': {'price': 15, 'offers': []},
        'N': {'price': 40, 'offers': []},
        'O': {'price': 10, 'offers': []},
        'P': {'price': 50, 'offers': [(5, 200)]},
        'Q': {'price': 30, 'offers': [(3, 80)]},
        'R': {'price': 50, 'offers': []},
        'S': {'price': 30, 'offers': []},
        'T': {'price': 20, 'offers': []},
        'U': {'price': 40, 'offers': []},
        'V': {'price': 50, 'offers': [(3, 130), (2, 90)]},
        'W': {'price': 20, 'offers': []},
        'X': {'price': 90, 'offers': []},
        'Y': {'price': 10, 'offers': []},
        'Z': {'price': 50, 'offers': []}
    }
    
    
    if not isinstance(skus, str):
        return -1
    
    # Count the occurrence of each item
    item_counts = Counter(skus)
    
    total_price = 0

    # Calculate the price for each item considering the offers
    for item, count in item_counts.items():
        if item in price_table:
            item_price = price_table[item]['price']
            offers = sorted(price_table[item]['offers'], reverse=True, key=lambda x: x[1])  # Sort offers by savings
            
            for offer in offers:
                offer_count, offer_price = offer
                if count >= offer_count:
                    num_offers = count // offer_count
                    total_price += num_offers * offer_price
                    count -= num_offers * offer_count

            total_price += count * item_price
    
    return total_price
    
    



