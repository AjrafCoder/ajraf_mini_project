import json
from create_menu_list import create_list

def update_order():
    get_order = input("enter order number")
    order_json_file = (get_order+".json")

    with open(order_json_file, "r") as jsonFile:
        data = json.load(jsonFile)

    new_list = create_list()

    data['items in list'] = new_list

    with open(order_json_file, "w") as jsonFile:
        json.dump(data, jsonFile)

