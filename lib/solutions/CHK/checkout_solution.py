from collections import Counter

def checkout(skus: str) -> int:
    
    if not isinstance(skus, str):
        return -1
    
    count_items = Counter(skus)
    item_names = count_items.keys()
    for i in item_names:
        if i not in ("A", "B", "C", "D", "E", "F"):
            return -1

    total_price = 0
    for item in ("A", "C", "D", "F"):
        if item=="A":
            A = count_items["A"]
            A_5_offer = A // 5
            A_3_offer = (A % 5) // 3
            A_nooffer = A - A_5_offer * 5 - A_3_offer * 3
            total_price += A_5_offer * 200
            total_price += A_3_offer * 130
            total_price += A_nooffer * 50
            
        elif item == "C":
            total_price += 20 * count_items["C"]
            
        elif item == "D":
            total_price += 15 * count_items["D"]
            
        elif item == "F":
            
            # set of every 3 under off
            f_offer = count_items["F"] // 3
            
            # however many not in three not under offer
            f_nooffer = count_items["F"] % 3
            total_price += f_nooffer * 10
            print(f_offer)
            total_price += f_offer * 10 * 2
            
    
    B = count_items["B"]
    E = count_items["E"]
    
    def calc_e_first(B, E):
        price = 0
        free_bs = E // 2
        paid_bs = B - free_bs
        if paid_bs < 0:
            paid_bs=0
        offer_bs = paid_bs // 2
        normal_bs = paid_bs % 2
        price += 40 * E
        price += offer_bs * 45
        price += normal_bs * 30
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
        return price
    
    e_first = calc_e_first(B, E)
    b_first = calc_b_first(B, E)
    
    if e_first > b_first:
        total_price += b_first
    else:
        total_price += e_first
            
    return total_price
    
    