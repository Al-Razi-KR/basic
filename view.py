from Medium import *

def menu():
    basic_list = ["Add", "Substract", "Divide", "Power"]
    medium_list = ["Root", "Square", "Sin", "Log"]
    print("\nBasic")
    for item in range(len(basic_list)):
        print(f"{item+1}. {basic_list[item]}")
    print("\nMedium")
    for item in range(len(medium_list)):
        print(f"{item+1}. {medium_list[item]}")

menu()
