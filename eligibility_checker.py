# eligibility_checker.py

age = int(input("Enter your age: "))

# Rule: Members must be 13 or older
if age < 13:
    print("Sorry, you are not eligible yet.")
else:
    # Rule: Under 18 requires parental consent
    if age < 18:
        consent = input("Do you have parental consent? (yes/no): ").lower()
        # Condition: age >= 13 AND consent is yes
        if consent == "yes":
            print("Welcome to the club!")
        else:
            print("Sorry, you are not eligible yet.")
    else:
        # Condition: age >= 18 (no consent needed)
        print("Welcome to the club!")
