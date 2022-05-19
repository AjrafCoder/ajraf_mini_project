def create_list():
    items = [word.strip('\n') for word in open("items.txt", 'r').readlines()]
    customer_list = []

    while True:
        user_menu_input = input("Enter an item: ")

        if user_menu_input in items:
            customer_list.append(user_menu_input)
            print(customer_list)
        elif (user_menu_input == "exit"):
            print(customer_list)
            break
        else:
            break

    textfile = open("customer_list.txt", "w")
    for element in customer_list:
        textfile.write(element + "\n")
    textfile.close()
