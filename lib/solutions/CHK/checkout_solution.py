from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    count_items = Counter(skus)
    total_price = 0
    for item in ("A", "B", "C", "D"):
        if item=="A":
            offers_price = (count_items["A"] // 3) * 130
            no_offers_price = (count_items["A"] % 3) * 50
            total_price += offers_price
            total_price += no_offers_price
        elif item == "B":    
            offers_price = (count_items["B"] // 2) * 45
            no_offers_price = (count_items["B"] % 2) * 30
            total_price += offers_price
            total_price += no_offers_price
        elif item == "C":
            total_price += 20 * count_items["C"]
            
        elif item == "D":
            total_price += 15 * count_items["D"]

    return total_price
    
    

