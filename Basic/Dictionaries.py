customer = {
    "name" : "Maruf Ahammed",
    "age" : 30,
    "is_verified" : True
}
print(customer ["name"])     #Case sensative
print (customer.get("birthdate", "Sep 10 1980"))

customer["name"] = "Jack Smith"
print(customer["name"])   #Updated
