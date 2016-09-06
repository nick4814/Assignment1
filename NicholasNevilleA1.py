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


def load_items(lst, choice):

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
    else:
        state = 'r'

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


def add_items(lst, choice):
    # Function for adding items

    itName = inp_chk("Item name: ")
    price = inp_chk("Price: $")
    priority = inp_chk("Priority: ")


def inp_chk(string1):
    while True:
        try:
            if string1 == "Price: $":
                r = input(string1)
                if r < 0:
                    raise ValueError("Price must be >= $0")
                elif not isinstance(r, int):
                    raise TypeError("String is not of type 'int'")
            elif string1 == "Priority: ":
                r = int(input(string1))
                if 3 < r < 0:
                    raise ValueError("Priority must be 1, 2 or 3")
                elif not isinstance(r, int):
                    raise TypeError("String is not of type 'int'")
            else:  # Check string
                r = str(input(string1))
                if not any(c.isalpha() for c in r):  # If no letters in r (can contain numbers)
                    raise TypeError("String doesn't contain letters")
            if r.isnumeric():
                raise TypeError("String is not of type 'str'")
            break
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
    return r


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
            load_items(lst, choice)
        elif choice == "C":
            pass
        elif choice == "A":
            add_items(lst, choice)
        elif choice == "M":
            load_items(lst, choice)
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice = input(">>> ").upper()

main()