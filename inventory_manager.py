
"""
Name: Kyle Graham
Course: CPS310
Project: Inventory Manager

A command-line application for managing inventory.
"""

INVENTORY_FILE = "inventory.txt"


def display_menu():
    """Display the available inventory management options."""
    print("\nInventory Manager")
    print("1. View inventory")
    print("2. Add an item")
    print("3. Update an item quantity")
    print("4. Remove an item")
    print("5. Search inventory")
    print("6. View inventory summary")
    print("7. Exit")


def load_inventory(filename):
    """Load inventory records from a text file."""
    inventory = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, category, quantity = line.split("|")

                item = {
                    "name": name,
                    "category": category,
                    "quantity": int(quantity)
                }

                inventory.append(item)

    except FileNotFoundError:
        return []

    return inventory


def save_inventory(inventory, filename):
    """Save all inventory records to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        for item in inventory:
            file.write(
                f"{item['name']}|{item['category']}|"
                f"{item['quantity']}\n"
            )


def view_inventory(inventory):
    """Display all inventory items in a numbered list."""
    if not inventory:
        print("No inventory items found.")
        return

    print("\nInventory:")

    for number, item in enumerate(inventory, start=1):
        print(
            f"{number}. {item['name']} | {item['category']} | "
            f"Quantity: {item['quantity']}"
        )


def get_nonnegative_quantity(prompt):
    """Return a nonnegative whole number entered by the user."""
    value = input(prompt).strip()

    if not value.isdigit():
        print("Quantity must be a nonnegative whole number.")
        return None

    return int(value)


def add_item(inventory):
    """Validate and add a new inventory item."""
    name = input("Enter the item name: ").strip()

    if not name:
        print("Item name cannot be empty.")
        return

    if "|" in name:
        print("Item name cannot contain '|'.")
        return

    for item in inventory:
        if item["name"].casefold() == name.casefold():
            print("An item with that name already exists.")
            return

    category = input("Enter the category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    if "|" in category:
        print("Category cannot contain '|'.")
        return

    quantity = get_nonnegative_quantity("Enter the quantity: ")

    if quantity is None:
        return

    inventory.append({
        "name": name,
        "category": category,
        "quantity": quantity
    })

    print("Item added successfully.")
    save_inventory(inventory, INVENTORY_FILE)


def update_quantity(inventory):
    """Update the quantity of a selected inventory item."""
    if not inventory:
        print("No inventory items found.")
        return

    view_inventory(inventory)

    selection = input(
        "Enter the item number to update: "
    ).strip()

    if not selection.isdigit():
        print("Invalid item number.")
        return

    number = int(selection)

    if number < 1 or number > len(inventory):
        print("Invalid item number.")
        return

    quantity = get_nonnegative_quantity(
        "Enter the new quantity: "
    )

    if quantity is None:
        return

    item = inventory[number - 1]
    item["quantity"] = quantity

    print(
        f"{item['name']} quantity updated to {quantity}."
    )

    save_inventory(inventory, INVENTORY_FILE)


def remove_item(inventory):
    """Remove a selected item from the inventory."""
    if not inventory:
        print("No inventory items found.")
        return

    view_inventory(inventory)

    selection = input(
        "Enter the item number to remove: "
    ).strip()

    if not selection.isdigit():
        print("Invalid item number.")
        return

    number = int(selection)

    if number < 1 or number > len(inventory):
        print("Invalid item number.")
        return

    removed_item = inventory.pop(number - 1)

    print(f"Item removed: {removed_item['name']}")

    save_inventory(inventory, INVENTORY_FILE)


def search_inventory(inventory):
    """Search item names using case-insensitive partial matching."""
    term = input("Enter an item name to search for: ").strip()

    if not term:
        print("Search term cannot be empty.")
        return

    matches = []

    for item in inventory:
        if term.casefold() in item["name"].casefold():
            matches.append(item)

    if not matches:
        print("No inventory items matched your search.")
        return

    print("\nSearch Results:")

    for number, item in enumerate(matches, start=1):
        print(
            f"{number}. {item['name']} | {item['category']} | "
            f"Quantity: {item['quantity']}"
        )


def display_summary(inventory):
    """Display inventory totals and counts by category."""
    total_quantity = 0
    low_stock_count = 0
    category_counts = {}

    for item in inventory:
        total_quantity += item["quantity"]

        if item["quantity"] < 5:
            low_stock_count += 1

        category_key = item["category"].casefold()

        if category_key not in category_counts:
            category_counts[category_key] = {
                "name": item["category"],
                "count": 0
            }

        category_counts[category_key]["count"] += 1

    print("\nInventory Summary")
    print(f"Unique items: {len(inventory)}")
    print(f"Total quantity: {total_quantity}")
    print(f"Low-stock items: {low_stock_count}")

    print("\nItems by category:")

    if not category_counts:
        print("No categories found.")
        return

    for category in category_counts.values():
        print(f"{category['name']}: {category['count']}")


def main():
    """Load inventory and run the main menu loop."""
    inventory = load_inventory(INVENTORY_FILE)

    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            update_quantity(inventory)
        elif choice == "4":
            remove_item(inventory)
        elif choice == "5":
            search_inventory(inventory)
        elif choice == "6":
            display_summary(inventory)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
