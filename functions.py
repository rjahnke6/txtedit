def create():
    filename = input("What would you like to name your file? DONT FORGET THE EXTENSION\n")
    print("Your file name is:", filename)
    file = open(filename, "w")
    file.close()

def disp():
    filename = input("What file would you like to display? DONT FORGET THE EXTENSION\n")
    file = open(filename, "r")
    print(file.read())
    file.close()

def addc():
    filename = input("What file would you like to add content to? DONT FORGET THE EXTENSION\n")
    file = open(filename, "a")
    add = input("Input the content you want added to the file:\n")
    file.write(add)
    file.close()

def delete():
    filename = input("What file would you like to delete? DONT FORGET THE EXTENSION\n")
    os.remove(filename)

def newl():
    filename = input("What file do you want to add a new line to? DONT FORGET THE EXTENSION\n")
    file = open(filename, "a")
    newlinestuff = input("What do you want to add on your new line?\n")
    file.write("\n")
    file.write(newlinestuff)
    file.close()
