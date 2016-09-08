"""
Nicholas Neville, 5/9/2016
-----------------------------------------------------
            ***Shopping List 1.0***
Program ranks items based on the priority (1, 2 or 3).
Users can:
           * Add items to the list
           * Mark items as complete
           * Review a list of completed/required items (with estimated price))
Users can't change items from complete to required
-----------------------------------------------------
GitHub: https://github.com/nick4814/Assignment1
"""
import csv


def main():
    menu = ("Menu:\nR - List required items\nC - List completed items"
            "\nA - Add new item\nM - Mark an item as completed\nQ - Quit")

    lst = read_write_csv("read")  # Get list 'lst' from 'items.csv'
    lst = order_list(lst)  # Order list by priority
    print("Shopping List 1.0 - by Nicholas Neville")
    print(menu)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "R":
            load_items(lst, choice, None)
        elif choice == "C":
            pass
        elif choice == "A":
            add_items(lst, choice)
        elif choice == "M":
            load_items(lst, choice, None)
        else:
            print("Invalid menu choice.")
        print(menu)
        choice = input(">>> ").upper()
    read_write_csv("write")


def load_items(lst, choice, item_info):

    total = [0, 0]  # Total[0] is total price, Total[1] is total items

    if choice == "R":
        print("Required items:")
        state = "r"
    elif choice == "C":
        print("Completed items:")
        state = "c"
    elif choice == "M":
        state = "r"

    if choice == 'A':
        print("{}, ${:.2f} (priority {}) added to shopping list".format(*item_info))
    else:  # Choice is "R" or "C" or "M"
        max_width = max(len(str(word)) for row in lst for word in row)  # For dynamic column padding
        for row in lst:
            if row[3] == state:  # If priority num = a+1 and state are in row
                print("{}. {} {} \t\t $  {:.2f} ({})".format(total[1], row[0], ' '*(max_width-len(row[0])), row[1], row[2]))
                total[0] += row[1]  # Accumulate total price
                total[1] += 1  # Accumulate total items
        print("Total expected price for {} items: ${:.2f}".format(total[1], total[0]))

    if choice == "M":
        item_num = int(inp_chk("Enter the number of item to mark as completed \n>>> ", total[1]))
        print("{} marked as completed".format(lst[item_num][0]))


def add_items(lst, choice):  # Function for adding items

    item_info = ['', '', '', 'r']  # Initialise list, ''
    item_info[0] = inp_chk("Item name: ", None)  # Item name
    item_info[1] = float(inp_chk("Price: $", None))  # Store price as float
    item_info[2] = int(inp_chk("Priority: ", None))  # Store priority value as integer
    lst.append(item_info)  # Add new list item 'item_info[]' to lst
    lst = order_list(lst)  # Order the new list
    load_items(lst, choice, item_info)  # Pass new list 'lst' and choice to loadItems() for printing


def order_list(temp_lst):  # Function to order lists

    lst = []  # Initialise lists
    pri = [0, 0, 0]  # To store priorities, pri[0] is 1, pri [1] is 2 ...

    for row in temp_lst:  # Get number of priorities
        if row[2] == 1:  # If priority is 1
            pri[0] += 1
        elif row[2] == 2:  # If priority is 2
            pri[1] += 1
        else:  # Priority is 3
            pri[2] += 1
    for a in range(0, 3):  # Loop through priority values
        i = 0
        for row in temp_lst:
            if i != pri[a] and row[2] == a + 1:  # Skip if printed all lists of priority a
                lst.append(row)
                i += 1
    return lst  # Ordered list


def inp_chk(pick, sum_items):  # Function to handle inputs (extra error handling for different user inputs)
    while True:
        try:
            r = input(pick)
            if pick == "Price: $" or pick == "Priority: " or pick == "Enter the number of item to mark as completed \n>>> ":
                if not (is_float(r) or r.isdigit()):
                    raise ValueError("Invalid input; enter a valid number")
                if pick == "Price: $" and float(r) < 0:  # Check price input and if r is negative
                    raise ValueError("Price must be >= $0")
                elif pick == "Priority: " and not (1 <= int(r) <= 3):  # Check input is priority: and r is not 1, 2 or 3
                    raise ValueError("Priority must be 1, 2 or 3")
                elif pick == "Enter the number of item to mark as completed \n>>> " and not (0 <= int(r) <= sum_items):
                        raise ValueError("Invalid item number")
            else:  # Check string input
                if not any(c.isalpha() for c in r) and not(r.isspace() or not r):  # if r has no letters and isn't blank
                    raise ValueError("Invalid string input")
            if not isinstance(r, int):  # If r is not an integer (r.isspace() doesn't work on integers)
                if r.isspace() or not r:  # If r is filled with spaces or empty
                    raise ValueError("Input can not be blank")
            break   # Exit while loop
        except ValueError as e:
            print(e)
    return r


def is_float(num):  # Return true if float, false if not
    try:
        float(num)
        return True
    except ValueError:
        return False


def read_write_csv(string):
    if string == "read":
        lst = []
        with open('items.csv', 'r') as f:
            r = csv.reader(f, delimiter=',')
            for row in r:
                itemInfo = ['', '', '', 'r']  # Initialise/clear variable
                for i in range(0, len(row) - 1):
                    if i == 1:
                        itemInfo[i] = float(row[i])  # Add item price
                    elif i == 2:
                        itemInfo[i] = int(row[i])   # Add item priority
                    else:  # If string items
                        itemInfo[i] = row[i]  # Add item name
                lst.append(itemInfo)
        return lst
    else:  # write to csv file
        pass

main()
