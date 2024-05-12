print("My name is Muhammad Aamir Bin Habib")

print("<------------------------------------------------------------->")

for i in range (1,11):
    print(i)


print("<------------------------------------------------------------->")

def print_pyramid(rows):
    """
    Function to print a pyramid of stars with the specified number of rows.
    """
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

def print_inverted_pyramid(rows):
    """
    Function to print an inverted pyramid of stars with the specified number of rows.
    """
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

def print_hollow_pyramid(rows):
    """
    Function to print a hollow pyramid of stars with the specified number of rows.
    """
    print("*" * (2 * rows - 1))
    for i in range(2, rows):
        print(" " * (rows - i) + "*" + " " * (2 * i - 3) + "*")
    print("*" * (2 * rows - 1))


rows = 5

print("Regular Pyramid:")
print_pyramid(rows)
print("\nInverted Pyramid:")
print_inverted_pyramid(rows)
print("\nHollow Pyramid:")
print_hollow_pyramid(rows)

print()
print("<---------- Printing the inverted pyramid again to ensure CI-CD ---------->")
print("\nInverted Pyramid:")
print_inverted_pyramid(rows)
