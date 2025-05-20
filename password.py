attempts = 0
max_attempts = 3
password = "admin123"

while attempts < max_attempts:
    guest_password = input("Enter Password: ")
    if guest_password == password:
        print("Correct")
        break
    else:
        attempts += 1
        tries_left = max_attempts - attempts
        print(f"Wrong, you have only {tries_left} attempt(s) left.")

if attempts == max_attempts:
    print("3 times a charm but you failed, access denied.")
