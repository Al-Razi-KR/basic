import basic as b
import Medium as m


def menu():
    basic_list = ["Add", "Substract", "Divide", "Power"]
    medium_list = ["Square", "Root", "Sine", "Log"]
    print("\nBasic")
    for item in range(len(basic_list)):
        print(f"{item+1}. {basic_list[item]}")
    print("\nMedium")
    for item in range(len(medium_list)):
        print(f"{item+len(medium_list)+1}. {medium_list[item]}")

def choice():
    user_choice = int(input("Enter your choice: "))
    if user_choice <= 0 or user_choice > 8:
        print("Invalid choice! Choose between 1-8.")
        menu()
        choice()
    elif user_choice <= 4:
        x = int(input("Enter 1st number: "))
        y = int(input("Enter 2nd number: "))
        if user_choice == 1:
            print(b.add(x, y))
        elif user_choice == 2:
            print(b.subtract(x, y))
        elif user_choice == 3:
            print(b.multiply (x, y))
        else:
            print(b.power(x, y))
    else:
        x = int(input("Enter the number: "))
        if user_choice == 5:
            print(m.square(x))
        elif user_choice == 6:
            print(m.root(x))
        elif user_choice == 7:
            print(m.sine(x))
        else:
            print(m.lg(x))
            