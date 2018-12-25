
import address_book_pb2
import sys


def PromptForAddress(person):

    person.id = int(input("Enter person ID number: "))
    person.name = input("Enter name: ")

    email = input("Enter email (leave blank for none): ")
    if email != "":
        person.email = email

    while True:
        _number = input("Enter a phone number (leave blank to finish): ")
        if _number == "":
            break

        phone_number = person.phones.add()
        phone_number.number = _number

        _type = input("Is this a mobile, home, or work phone? ")
        if _type.upper() == "MOBILE":
            phone_number.type = address_book_pb2.Person.MOBILE

        elif _type.upper() == "HOME":
            phone_number.type = address_book_pb2.Person.HOME

        elif _type.upper() == "WORK":
            phone_number.type = address_book_pb2.Person.WORK

        else:
            print("Unknown phone type. Leaving as default.")







# main procedure:
#   reads the address book from a file
#   adds one person based on user input
#   write back to the file
if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)

address_book = address_book_pb2.AddressBook()

# read the existing address book
try:
    f = open(sys.argv[1], "rb")
    address_book.ParseFromString(f.read())
    f.close()
except IOError:
    print(sys.argv[1], ": Could not open file. Creating a new one.")


# add an address
PromptForAddress(address_book.people.add())

# write back the new address book to disk
f = open(sys.argv[1], "wb")
f.write(address_book.SerializeToString())
f.close()