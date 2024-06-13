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

def checkout(skus: str) -> int:
    
    if not isinstance(skus, str):
        # raise ValueError("skus input is not a string")
        return -1
    
    count_items = Counter(skus)
    item_names = count_items.keys()
    for i in item_names:
        if i not in ("A", "B", "C", "D", "E"):
            return -1

    total_price = 0
    for item in ("A", "C", "D"):
        if item=="A":
            A = count_items["A"]
            A_5_offer = A // 5
            A_3_offer = (A % 5) // 3
            A_nooffer = A - A_5_offer * 5 - A_3_offer * 3
            print(A_5_offer, A_3_offer, A_nooffer)
            total_price += A_5_offer * 200
            total_price += A_3_offer * 130
            total_price += A_nooffer * 50
            
        elif item == "C":
            total_price += 20 * count_items["C"]
            
        elif item == "D":
            total_price += 15 * count_items["D"]
            
    # work out E offers and B offers and calculate the minimum
    
    # calculate B's first and let remainder be for E offer
    # compare to E offer first and put remainder Bs in B offer..
    
    B = count_items["B"]
    E = count_items["E"]
    
    print(total_price)
    # e first:
    def calc_e_first(B, E):
        price = 0
        free_bs = E // 2
        paid_bs = B - free_bs
        offer_bs = paid_bs // 2
        normal_bs = paid_bs % 2
        price += 40 * E
        price += offer_bs * 45
        price += normal_bs * 30
        print("n, o, f, p")
        print(normal_bs, offer_bs, free_bs, paid_bs)
        print("e first price", price)
        return price
    
    def calc_b_first(B, E):
        price = 0
        offer_bs = B // 2
        normal_bs = B % 2
        potential_free_bs = E // 2
        paid_bs = normal_bs - potential_free_bs
        if paid_bs <0:
            paid_bs=0
        
        price += 40 * E
        price += offer_bs * 45
        price += paid_bs * 30
        print("b first price", price)
        return price
    
    e_first = calc_e_first(B, E)
    b_first = calc_b_first(B, E)
    
    if e_first > b_first:
        total_price += b_first
    else:
        total_price += e_first
            
    return total_price
    
    




