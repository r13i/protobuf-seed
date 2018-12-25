import address_book_pb2

person = address_book_pb2.Person()

person.name = "John Doe"
person.id = 1234
person.email = "a@b.c" 

phone = person.phones.add()
phone.number = "4321"
phone.type = address_book_pb2.Person.WORK


print("====== START Test 1 ======")
print(person.IsInitialized())
print(person.__str__())
print("====== END Test 1 ======")


print("====== START Test 2 ======")
serialized = person.SerializeToString()
print(serialized)

unserialized = person.ParseFromString(serialized)
print(unserialized)
print("====== END Test 2 ======")
