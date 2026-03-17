def stock_tracker():
    stocks = {"apple": 150, "tesla": 200, "google": 180, "amazon": 170}
    total = 0
    details = []

    print("\n📈 Stock Portfolio Tracker")

    while True:
        name = input("Enter stock name (or 'done' to finish): ").lower()
        if name == "done":
            break
        if name not in stocks:
            print("❌ Stock not found!")
            continue
        qty = input("Enter quantity: ")
        if not qty.isdigit():
            print("⚠ Quantity must be a number!")
            continue
        qty = int(qty)
        amount = qty * stocks[name]
        total += amount
        details.append(f"{name.title()}: {qty} shares x ${stocks[name]} = ${amount}")

    with open("portfolio.txt", "w") as file:
        for line in details:
            file.write(line + "\n")
        file.write(f"\nTotal Investment: ${total}\n")

    print("\n✅ Portfolio saved in 'portfolio.txt'")
    print(f"💰 Total Investment: ${total}")

if __name__ == "__main__":
    stock_tracker()