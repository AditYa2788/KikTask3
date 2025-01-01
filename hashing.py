import random
import string
def custom_hash(input_string: str, hash_size: int = 32) -> str:
    if not input_string:
        return "0" * hash_size
    prime1 = 31
    prime2 = 53
    prime3 = 101
    hash1 = prime1
    hash2 = prime2
    hash3 = prime3
    for i, char in enumerate(input_string):
        char_value = ord(char)
        hash1 = (hash1 * prime1 + char_value) % (2**32)
        hash2 = (hash2 * prime2 + char_value) % (2**32)
        hash3 = (hash3 * prime3 + char_value) % (2**32)
    combined_hash = (hash1 ^ hash2 ^ hash3) % (2**32)
    hex_hash = hex(combined_hash)[2:]
    return hex_hash[:hash_size].zfill(hash_size)
saltData={
    "5adityabhide@gmail.com":"X7P9QZT",
    "rehan43@gmail.com":"J8L2WKC",
    "varad777@gmail.com":"M5TQ9RY"
}
userPass={
    "5adityabhide@gmail.com":custom_hash(saltData["5adityabhide@gmail.com"]+"jonSnow755",16),
    "rehan43@gmail.com":custom_hash(saltData["rehan43@gmail.com"]+"goose90",16),
    "varad777@gmail.com":custom_hash(saltData["varad777@gmail.com"]+"bond78",16)
}
def randomString():
    characters = string.ascii_letters + string.digits  # Letters (a-z, A-Z) and digits (0-9)
    random_string = ''.join(random.choice(characters) for _ in range(5))
    return random_string

def signup():
     userID=input("Enter email id ")
     password=input("Enter password ")
     salt = randomString()
     saltData.update({userID: salt})
     userPass.update({userID:custom_hash(salt+password)})

def login():
    id2=input("Enter email ")
    pass2=input("Enter Password ")
    if custom_hash(saltData[id2] + pass2, 16)==userPass[id2]:
        print("Login Successful!")
    else:
        print("Login failed!")
while True:
    inp=input("Enter 1 to login, 2 to signup and 3 for application to stop ")
    if(inp=="1"):
        login()
    if(inp=="2"):
        signup()
    if(inp=="3"):
        break

