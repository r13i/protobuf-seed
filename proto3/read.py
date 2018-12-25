import address_book_pb2
import sys



def ListPeople(address_book):
    for person in address_book.people:

        print("Person ID:", person.id)
        print("    Name:", person.name)

        if person.email != "":
            print("    E-mail:", person.email)

        for phone_number in person.phones:

            if phone_number.type == address_book_pb2.Person.MOBILE:
                print("    Mobile phone #:", phone_number.number)
            elif phone_number.type == address_book_pb2.Person.WORK:
                print("    Work phone #:", phone_number.number)
            elif phone_number.type == address_book_pb2.Person.HOME:
                print("    Home phone #:", phone_number.number)




# main procedure
#   reads the entire address book from a file
#   prints all infromations
if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)


address_book = address_book_pb2.AddressBook()

# read the existing address book
f = open(sys.argv[1], "rb")
address_book.ParseFromString(f.read())
f.close()

ListPeople(address_book)