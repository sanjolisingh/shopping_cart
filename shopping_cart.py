# Product list
products = ["Apple", "Banana", "Milk", "Bread"]
prices = [10, 5, 25, 20]
cart = []

while True:
    print("\n1. Show Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        for i in range(len(products)):
            print(f"{i+1}. {products[i]} - ₹{prices[i]}")

    elif choice == '2':
        pid = int(input("Enter product number: ")) - 1
        if 0 <= pid < len(products):
            cart.append(pid)
            print(f"{products[pid]} added to cart.")
        else:
            print("Invalid product number.")

    elif choice == '3':
        total = 0
        print("\nYour Cart:")
        for pid in cart:
            print(f"- {products[pid]} ₹{prices[pid]}")
            total += prices[pid]
        print(f"Total: ₹{total}")

    elif choice == '4':
        print("Thanks for shopping!")
        break

    else:
        print("Invalid choice.")
    
