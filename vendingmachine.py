# CODE LAB 1
# ASSESSMENT 2 - UTILITY APP
# TASK: To code a vending machine  

# to begin, a welcome message
print("""\033[31m

░█  ░█ ░█▀▀▀ ░█    ░█▀▀█ ░█▀▀▀█ ░█▀▄▀█ ░█▀▀▀ 　 ▀▀█▀▀ ░█▀▀▀█ 　 ▀▀█▀▀ ░█ ░█ ░█▀▀▀ 　 ░█  ░█ ░█▀▀▀ ░█▄ ░█ ░█▀▀▄ ▀█▀ ░█▄ ░█ ░█▀▀█ 
░█░█░█ ░█▀▀▀ ░█    ░█    ░█  ░█ ░█░█░█ ░█▀▀▀ 　  ░█   ░█  ░█ 　  ░█   ░█▀▀█ ░█▀▀▀ 　  ░█░█  ░█▀▀▀ ░█░█░█ ░█ ░█ ░█  ░█░█░█ ░█ ▄▄ 
░█▄▀▄█ ░█▄▄▄ ░█▄▄█ ░█▄▄█ ░█▄▄▄█ ░█  ░█ ░█▄▄▄ 　  ░█   ░█▄▄▄█ 　  ░█   ░█ ░█ ░█▄▄▄ 　   ▀▄▀  ░█▄▄▄ ░█  ▀█ ░█▄▄▀ ▄█▄ ░█  ▀█ ░█▄▄█ 

░█▀▄▀█  █▀▀█ ░█▀▀█ ░█ ░█ ▀█▀ ░█▄ ░█ ░█▀▀▀ 　 █ 
░█░█░█ ░█▄▄█ ░█    ░█▀▀█ ░█  ░█░█░█ ░█▀▀▀ 　 ▀ 
░█  ░█ ░█ ░█ ░█▄▄█ ░█ ░█ ▄█▄ ░█  ▀█ ░█▄▄▄ 　 ▄
\033[0m""")


print("\033[1m\033[36m\n\t\t\t\tWhat would you like to buy today?\n\033[0m")

# print the menu for the user to choose from
print("""\033[33m
╔════════════════════════════════════════════════════╗
‖     SNACKS      ‖   CODE   ‖   PRICE   ‖   STOCK   ‖
‖════════════════════════════════════════════════════‖
‖ Chips           |    S1    |    £5     |     6     ‖
‖ Chocolate       |    S2    |    £4     |     4     ‖
‖ Biscuits        |    S3    |    £3     |     7     ‖
‖ Cookies         |    S4    |    £7     |     5     ‖
‖ Cake            |    S5    |    £4     |     6     ‖ 
╚════════════════════════════════════════════════════╝
      
╔════════════════════════════════════════════════════╗
‖     DRINKS      ‖   CODE   ‖   PRICE   ‖   STOCK   ‖
‖════════════════════════════════════════════════════‖
‖ Water           |    D1    |    £2     |     4     ‖
‖ Mango Juice     |    D2    |    £3     |     5     ‖
‖ Chocolate Milk  |    D3    |    £5     |     3     ‖
‖ Coffee          |    D4    |    £8     |     2     ‖
‖ Fanta           |    D5    |    £4     |     7     ‖ 
╚════════════════════════════════════════════════════╝      
\033[0m""")

# make a nested dictionary consisting of the items in the menu
# the dictionary should include the item name, item code, item price, and item stock
Available_Items={
    'Snacks':{
        'snack1':{
            'PRODUCT':'Chips',
            'ITEM CODE':'S1',
            'ITEM PRICE':'£5',
            'CURRENT STOCK':'6'
        },
        'snack2':{
            'PRODUCT':'Chocolate',
            'ITEM CODE':'S2',
            'ITEM PRICE':'£4',
            'CURRENT STOCK':'4'
        },
        'snack3':{
            'PRODUCT':'Biscuits',
            'ITEM CODE':'S3',
            'ITEM PRICE':'£3',
            'CURRENT STOCK':'7'
        },
        'snack4':{
            'PRODUCT':'Cookies',
            'ITEM CODE':'S4',
            'ITEM PRICE':'£7',
            'CURRENT STOCK':'5'
        },
        'snack5':{
            'PRODUCT':'Cake',
            'ITEM CODE':'S5',
            'ITEM PRICE':'£4',
            'CURRENT STOCK':'6'
        }    
    },
    'Drinks':{
        'drink1':{
            'PRODUCT':'Water',
            'ITEM CODE':'D1',
            'ITEM PRICE':'£2',
            'CURRENT STOCK':'4'
        },
        'drink2':{
            'PRODUCT':'Mango Juice',
            'ITEM CODE':'D2',
            'ITEM PRICE':'£3',
            'CURRENT STOCK':'5'
        },
        'drink3':{
            'PRODUCT':'Chocolate Milk',
            'ITEM CODE':'D3',
            'ITEM PRICE':'£5',
            'CURRENT STOCK':'3'
        },
        'drink4':{
            'PRODUCT':'Coffee',
            'ITEM CODE':'D4',
            'ITEM PRICE':'£8',
            'CURRENT STOCK':'2'
        },
        'drink5':{
            'PRODUCT':'Fanta',
            'ITEM CODE':'D5',
            'ITEM PRICE':'£4',
            'CURRENT STOCK':'7'
        }
    }
}

# make a function that contains the procedure of buying something from the vending machine
def vend_machine():
    # ask user to type the code of the product that they wish to buy 
    #(input function will allow the user to enter the code)
    choose=str(input("\033[35m\nPlease enter the respective code of the product that you would like:\t\033[0m"))

    # use the def function for managing the number of items
    # for snack 1:
    def S1_stock():
        x=6 # x is the CURRENT STOCK 
        while x >= 0:
            print("\033[3m\033[33m\t\t\t\t\tItem:",Available_Items['Snacks']['snack1']['PRODUCT'],"\n\t\t\t\t\tCurrent Stock:",(x-1),"\n\033[0m")
            break
        else:
            print("\033[33m\033[3m\t\t\t\tThe product",Available_Items['Snacks']['snack1']['PRODUCT'],"is no longer available.\033[0m")

    # for snack 2:
    def S2_stock():
        x=4
        while x >= 0:
            print("\033[3m\033[33m\t\t\t\t\tItem:",Available_Items['Snacks']['snack2']['PRODUCT'],"\n\t\t\t\t\tCurrent Stock:",(x-1),"\n\033[0m")
            break
        else:
            print("\033[33m\033[3m\t\t\t\tThe product",Available_Items['Snacks']['snack2']['PRODUCT'],"is no longer available.\033[0m")

    # for snack 3:
    def S3_stock():
        x=7
        while x >= 0:
            print("\033[3m\033[33m\t\t\t\t\tItem:",Available_Items['Snacks']['snack3']['PRODUCT'],"\n\t\t\t\t\tCurrent Stock:",(x-1),"\n\033[0m")
            break
        else:
            print("\033[33m\033[3m\t\t\t\tThe product",Available_Items['Snacks']['snack3']['PRODUCT'],"is no longer available.\033[0m")

    # for snack 4:
    def S4_stock():
        x=5
        while x >= 0:
            print("\033[3m\033[33m\t\t\t\t\tItem:",Available_Items['Snacks']['snack4']['PRODUCT'],"\n\t\t\t\t\tCurrent Stock:",(x-1),"\n\033[0m")
            break
        else:
            print("\033[33m\033[3m\t\t\t\tThe product",Available_Items['Snacks']['snack4']['PRODUCT'],"is no longer available.\033[0m")

    # for snack 5:
    def S5_stock():
        x=6
        while x >= 0:
            print("\033[3m\033[33m\t\t\t\t\tItem:",Available_Items['Snacks']['snack5']['PRODUCT'],"\n\t\t\t\t\tCurrent Stock:",(x-1),"\n\033[0m")
            break
        else:
            print("\033[33m\033[3m\t\t\t\tThe product",Available_Items['Snacks']['snack5']['PRODUCT'],"is no longer available.\033[0m")

    # for drink 1:  
    def D1_stock():
        x=4
        while x >= 0:
            print("\033[3m\033[33m\t\t\t\t\tItem:",Available_Items['Drinks']['drink1']['PRODUCT'],"\n\t\t\t\t\tCurrent Stock:",(x-1),"\n\033[0m")
            break
        else:
            print("\033[33m\033[3m\t\t\t\tThe product",Available_Items['Drinks']['drink1']['PRODUCT'],"is no longer available.\033[0m")

    # for drink 2:  
    def D2_stock():
        x=5
        while x >= 0:
            print("\033[3m\033[33m\t\t\t\t\tItem:",Available_Items['Drinks']['drink2']['PRODUCT'],"\n\t\t\t\t\tCurrent Stock:",(x-1),"\n\033[0m")
            break
        else:
            print("\033[33m\033[3m\t\t\t\tThe product",Available_Items['Drinks']['drink2']['PRODUCT'],"is no longer available.\033[0m")

    # for drink 3:  
    def D3_stock():
        x=3
        while x >= 0:
            print("\033[3m\033[33m\t\t\t\t\tItem:",Available_Items['Drinks']['drink3']['PRODUCT'],"\n\t\t\t\t\tCurrent Stock:",(x-1),"\n\033[0m")
            break
        else:
            print("\033[33m\033[3m\t\t\t\tThe product",Available_Items['Drinks']['drink3']['PRODUCT'],"is no longer available.\033[0m")

    # for drink 4:  
    def D4_stock():
        x=2
        while x >= 0:
            print("\033[3m\033[33m\t\t\t\t\tItem:",Available_Items['Drinks']['drink4']['PRODUCT'],"\n\t\t\t\t\tCurrent Stock:",(x-1),"\n\033[0m")
            break
        else:
            print("\033[33m\033[3m\t\t\t\tThe product",Available_Items['Drinks']['drink4']['PRODUCT'],"is no longer available.\033[0m")

    # for drink 5:  
    def D5_stock():
        x=7
        while x >= 0:
            print("\033[3m\033[33m\t\t\t\t\tItem:",Available_Items['Drinks']['drink5']['PRODUCT'],"\n\t\t\t\t\tCurrent Stock:",(x-1),"\n\033[0m")
            break
        else:
            print("\033[33m\033[3m\t\t\t\tThe product",Available_Items['Drinks']['drink5']['PRODUCT'],"is no longer available.\033[0m")

    # set of functions defined for managing the purchasing of items
    # for snack 1:
    def S1_pay():
        print("\033[1mThe product",Available_Items['Snacks']['snack1']['PRODUCT'],"costs",Available_Items['Snacks']['snack1']['ITEM PRICE']+".\033[0m")
        req_amount = float(input("\033[35m\nPlease enter the required amount: \033[0m")) #prompts the user to enter money
        if req_amount == 5:
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            S1_stock()
            add_choice()
        elif req_amount >= 5: 
            change = req_amount-5 # for the change
            print("\033[1m\033[32mYour change is",change,".\033[0m")
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            S1_stock()
            add_choice()
        elif req_amount <= 5:
            print("\033[1m\nThe amount you have entered is inadequate.\033[0m")
            print("Would you like to enter more money?")
            ask = int(input("\033[32mType 1 for Yes\nType 0 for No\n\033[0m")) 
            if ask == 1: # the user can enter more money
                remain = (5-req_amount)
                print("\033[1m\033[3m\033[35mYour remaining balance is",remain,".\033[0m")
                more = float(input("\033[1mPlease enter the remaining amount: \033[0m"))
                if more+req_amount == 5:
                    print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
                    S1_stock()
                    add_choice()
            elif ask == 0: # exits the vending machine
                print("\033[1m\nPress 0 to exit Vending Machine.\033[0m")
                exit = int(input())
                if exit == 0:
                    quit("\033[36m\033[1m\n\t\t\t\tHave a wonderful day! Goodbye.\n\033[0m")

    # for snack 2:
    def S2_pay():
        print("\033[1mThe product",Available_Items['Snacks']['snack2']['PRODUCT'],"costs",Available_Items['Snacks']['snack2']['ITEM PRICE']+".\033[0m")
        req_amount = float(input("\033[35m\nPlease enter the required amount: \033[0m"))
        if req_amount == 4:
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            S2_stock()
            add_choice()
        elif req_amount >= 4:
            change = req_amount-4
            print("\033[1m\033[32mYour change is",change,".\033[0m")
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            S2_stock()
            add_choice()
        elif req_amount <= 4:
            print("\033[1m\nThe amount you have entered is inadequate.\033[0m")
            print("Would you like to enter more money?")
            ask = int(input("\033[32mType 1 for Yes\nType 0 for No\n\033[0m"))
            if ask == 1:
                remain = (4-req_amount)
                print("\033[1m\033[3m\033[35mYour remaining balance is",remain,".\033[0m")
                more = float(input("\033[1mPlease enter the remaining amount: \033[0m"))
                if more+req_amount == 4:
                    print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
                    S2_stock()
                    add_choice()
            elif ask == 0:
                print("\033[1m\nPress 0 to exit Vending Machine.\033[0m")
                exit = int(input())
                if exit == 0:
                    quit("\033[36m\033[1m\n\t\t\t\tHave a wonderful day! Goodbye.\n\033[0m")

    # for snack 3:
    def S3_pay():
        print("\033[1mThe product",Available_Items['Snacks']['snack3']['PRODUCT'],"costs",Available_Items['Snacks']['snack3']['ITEM PRICE']+".\033[0m")
        req_amount = float(input("\033[35m\nPlease enter the required amount: \033[0m"))
        if req_amount == 3:
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            S3_stock()
            add_choice()
        elif req_amount >= 3:
            change = req_amount-3
            print("\033[1m\033[32mYour change is",change+".\033[0m")
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            S3_stock()
            add_choice()
        elif req_amount <= 3:
            print("\033[1m\nThe amount you have entered is inadequate.\033[0m")
            print("Would you like to enter more money?")
            ask = int(input("\033[32mType 1 for Yes\nType 0 for No\n\033[0m"))
            if ask == 1:
                remain = (3-req_amount)
                print("\033[1m\033[3m\033[35mYour remaining balance is",remain,".\033[0m")
                more = float(input("\033[1mPlease enter the remaining amount: \033[0m"))
                if more+req_amount == 3:
                    print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
                    S3_stock()
                    add_choice()
            elif ask == 0:
                print("\033[1m\nPress 0 to exit Vending Machine.\033[0m")
                exit = int(input())
                if exit == 0:
                    quit("\033[36m\033[1m\n\t\t\t\tHave a wonderful day! Goodbye.\n\033[0m")

    # for snack 4:
    def S4_pay():
        print("\033[1mThe product",Available_Items['Snacks']['snack4']['PRODUCT'],"costs",Available_Items['Snacks']['snack4']['ITEM PRICE']+".\033[0m")
        req_amount = float(input("\033[35m\nPlease enter the required amount: \033[0m"))
        if req_amount == 7:
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            S4_stock()
            add_choice()
        elif req_amount >= 7:
            change = req_amount-7
            print("\033[1m\033[32mYour change is",change,".\033[0m")
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            S4_stock()
            add_choice()
        elif req_amount <= 7:
            print("\033[1m\nThe amount you have entered is inadequate.\033[0m")
            print("Would you like to enter more money?")
            ask = int(input("\033[32mType 1 for Yes\nType 0 for No\n\033[0m"))
            if ask == 1:
                remain = (7-req_amount)
                print("\033[1m\033[3m\033[35mYour remaining balance is",remain,".\033[0m")
                more = float(input("\033[1mPlease enter the remaining amount: \033[0m"))
                if more+req_amount == 7:
                    print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
                    S4_stock()
                    add_choice()
            elif ask == 0:
                print("\033[1m\nPress 0 to exit Vending Machine.\033[0m")
                exit = int(input())
                if exit == 0:
                    quit("\033[36m\033[1m\n\t\t\t\tHave a wonderful day! Goodbye.\n\033[0m")

    # for snack 5:
    def S5_pay():
        print("\033[1mThe product",Available_Items['Snacks']['snack5']['PRODUCT'],"costs",Available_Items['Snacks']['snack5']['ITEM PRICE']+".\033[0m")
        req_amount = float(input("\033[35m\nPlease enter the required amount: \033[0m"))
        if req_amount == 4:
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            S5_stock()
            add_choice()
        elif req_amount >= 4:
            change = req_amount-4
            print("\033[1m\033[32mYour change is",change,".\033[0m")
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            S5_stock()
            add_choice()
        elif req_amount <= 4:
            print("\033[1m\nThe amount you have entered is inadequate.\033[0m")
            print("Would you like to enter more money?")
            ask = int(input("\033[32mType 1 for Yes\nType 0 for No\n\033[0m"))
            if ask == 1:
                remain = (4-req_amount)
                print("\033[1m\033[3m\033[35mYour remaining balance is",remain,".\033[0m")
                more = float(input("\033[1mPlease enter the remaining amount: \033[0m"))
                if more+req_amount == 4:
                    print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
                    S5_stock()
                    add_choice()
            elif ask == 0:
                print("\033[1m\nPress 0 to exit Vending Machine.\033[0m")
                exit = int(input())
                if exit == 0:
                    quit("\033[36m\033[1m\n\t\t\t\tHave a wonderful day! Goodbye.\n\033[0m")

    # for drink 1:
    def D1_pay():
        print("\033[1mThe product",Available_Items['Drinks']['drink1']['PRODUCT'],"costs",Available_Items['Drinks']['drink1']['ITEM PRICE']+".\033[0m")
        req_amount = float(input("\033[35m\nPlease enter the required amount: \033[0m"))
        if req_amount == 2:
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            D1_stock()
            add_choice()
        elif req_amount >= 2:
            change = req_amount-2
            print("\033[1m\033[32mYour change is",change,".\033[0m")
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            D1_stock()
            add_choice()
        elif req_amount <= 2:
            print("\033[1m\nThe amount you have entered is inadequate.\033[0m")
            print("Would you like to enter more money?")
            ask = int(input("\033[32mType 1 for Yes\nType 0 for No\n\033[0m"))
            if ask == 1:
                remain = (2-req_amount)
                print("\033[1m\033[3m\033[35mYour remaining balance is",remain,".\033[0m")
                more = float(input("\033[1mPlease enter the remaining amount: \033[0m"))
                if more+req_amount == 2:
                    print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
                    D1_stock()
                    add_choice()
            elif ask == 0:
                print("\033[1m\nPress 0 to exit Vending Machine.\033[0m")
                exit = int(input())
                if exit == 0:
                    quit("\033[36m\033[1m\n\t\t\t\tHave a wonderful day! Goodbye.\n\033[0m")

    # for drink 2:
    def D2_pay():
        print("\033[1mThe product",Available_Items['Drinks']['drink2']['PRODUCT'],"costs",Available_Items['Drinks']['drink2']['ITEM PRICE']+".\033[0m")
        req_amount = float(input("\033[35m\nPlease enter the required amount: \033[0m"))
        if req_amount == 3:
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            D2_stock()
            add_choice()
        elif req_amount >= 3:
            change = req_amount-3
            print("\033[1m\033[32mYour change is",change,".\033[0m")
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            D2_stock()
            add_choice()
        elif req_amount <= 3:
            print("\033[1m\nThe amount you have entered is inadequate.\033[0m")
            print("Would you like to enter more money?")
            ask = int(input("\033[32mType 1 for Yes\nType 0 for No\n\033[0m"))
            if ask == 1:
                remain = (3-req_amount)
                print("\033[1m\033[3m\033[35mYour remaining balance is",remain,".\033[0m")
                more = float(input("\033[1mPlease enter the remaining amount: \033[0m"))
                if more+req_amount == 3:
                    print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
                    D2_stock()
                    add_choice()
            elif ask == 0:
                print("\033[1m\nPress 0 to exit Vending Machine.\033[0m")
                exit = int(input())
                if exit == 0:
                    quit("\033[36m\033[1m\n\t\t\t\tHave a wonderful day! Goodbye.\n\033[0m")

    # for drink 3:
    def D3_pay():
        print("\033[1mThe product",Available_Items['Drinks']['drink3']['PRODUCT'],"costs",Available_Items['Drinks']['drink3']['ITEM PRICE']+".\033[0m")
        req_amount = float(input("\033[35m\nPlease enter the required amount: \033[0m"))
        if req_amount == 5:
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            D3_stock()
            add_choice()
        elif req_amount >= 5:
            change = req_amount-5
            print("\033[1m\033[32mYour change is",change,".\033[0m")
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            D3_stock()
            add_choice()
        elif req_amount <= 5:
            print("\033[1m\nThe amount you have entered is inadequate.\033[0m")
            print("Would you like to enter more money?")
            ask = int(input("\033[32mType 1 for Yes\nType 0 for No\n\033[0m"))
            if ask == 1:
                remain = (5-req_amount)
                print("\033[1m\033[3m\033[35mYour remaining balance is",remain,".\033[0m")
                more = float(input("\033[1mPlease enter the remaining amount: \033[0m"))
                if more+req_amount == 5:
                    print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
                    D3_stock()
                    add_choice()
            elif ask == 0:
                print("\033[1m\nPress 0 to exit Vending Machine.\033[0m")
                exit = int(input())
                if exit == 0:
                    quit("\033[36m\033[1m\n\t\t\t\tHave a wonderful day! Goodbye.\n\033[0m")

    # for drink 4:
    def D4_pay():
        print("\033[1mThe product",Available_Items['Drinks']['drink4']['PRODUCT'],"costs",Available_Items['Drinks']['drink4']['ITEM PRICE']+".\033[0m")
        req_amount = float(input("\033[35m\nPlease enter the required amount: \033[0m"))
        if req_amount == 8:
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            D4_stock()
            add_choice()
        elif req_amount >= 8:
            change = req_amount-8
            print("\033[1m\033[32mYour change is",change,".\033[0m")
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            D4_stock()
            add_choice()
        elif req_amount <= 8:
            print("\033[1m\nThe amount you have entered is inadequate.\033[0m")
            print("Would you like to enter more money?")
            ask = int(input("\033[32mType 1 for Yes\nType 0 for No\n\033[0m"))
            if ask == 1:
                remain = (8-req_amount)
                print("\033[1m\033[3m\033[35mYour remaining balance is",remain,".\033[0m")
                more = float(input("\033[1mPlease enter the remaining amount: \033[0m"))
                if more+req_amount == 8:
                    print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
                    D4_stock()
                    add_choice()
            elif ask == 0:
                print("\033[1m\nPress 0 to exit Vending Machine.\033[0m")
                exit = int(input())
                if exit == 0:
                    quit("\033[36m\033[1m\n\t\t\t\tHave a wonderful day! Goodbye.\n\033[0m")

    # for drink 5:
    def D5_pay():
        print("\033[1mThe product",Available_Items['Drinks']['drink5']['PRODUCT'],"costs",Available_Items['Drinks']['drink5']['ITEM PRICE']+".\033[0m")
        req_amount = float(input("\033[35m\nPlease enter the required amount: \033[0m"))
        if req_amount == 4:
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            D5_stock()
            add_choice()
        elif req_amount >= 4:
            change = req_amount-4
            print("\033[1m\033[32mYour change is",change,".\033[0m")
            print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
            D5_stock()
            add_choice()
        elif req_amount <= 4:
            print("\033[1m\nThe amount you have entered is inadequate.\033[0m")
            print("Would you like to enter more money?")
            ask = int(input("\033[32mType 1 for Yes\nType 0 for No\n\033[0m"))
            if ask == 1:
                remain = (4-req_amount)
                print("\033[1m\033[3m\033[35mYour remaining balance is",remain,".\033[0m")
                more = float(input("\033[1mPlease enter the remaining amount: \033[0m"))
                if more+req_amount == 4:
                    print("\033[31m\033[1m\033[3m\n\t\t\t\tThe item has been dispensed.\n\033[0m")
                    D5_stock()
                    add_choice()
            elif ask == 0:
                print("\033[1m\nPress 0 to exit Vending Machine.\033[0m")
                exit = int(input())
                if exit == 0:
                    quit("\033[36m\033[1m\n\t\t\t\tHave a wonderful day! Goodbye.\n\033[0m")

    # a function that makes suggestions based on what the user has already bought
    def extra_choice():
        if choose == "S1":
            print("\nSince you have chosen",Available_Items['Snacks']['snack1']['PRODUCT'],", I would suggest buying",Available_Items['Drinks']['drink5']['PRODUCT'],"as well. They taste great together. ")
        elif choose == "S2":
            print("\nSince you have chosen",Available_Items['Snacks']['snack2']['PRODUCT'],", I would suggest buying",Available_Items['Drinks']['drink2']['PRODUCT'],"as well. They taste great together. ")
        elif choose == "S3":
            print("\nSince you have chosen",Available_Items['Snacks']['snack3']['PRODUCT'],", I would suggest buying",Available_Items['Drinks']['drink3']['PRODUCT'],"as well. They taste great together. ")
        elif choose == "S4":
            print("\nSince you have chosen",Available_Items['Snacks']['snack4']['PRODUCT'],", I would suggest buying",Available_Items['Drinks']['drink4']['PRODUCT'],"as well. They taste great together. ")
        elif choose == "S5":
            print("\nSince you have chosen",Available_Items['Snacks']['snack5']['PRODUCT'],", I would suggest buying",Available_Items['Drinks']['drink1']['PRODUCT'],"as well. They taste great together. ")
        elif choose == "D1":
            print("\nSince you have chosen",Available_Items['Drinks']['drink1']['PRODUCT'],", I would suggest buying",Available_Items['Snacks']['snack4']['PRODUCT'],"as well. They taste great together. ") 
        elif choose == "D2":
            print("\nSince you have chosen",Available_Items['Drinks']['drink2']['PRODUCT'],", I would suggest buying",Available_Items['Snacks']['snack3']['PRODUCT'],"as well. They taste great together. ")
        elif choose == "D3":
            print("\nSince you have chosen",Available_Items['Drinks']['drink3']['PRODUCT'],", I would suggest buying",Available_Items['Snacks']['snack2']['PRODUCT'],"as well. They taste great together. ")
        elif choose == "D4":
            print("\nSince you have chosen",Available_Items['Drinks']['drink4']['PRODUCT'],", I would suggest buying",Available_Items['Snacks']['snack1']['PRODUCT'],"as well. They taste great together. ")
        elif choose == "D5":
            print("\nSince you have chosen",Available_Items['Drinks']['drink5']['PRODUCT'],", I would suggest buying",Available_Items['Snacks']['snack5']['PRODUCT'],"as well. They taste great together. ")
    
    # a function that specifies which specific function needs to be put forward based on what the user buys 
    def pay():
        if choose == "S1": #if the user enter the code S1, the the S1_pay() function will be run (all the other functions have been defined similarly based on their respective code)
            S1_pay()
        if choose == "S2":
            S2_pay()
        if choose == "S3":
            S3_pay()
        if choose == "S4":
            S4_pay()
        if choose == "S5":
            S5_pay()
        if choose == "D1":
            D1_pay()
        if choose == "D2":
            D2_pay()
        if choose == "D3":
            D3_pay()
        if choose == "D4":
            D4_pay()
        if choose == "D5":
            D5_pay()

        # a function that asks if the user would like additional items        
    def add_choice(): 
        add=int(input("\033[1m\nWould you like to buy anything else?\033[0m \n\033[32mIf yes, enter 1\nIf no, enter 0\n\033[0m"))
        if add==1: # provides a suggestion and asks the user again to enter the code for the item they want 
                extra_choice()
                vend_machine()
                pay()
        if add==0: # stops the program and also prints a message
                quit("\033[36m\n\t\t\t\tThank you for purchasing from the Vending Machine. \n\t\t\t\t\tHave a wonderful day!\n\033[0m")
    pay()

vend_machine()
