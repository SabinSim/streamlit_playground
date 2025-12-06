rate = 1.05  # exchange rate

choice = input("Select an option: 1) CHF → EUR | 2) EUR → CHF: ")

if choice == "1":
    print("=== Currency Converter ===")
    amount = float(input("Enter amount in CHF: "))
    result = amount * rate
    print("EUR:", result)

elif choice == "2":
    print("=== Currency Converter ===")
    amount = float(input("Enter amount in EUR: "))
    result = amount / rate
    print("CHF:", result)

else:
    print("Invalid option.")
