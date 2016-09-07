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


MENU = ("Menu:\nR - List required items\nC - List completed items"
        "\nA - Add new item\nM - Mark an item as completed\nQ - Quit")


def loadItems(lst, choice):

    total = [0, 0]  # Total[0] is total price, Total[1] is total items
    pri = [0, 0, 0]  # To store priorities, pri[0] is 1, pri [1] is 2 ...

    for c in range(0, len(lst)):  # Get number of priorities
        if lst[c][2] == '1':
            pri[0] += 1
        elif lst[c][2] == '2':
            pri[1] += 1
        else:
            pri[2] += 1

    if choice == "R":
        print("Required items:")
        state = 'r'
    elif choice == "C":
        print("Completed items:")
        state = 'c'
    elif choice == "M":
        state = 'r'

    if choice == 'A':
        print("{}, ${:.2f} (priority {}) added to shopping list".format(lst[-1][0], float(lst[-1][1]), lst[-1][2]))

    else:
        for a in range(0, 3):
            i = 0
            for L in range(0, len(lst)):
                if i != pri[a]:  # Skip if printed all lists of priority a
                    if lst[L][2] == str(a+1) and lst[L][3] == state:  # If priority num and 'r' in lst[L]
                        print("{}. {} \t ${:.2f} ({})".format(a, lst[L][0], float(lst[L][1]), lst[L][2]))
                        total[0] += float(lst[L][1])
                        total[1] += 1
                        i += 1
        print("Total expected price for {} items: ${:.2f}".format(str(total[1]), total[0]))


def addItems(lst, choice):
    # Function for adding items
    itemInfo = ["", "", "", "r"]
    itemInfo[0] = inpChk("Item name: ")  # Item name (itemInfo[0]) can have letters, numbers and special characters
    itemInfo[1] = inpChk("Price: $")  # Price (itemInfo[1]) can be a float or an integer value
    itemInfo[2] = inpChk("Priority: ")  # itemInfo[2] stores priority value (integer)
    lst.append(itemInfo)
    loadItems(lst, choice)


# Function to handle inputs (extra error handling for different user inputs)
def inpChk(pick):
    specialChars = "!@#$%^&*()_=+`~,/'[]\<>?{}|"
    while True:
        try:
            r = input(pick)
            if pick == "Price: $":  # Check price input
                if any(c.isalpha() or (c in specialChars) for c in r):
                    raise ValueError("Price can't contain letters or these characters '{}'".format(specialChars))
                elif not floatOrNum(r):
                    raise TypeError("Input is not a whole or decimal number")
                elif float(r) < 0:  # Using float as it can evaluate integers and decimals
                    raise ValueError("Price must be >= $0")
            elif pick == "Priority: ":  # Check priority input
                if not r.isdigit():
                    raise TypeError("Invalid input; enter a valid number")
                elif not (1 <= int(r) <= 3):
                    raise ValueError("Priority must be 1, 2 or 3")
            else:  # Check string input
                if not any(c.isalpha() for c in r) and not(r.isspace() or not r) or any((c in specialChars) for c in r):
                    raise TypeError("Invalid string input")
            if not isinstance(r, int):  # If r is not an integer (r.isspace() doesn't work on integers)
                if r.isspace() or not r:
                    raise ValueError("Input can't be blank")
            break   # Exit while loop
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
    return r


def floatOrNum(num):  # Return true if float or int and false of not
    try:
        float(num)  # Using float as it can evaluate integers and decimals
        return True
    except ValueError:
        return False


def main():
    # Read CSV file once
    with open('items.csv', 'r') as f:
        r = csv.reader(f, delimiter=',')
        lst = list(r)

    print("Shopping List 1.0 - by Nicholas Neville")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "R":
            loadItems(lst, choice)
        elif choice == "C":
            pass
        elif choice == "A":
            addItems(lst, choice)
        elif choice == "M":
            loadItems(lst, choice)
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice = input(">>> ").upper()

main()