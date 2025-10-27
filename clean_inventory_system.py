"""
Inventory Management System
---------------------------
A simple system to manage items in stock — add, remove, update, and view inventory.

Author: Yuti Naha
Lab: SE Lab 5 - Static Code Analysis
"""

from typing import Dict


class InventoryItem:
    """Class representing a single inventory item."""

    def __init__(self, name: str, quantity: int, price: float) -> None:
        """
        Initialize an inventory item.
        :param name: Name of the item
        :param quantity: Quantity in stock
        :param price: Price per item
        """
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, new_quantity: int) -> None:
        """Update the quantity of the item."""
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = new_quantity

    def update_price(self, new_price: float) -> None:
        """Update the price of the item."""
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = new_price

    def total_value(self) -> float:
        """Return total value of the item (quantity × price)."""
        return self.quantity * self.price

    def __repr__(self) -> str:
        """Return a string representation of the item."""
        return f"{self.name}: {self.quantity} units @ ₹{self.price:.2f} each"


class InventorySystem:
    """Inventory management system to store and handle multiple items."""

    def __init__(self) -> None:
        """Initialize an empty inventory."""
        self.items: Dict[str, InventoryItem] = {}

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """Add a new item to the inventory."""
        if name in self.items:
            raise ValueError("Item already exists.")
        self.items[name] = InventoryItem(name, quantity, price)

    def remove_item(self, name: str) -> None:
        """Remove an item from the inventory."""
        if name not in self.items:
            raise KeyError("Item not found.")
        del self.items[name]

    def update_item(self, name: str, quantity: int = None, price: float = None) -> None:
        """Update item quantity or price."""
        if name not in self.items:
            raise KeyError("Item not found.")
        if quantity is not None:
            self.items[name].update_quantity(quantity)
        if price is not None:
            self.items[name].update_price(price)

    def get_total_inventory_value(self) -> float:
        """Calculate total inventory value."""
        return sum(item.total_value() for item in self.items.values())

    def display_inventory(self) -> None:
        """Display all items in the inventory."""
        if not self.items:
            print("Inventory is empty.")
            return
        print("\n--- Inventory List ---")
        for item in self.items.values():
            print(item)
        print(f"\nTotal Inventory Value: ₹{self.get_total_inventory_value():.2f}")


def main() -> None:
    """Main function for demonstration."""
    system = InventorySystem()

    # Adding items
    system.add_item("Laptop", 5, 55000.0)
    system.add_item("Mouse", 10, 500.0)

    # Updating an item
    system.update_item("Laptop", price=56000.0)

    # Display inventory
    system.display_inventory()


if __name__ == "__main__":
    main()
