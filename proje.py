dict_of_items_and_prices = {
    'sugar': [50, 131], 'sliced bread': [200, 311], 'unsliced bread': [150, 229], 'egg': [50, 545],
    'tin three crown': [150, 201], 'tin peak milk': [120, 230], 'sachet peak milk': [50, 791],
    'sachet bournvita': [50, 611], 'tin milo': [500, 367], 'large sachet peak': [700, 889],
    'large sachet milo': [700, 934], 'large bournvita': [100, 758], 'small sachet custard': [200, 383],
    'small sachet corn flakes': [150, 647], 'small golden more': [100, 121], 'small waw': [120, 198],
    'small aeriel': [115, 354], 'big waw': [200, 323], 'big aerial': [250, 222], 'big corn flakes': [750, 341],
    'large golden more': [650, 458], 'small sprite': [80, 134], 'small pepsi': [80, 674], 'small fanta': [80, 757],
    'small lacasera': [80, 127], 'big sprite': [150, 956], 'big pepsi': [150, 374], 'big fanta': [150, 267],
    'big lacasera': [150, 786], 'big coke': [150, 546]
    }
sales_today = {}
prie = []


def call_item_and_price():
    item = input("what quantity's price do want to change > ")
    price = int(input("The price to change it to > "))
    return item, price


def change_price(item, price):
    if item.lower() in dict_of_items_and_prices.keys():
        dict_of_items_and_prices[item.lower()][0] = price
        return dict_of_items_and_prices
    else:
        print("the item is not available in the store.")


def call_item_price_and_quantity():
    item = input("what item do you want to add > ")
    price = int(input("the price > "))
    quantity = int(input("the quantity available > "))
    return item, price, quantity


def add_more_items(item, price, quantity):
    if item.lower() not in dict_of_items_and_prices.keys():
        dict_of_items_and_prices[item] = [price, quantity]
        return dict_of_items_and_prices
    else:
        print("The item name \"" + item.upper() + "\" already exists.")


def price_of_good_purchased():
    dict_for_customer = {}
    item = input("input commodity: ")
    # price = 0
    sum_of_price = 0
    sum_quantities = 0
    list_quantity = []
    # vat = 0
    while item in dict_of_items_and_prices.keys():
        quantity = int(input("how many: "))
        dict_of_items_and_prices[item][1] = dict_of_items_and_prices[item][1] - quantity
        list_quantity.append(quantity)
        price = quantity * dict_of_items_and_prices[item][0]
        sum_quantities += quantity
        if sum_quantities < 5:
            vat = .2 * price
        elif sum_quantities > 10:
            vat = 0.3 * price
        else:
            vat = 0
        sum_of_price += price + vat
        dict_for_customer[item] = [price, vat]
        sales_today[item] = quantity
        item = input("enter commodity: ")
    else:
        print("item not available.")
    for val in dict_for_customer.keys():
        if dict_of_items_and_prices[val][0] > 100 and sum_quantities > 10:
            sum_of_price = sum_of_price - 800
            break
    sum_vat = 0
    print(dict_for_customer)
    print("\n Your receipt is below.")
    print("".center(70, "-"))
    print("".center(70, "-"))
    print("Items                    Quantity             Amount(#)")
    for items, quant in zip(dict_for_customer.keys(), list_quantity):
        sum_vat += dict_for_customer[items][1]
        print(items.ljust(23, " "), str(quant).center(10, " "), str(dict_for_customer[items][0]).rjust(16, " "))
    del dict_for_customer
    print("\nVAT: #" + str(sum_vat))
    if sum_quantities > 10:
        print("\nDiscount: #800")
    print("\nTotal Amount you are paying is: #" + str(sum_of_price))
    prie.append(sum_of_price)
    print("".center(70, "-"))
    print("".center(70, "-"))
    # print(list_quantity)
    return dict_of_items_and_prices


whi = input("Are you the Admin or User? (A/U) > ")
while True:
    if whi.lower() == "a":
        what_to_do = input("what do you want to do?\n1. change price \n2. see sales today\n3. Add items\n")
        if what_to_do == "1":
            x, y = call_item_and_price()
            changed = change_price(x, y)
            print(changed)

        elif what_to_do == "2":
            print("Goods                      quantity")
            for itr, itr_quantity in zip(sales_today.keys(), sales_today.values()):
                print(str(itr).ljust(30, " "), itr_quantity)
            sume = 0
            for y in prie:
                sume += y
            print("Total amount of sales made today is #" + str(sume))
        elif what_to_do == "3":
            a, b, c = call_item_price_and_quantity()
            added_item = add_more_items(a, b, c)
        else:
            break
    elif whi.lower() == 'u':
        user_menu = input("what do you want to do > \n 1. Buy Items \n2. exit \n")
        if user_menu == '1':
            i = 1
            while True:
                inputs = input("Enter any word to initiate a new customer's list except close > ")
                if inputs == "close":
                    break
                else:
                    print("The items available for sale are as follows with their prices in front :")
                    print("".center(70, "="))
                    print('s/n                 items', '                       Price')
                    print("".center(70, "="))
                    for keys, values in zip(dict_of_items_and_prices.keys(), dict_of_items_and_prices.values()):
                        print(i, keys.center(40, " "), '#' + str(values[0]).ljust(15, " "))
                        i += 1
                    dict_of_cus = price_of_good_purchased()
                    print(dict_of_cus)
                    i = 1
        elif user_menu == '2':
            break
        whi = input("Are you the Admin or User? (A/U) > ")
    else:
        break
