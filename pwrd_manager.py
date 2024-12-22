from cryptography.fernet import Fernet



def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as keyFile:
        keyFile.write(key)


def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key



def add():
    usrName = input("Enter a username: ")
    pwd = input("Enter a password corresponding to the username: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()  
    with open('password.txt', 'a') as f:
        f.write(f"{usrName}:{encrypted_pwd}\n")
    print("Password added successfully!")




def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, encrypted_pwd = data.split(":")
            decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode()  # Decrypt and convert to string
            print(f"Username: {user}\tPassword: {decrypted_pwd}")



key = load_key()
fer = Fernet(key)

# Main program loop
while True:
    mode = input("Enter a mode to view or add a password (view / add / or press q to exit): ").lower()
    if mode == "q":
        break
    elif mode == 'view':
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input!")
