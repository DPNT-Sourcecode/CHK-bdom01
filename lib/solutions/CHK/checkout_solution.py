from collections import Counter
from .offers import offers
import re

def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1

    # Define prices and special offers
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60,
        'K': 80, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 30, 'T': 20,
        'U': 40, 'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50
    }

    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'E': [(2, 80)],  # buy 2E, get one B free
        'F': [(3, 20)],  # buy 2F, get one F free
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'N': [(3, 120)],  # buy 3N, get one M free
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'R': [(3, 150)],  # buy 3R, get one Q free
        'U': [(4, 120)],  # buy 3U, get one U free
        'V': [(3, 130), (2, 90)],
    }

    # Count occurrences of each SKU
    from collections import Counter
    item_counts = Counter(skus)

    # Check for invalid items
    for item in item_counts:
        if item not in prices:
            return -1

    # Calculate total price
    total = 0

    # Apply special offers where possible
    for item, count in item_counts.items():
        if item in offers:
            item_total = 0
            for offer in sorted(offers[item], key=lambda x: -x[0]):  # Sort offers by quantity descending
                while count >= offer[0]:
                    item_total += offer[1]
                    count -= offer[0]
            item_total += count * prices[item]  # Add the remaining items at regular price
            total += item_total
        else:
            total += count * prices[item]

    # Apply dependent offers like E and N separately
    if 'E' in item_counts and 'B' in item_counts:
        free_bs = item_counts['E'] // 2
        item_counts['B'] = max(0, item_counts['B'] - free_bs)
    
    if 'N' in item_counts and 'M' in item_counts:
        free_ms = item_counts['N'] // 3
        item_counts['M'] = max(0, item_counts['M'] - free_ms)
    
    if 'R' in item_counts and 'Q' in item_counts:
        free_qs = item_counts['R'] // 3
        item_counts['Q'] = max(0, item_counts['Q'] - free_qs)

    # Recalculate total price for dependent offers
    for item, count in item_counts.items():
        total += count * prices[item]

    return total
    
    



