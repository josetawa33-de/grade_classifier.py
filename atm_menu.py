# atm_menu.py

balance = 1000
correct_pin = "1234"  # You can choose your own PIN

pin = input("Enter your 4-digit PIN: ")

if pin != correct_pin:
    print("Incorrect PIN")
else:
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful. New balance: {balance}")
    else:
        print("Insufficient funds")
