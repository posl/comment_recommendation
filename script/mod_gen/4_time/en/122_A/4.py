def main():
    b = input()
    if b == "A":
        print("T")
    elif b == "T":
        print("A")
    elif b == "C":
        print("G")
    elif b == "G":
        print("C")
    else:
        print("Please input A, C, G or T")

if __name__ == '__main__':
    main()