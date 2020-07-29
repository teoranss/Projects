DEFAULT_SHOPS =(
    {'Lego': 50, 'Hotwheels':60, 'Barbie': 30, 'jucarie1': 30},
    {'Lego': 60, 'Hotwheels':55, 'Barbie': 25, 'jucarie2': 31},
    {'Lego': 55, 'Hotwheels':70, 'Barbie': 14, 'jucarie3': 32},)

def best_buy(*args:dict, to_buy: dict = None) -> int:
    """Function to calculate best price in shop
    :param args: dict with shop items
    :param to_buy: list with shopping information
    :return: int best price of all shops
    """
    best_price = None
    for magazin in args:
        print(magazin)
        pret_total = 0
        for nume_jucarie, numar_jucarie in to_buy.items():
            print(nume_jucarie, numar_jucarie)
            pret_total += to_buy[nume_jucarie]*magazin[nume_jucarie]
            print(pret_total)
        if best_price:
            if best_price < pret_total:
                pass
            else:
                best_price = pret_total
        else:
            best_price = pret_total
        print(best_price)



