def print_zigzag_pattern(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()