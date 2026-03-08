import os
import sys
import json

# Get the directory of this script
CUR_DIR = os.path.dirname(__file__)

# Path to the JSON file
LIST_PATH = os.path.join(CUR_DIR, "list.json")

# Menu displayed to the user
MENU = """Choose one of the following 5 options:
1: Add an item to the list
2: Remove an item from the list
3: Display the list
4: Clear the list
5: Quit
? Your choice: """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

# Load the list if the JSON file exists
if os.path.exists(LIST_PATH):
    with open(LIST_PATH, "r") as f:
        SHOPPING_LIST = json.load(f)
else:
    SHOPPING_LIST = []


while True:
    user_choice = ""

    # Ask the user until a valid choice is entered
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)

        if user_choice not in MENU_CHOICES:
            print("Please choose a valid option...")

    # 1: Add an item
    if user_choice == "1":
        item = input("Enter the name of an item to add to the shopping list: ")
        SHOPPING_LIST.append(item)
        print(f"The item '{item}' has been added to the list.")

    # 2: Remove an item
    elif user_choice == "2":
        item = input("Enter the name of an item to remove from the shopping list: ")

        if item in SHOPPING_LIST:
            SHOPPING_LIST.remove(item)
            print(f"The item '{item}' has been removed from the list.")
        else:
            print(f"The item '{item}' is not in the list.")

    # 3: Display the list
    elif user_choice == "3":
        if SHOPPING_LIST:
            print("Here is the content of your list:")

            for i, item in enumerate(SHOPPING_LIST, 1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is empty.")

    # 4: Clear the list
    elif user_choice == "4":
        SHOPPING_LIST.clear()
        print("The list has been cleared.")

    # 5: Save and quit
    elif user_choice == "5":
        with open(LIST_PATH, "w") as f:
            json.dump(SHOPPING_LIST, f, indent=4)

        print("See you soon!")
        sys.exit()

    print("-" * 50)