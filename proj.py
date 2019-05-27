#MODULE IMPORT
import functions
import os

#MAIN MENU
i = 1
while i == 1:
    print("Please select one of the following options:")
    print("1: create a file")
    print("2: display contents of file")
    print("3: add content to a file")
    print("4: delete a file")
    print("5: quit the program")
    print("6: start a new line in file")
    opt = int(input())
    if opt == 1:
        functions.create()
    elif opt == 2:
        functions.disp()
    elif opt == 3:
        functions.addc()
    elif opt == 4:
        functions.delete()
    elif opt == 5:
        exit()
    elif opt == 6:
        functions.newl()
    else:
        print("That option was not on the menu. Try again.\n")
