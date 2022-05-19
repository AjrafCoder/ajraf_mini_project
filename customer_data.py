def customer_data():
    text_file = open("name.txt", "w")
    text_file.write(input("Enter a name: "))
    text_file.close()

    text_file = open("address.txt", "w")
    text_file.write(input("Enter an address: "))
    text_file.close()

    text_file = open("phone.txt", "w")
    text_file.write(input("Enter a phone number: "))
    text_file.close()

        
