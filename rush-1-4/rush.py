import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        line = ""

        for col in range(x):
            if col == 0 and (row == 0 or row == y - 1):
                line += "A"
            elif col == x - 1 and (row == 0 or row == y - 1):
                line += "C"
            elif row == 0 or row == y - 1 or col == 0 or col == x - 1:
                line += "B"
            else:
                line += " "

        print(line)