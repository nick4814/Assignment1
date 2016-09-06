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
    total = 0
    pri = [0, 0, 0]
    for c in range(0, len(lst)):
        if lst[c][2] == '1':
            pri[0] += 1
        elif lst[c][2] == '2':
            pri[1] += 1
        else:
            pri[2] += 1

    if choice == "R":
        print("Required items:")

        for a in range(0, 3):
            i = 0
            for L in range(0, len(lst)):
                if i != pri[a]: # Skip if printed all lists of priority a
                    if lst[L][2] == str(a+1) and lst[L][3] == 'r':  # If priority num and 'r' in lst[L]
                        print("{}. {} \t ${:.2f} ({})".format(a, lst[L][0], float(lst[L][1]), lst[L][2]))
                        total += float(lst[L][1])
                        i += 1
        print("Total expected price for 3 items: ${:.2f}".format(total))


def complete_items():
    # function for completing items
    pass


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
            pass
        elif choice == "M":
            pass
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using Shopping List 1.0")

main()