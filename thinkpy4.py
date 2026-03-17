def print_ngang():
    print("+ - - - - + - - - - +")

def print_doc():
    print("|         |         |")

def print_grid():
    print_ngang()
    for i in range(4):
        print_doc()
    print_ngang()
    for i in range(4):
        print_doc()
    print_ngang()

print_grid()
