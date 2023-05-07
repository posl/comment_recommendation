def main():
    # Read a line
    line = input()
    # Split a line
    a, b = line.split()
    # Convert to integer
    a = int(a)
    b = int(b)
    # Output Yes or No
    if a * b % 2 == 1:
        print("Yes")
    else:
        print("No")
