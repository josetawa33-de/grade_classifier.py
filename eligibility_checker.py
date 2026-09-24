# eligibility_checker.py

age = int(input("Enter your age: "))
consent = input("Do you have parental consent? (yes/no): ").lower()

# Use compound boolean operators instead of nested ifs
if age >= 18 or (age >= 13 and consent == "yes"):
    print("Welcome to the club!")
else:
    print("Sorry, you are not eligible yet.")
