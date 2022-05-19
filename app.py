import sys

from create_menu_list import create_list
from customer_data import customer_data
from create_order import create_order
from update_order import update_order
from delete_order import delete_order

def menu(): 
    while True:
        user_input = int(input("enter an menu input: "))
        name_input = ""
        match user_input:
            case 1:
                create_list()
                menu()
            case 2:
                customer_data()
                menu()
            case 3:
                create_order()
                menu()
            case 4:
                update_order()
                menu()
            case 5:
                delete_order()
                menu()
            case 0:
                sys.exit()
menu()