print("------------Password Generator-----------")
import random
import string
length =int(input("Entrer The Password Length : "))

characters =string.ascii_letters + string.ascii_lowercase + string.digits + string.ascii_uppercase

password = " "

for i in range(length):
    password+= random.choice(characters)

print("Generated password : ",password)
