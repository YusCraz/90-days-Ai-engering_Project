class ShoppingCart:
    def __init__(self, owner, items):
        self.owner = owner
        self.items = items

    def add_item(self):
        name = input("Enter the name of item: ")
        price = float(input("Enter the price of item: "))

        item = {
            "name": name,
            "price": price
        }

        self.items.append(item)
        return self.items

    def remove_item(self):
        remove_name = input("Enter the item you want to remove: ")

        for item in self.items:
            if item["name"] == remove_name:
                self.items.remove(item)
                break

        return self.items

    def calculate_total(self):
        total = sum(item["price"] for item in self.items)
        return total

    def most_expensive(self):
        expensive = self.items[0]

        for item in self.items[1:]:
            if item["price"] > expensive["price"]:
                expensive = item

        return expensive


def main():
    cart = ShoppingCart("Aayush", [])

    # Add three items
    cart.add_item()
    cart.add_item()
    cart.add_item()

    # Remove one item
    cart.remove_item()

    print("\nItems in cart:")

    for item in cart.items:
        print(f"{item['name']} - ${item['price']:.2f}")

    print(f"\nTotal: ${cart.calculate_total():.2f}")

    expensive = cart.most_expensive()
    print(
        f"Most expensive: "
        f"{expensive['name']} - ${expensive['price']:.2f}"
    )


if __name__ == "__main__":
    main()