from random import randint
import json

def create_order():
    def random_with_N_digits(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
    order_number = random_with_N_digits(6)

    with open("name.txt","r") as f:
        name = f.read() 
    with open("address.txt","r") as f:
        address = f.read() 
    with open("phone.txt","r") as f:
        phone = f.read() 
    cust_list = [line.strip('') for line in open("customer_list.txt")]

    customer_dict = {
        "order number": order_number,
        "name": name,
        "address": address,
        "phone number": phone,
        "customer order": cust_list,
        "status": "In progress",
    }
    file_name = (str(order_number) + ".json")
    json_file = open((file_name),"w")
    json.dump(customer_dict, json_file)
    json_file.close()
    print("Your order number is:  " + str(order_number))

