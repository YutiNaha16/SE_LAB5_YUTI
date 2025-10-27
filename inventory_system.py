import json
import logging
from datetime import datetime

# Global variable
stock_data = {}
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def addItem(item="default", qty=0, logs=None):
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning("Invalid item or quantity type.")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    return logs

def removeItem(item, qty):
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
        else:
            logging.warning(f"Item {item} not found in inventory.")
    except KeyError as e:
        logging.error(f"Error removing item: {e}")

def getQty(item):
    return stock_data.get(item, 0)

def loadData(file="inventory.json"):
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        logging.warning("Inventory file not found, starting with empty stock.")

def saveData(file="inventory.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)

def printData():
    print("\nItems Report")
    for i, qty in stock_data.items():
        print(f"{i} -> {qty}")

def checkLowItems(threshold=5):
    return [item for item, qty in stock_data.items() if qty < threshold]

def main():
    addItem("apple", 10)
    addItem("banana", 2)
    removeItem("apple", 3)
    removeItem("orange", 1)
    print(f"Apple stock: {getQty('apple')}")
    print(f"Low items: {checkLowItems()}")
    saveData()
    loadData()
    printData()

if __name__ == "__main__":
    main()
