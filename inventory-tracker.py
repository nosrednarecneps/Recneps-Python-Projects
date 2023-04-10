print(f"""Welcome to the inventory tracker!
{"-" * 10}""")

def display_options():
    options = """(1) View Inventory 
(2) Add Item 
(3) Drop Item 
(4) Exit

Please select your option: """
    selected_option = int(input(options))
    return selected_option

def view_inventory():
    print("-" * 10)
    print(f"{len(inventory)} items in inventory")
    print(inventory)
    print("-" * 10)
    
def add_item():
    item = input("What item would you like to add?: ").upper()
    inventory.append(item)
    set_list = sorted(list(set(inventory)))
    sorted_list = sorted(inventory)
    if set_list != sorted_list:
        inventory.pop(-1)
        print("You're item already exists!")
    else:
        print(f"{item} added to inventory!")
    
def drop_item():
    view_inventory()
    index = int(input("What item would you like to drop: Item #")) - 1
    dropped_item = inventory.pop(index)
    print(f"Removed {dropped_item} from inventory.")

inventory = ["POTION", "SHIELD", "DAGGER", "ARROW"]   

while True:       
    selected_option = display_options()
    if selected_option == 1:
        view_inventory()
    elif selected_option == 2:
        add_item()
    elif selected_option == 3:
        drop_item()
    elif selected_option == 4:
        print("Goodbye!")
        break