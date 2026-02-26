import sys

SHOPPING_LIST = []

MENU = """Choose one of the following 5 options:
1: Add an item to the list
2: Remove an item from the list
3: Display the list
4: Clear the list
5: Quit
? Your choice: """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = input(MENU)

    if user_choice not in MENU_CHOICES:
        print("Please choose a valid option...")
        continue

    if user_choice == "1":  # Add an item
        item = input("Enter the name of an item to add to the shopping list: ")
        SHOPPING_LIST.append(item)
        print(f"The item '{item}' has been successfully added to the list.")

    elif user_choice == "2":  # Remove an item
        item = input("Enter the name of an item to remove from the shopping list: ")
        if item in SHOPPING_LIST:
            SHOPPING_LIST.remove(item)
            print(f"The item '{item}' has been successfully removed from the list.")
        else:
            print(f"The item '{item}' is not in the list.")

    elif user_choice == "3":  # Display the list
        if SHOPPING_LIST:
            print("Here is the content of your shopping list:")
            for i, item in enumerate(SHOPPING_LIST, 1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is empty.")

    elif user_choice == "4":  # Clear the list
        SHOPPING_LIST.clear()
        print("The shopping list has been cleared.")

    elif user_choice == "5":  # Quit
        print("See you soon!")
        sys.exit()

    print("-" * 50)