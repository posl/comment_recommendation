def main():
    # Get input
    a, b, c, d = input()
    # Check if all digits are the same
    if (a == b and b == c and c == d):
        print("Weak")
    # Check if each digit follows the previous one
    elif (int(a) + 1 == int(b) or (a == "9" and b == "0")) and (int(b) + 1 == int(c) or (b == "9" and c == "0")) and (int(c) + 1 == int(d) or (c == "9" and d == "0")):
        print("Weak")
    else:
        print("Strong")

if __name__ == '__main__':
    main()