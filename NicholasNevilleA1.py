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
R_C = ['r', 'c']  # CONSTANT list


def main():
    menu = ("Menu:\nR - List required items\nC - List completed items"
            "\nA - Add new item\nM - Mark an item as completed\nQ - Quit")
    m_count = 0
    # Read from csv file once
    lsts = read_write_csv("read", None)  # Get list 'lsts' from 'items.csv'
    print("Shopping List 1.0 - by Nicholas Neville")
    print(menu)
    choice = input(">>> ").upper()
    while choice != 'Q':
        pri = order_lsts(lsts,'y')
        lsts = order_lsts(lsts, None)  # Split lists (r, c) and order nested lists by priority
        if choice == 'R':
            if sum(pri[0]) == 0:
                print("No required items")
            else:
                print("Required items:")
                load_items(lsts, choice, 1)  # 1 to Pass through if statement later
        elif choice == 'C':
            if m_count == 0:
                print("No completed items")
            else:
                print("Completed items:")
                load_items(lsts, choice, m_count)
        elif choice == 'A':
            add_items(lsts, choice)
        elif choice == 'M':
            if sum(pri[0]) == 0:
                print("No required items")
            else:
                m_count += 1
                lsts = load_items(lsts, choice, m_count)
        else:
            print("Invalid menu choice.")
        print(menu)
        choice = input(">>> ").upper()
    print("{} items saved to items.csv\nHave a nice day :)".format(len(lsts[1])))
    read_write_csv("write", lsts[1])


def load_items(lsts, choice, item_info):
    total = [0, 0]  # Total[0] is total price, Total[1] is total items
    lst_num = 0  # For 'M' and 'R'
    if choice == 'C':  # item_info stores m_count
        lst_num = 1
    if choice == 'A':
        print("{}, ${:.2f} (priority {}) added to shopping list".format(*item_info))
    else:  # If choice is 'R'/'C'/'M'
        if lsts[lst_num]:
            for row in lsts[lst_num]:
                max_width = 19  # For dynamic column padding
                space = max_width - len(row[0])
                print("{}. {} {} $  {:.2f} ({})".format(total[1], row[0], ' '*space, row[1], row[2]))
                total[0] += row[1]  # Accumulate total price
                total[1] += 1  # Accumulate total items
            if lsts[lst_num]:
                print("Total expected price for {} items: ${:.2f}".format(total[1], total[0]))
                if total[1] != 0:
                    if choice == 'M':
                        item_num = int(inp_chk("Enter the number of item to mark as completed \n>>> ", total[1]))
                        lsts[0][item_num][3] = 'c'
                        print("{} marked as completed".format(lsts[0][item_num][0]))
                        return lsts


def add_items(lsts, choice):  # Function for adding items
    item_info = ['', '', '', 'r']  # Initialise new list
    item_info[0] = inp_chk("Item name: ", None)  # Item name
    item_info[1] = float(inp_chk("Price: $", None))  # Store price as float
    item_info[2] = int(inp_chk("Priority: ", None))  # Store priority value as integer
    lsts[0].append(item_info)  # Add new list item 'item_info[]' to lst 'r'
    load_items(lsts, choice, item_info)  # Pass new 'lsts' ('r' values), choice and new list to loadItems() for printing


def order_lsts(temp_lsts, p):  # Function to order lists, and send priority
    lst = [[], []]  # Initialise nested list
    pri = [[0, 0, 0], [0, 0, 0]]  # To store priorities, pri[0] is priorities for 'r' list, pri[1] for 'c' list
    for row in temp_lsts[0]:  # Get number of priorities
        for item in range(0, 2):
            if row[3] == R_C[item]:
                if row[2] == 1:  # If priority is 1
                    pri[item][0] += 1
                elif row[2] == 2:  # If priority is 2
                    pri[item][1] += 1
                else:  # Priority is 3
                    pri[item][2] += 1
    for r_c in range(0, 2):  # Loop through R_C values
        for a in range(0, 3):  # Loop through priority values
            for lst1 in range(0, 2):  # Loop through temp_lst lists
                for row in temp_lsts[lst1]:
                    if row[2] == a + 1 and row[3] == R_C[r_c]:
                        lst[r_c].append(row)
    if p == 'y':
        return pri  # Return priority
    else:
        return lst  # Ordered and split list


def inp_chk(pick, sum_items):  # Function to handle inputs
    while True:
        try:
            r = input(pick)
            if pick == "Price: $" or pick == "Priority: " or pick == "Enter the number of item to mark as completed \n>>> ":
                if not(is_float(r) or r.isdigit()):
                    raise ValueError("Invalid input; enter a valid number")
                if pick == "Price: $" and float(r) < 0:  # Check price input and if r is negative
                    raise ValueError("Price must be >= $0")
                elif pick == "Priority: " and not (1 <= int(r) <= 3):  # Check input is priority: and r is not 1, 2 or 3
                    raise ValueError("Priority must be 1, 2 or 3")
                elif pick == "Enter the number of item to mark as completed \n>>> " and not (0 <= int(r) <= sum_items-1):
                    i = True
                    raise ValueError("Invalid item number")
            else:  # Check string input
                if not any(c.isalpha() for c in r) and not (r.isspace() or not r):  # if r has no letters and isn't blank
                    raise ValueError("Invalid string input")
            if not isinstance(r, int):  # If r is not an integer (r.isspace() doesn't work on integers)
                if r.isspace() or not r:  # If r is filled with spaces or empty
                    raise ValueError("Input can not be blank")
            break  # Exit while loop
        except ValueError as e:
            print(e)
    return r


def is_float(num):  # Return true if float, false if not
    try:
        float(num)
        return True
    except ValueError:
        return False


def read_write_csv(string, lsts):
    if string == "read":  # Add list to lst[0], all 'r' values
        lst = [[], []]
        with open('items.csv', 'r') as f:
            r = csv.reader(f, delimiter=',')
            for row in r:
                item_info = ['', '', '', 'r']  # Initialise/clear variable
                for i in range(0, len(row) - 1):
                    if i == 1:
                        item_info[i] = float(row[i])  # Add item price
                    elif i == 2:
                        item_info[i] = int(row[i])  # Add item priority
                    else:  # If string items
                        item_info[i] = row[i]  # Add item name
                lst[0].append(item_info)
        return lst
    else:  # write to csv file
        with open('items.csv', 'w', newline='') as f:
            w = csv.writer(f, delimiter=',')
            for row in lsts:
                w.writerow(row)


main()