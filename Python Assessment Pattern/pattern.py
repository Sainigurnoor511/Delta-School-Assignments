def right_angle_triangle(rows):
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end="")
        print()

def left_aligned_triangle(rows):
    for i in range(0, rows):
        for j in range(0, rows - i - 1):
            print(" ", end="")
        
        for j in range(0, i + 1):
            print("*", end="")
        print()

def pyramid(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))

def inverted_pyramid(rows):
    for i in range(rows):
        print(" " * i + "*" * (2 * (rows - i) - 1))

def diamond(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))
    for i in range(rows - 2, -1, -1):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))


right_angle_triangle(5)
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
left_aligned_triangle(5)
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
pyramid(5)
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
inverted_pyramid(5)
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
diamond(5)
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")