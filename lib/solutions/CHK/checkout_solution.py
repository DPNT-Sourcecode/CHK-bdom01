from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
# def checkout(skus):
    
#     if not isinstance(skus, str):
#         # raise ValueError("skus input is not a string")
#         return -1
    
#     count_items = Counter(skus)
#     item_names = count_items.keys()
#     for i in item_names:
#         if i not in ("A", "B", "C", "D"):
#             return -1
    
#     total_price = 0
#     for item in ("A", "B", "C", "D"):
#         if item=="A":
#             offers_price = (count_items["A"] // 3) * 130
#             no_offers_price = (count_items["A"] % 3) * 50
#             total_price += offers_price
#             total_price += no_offers_price
            
#         elif item == "B":    
#             offers_price = (count_items["B"] // 2) * 45
#             no_offers_price = (count_items["B"] % 2) * 30
#             total_price += offers_price
#             total_price += no_offers_price
            
#         elif item == "C":
#             total_price += 20 * count_items["C"]
            
#         elif item == "D":
#             total_price += 15 * count_items["D"]

#     return total_price


# logic:
    # do A offers
    # do E offers 
    # do rest

def checkout(skus):
    
    if not isinstance(skus, str):
        # raise ValueError("skus input is not a string")
        return -1
    
    count_items = Counter(skus)
    item_names = count_items.keys()
    for i in item_names:
        if i not in ("A", "B", "C", "D", "E"):
            return -1

    total_price = 0
    for item in ("A", "B", "C", "D", "E"):
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
    
    