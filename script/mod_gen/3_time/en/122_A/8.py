def main():
    base = input()
    if base == "A":
        print("T")
    elif base == "C":
        print("G")
    elif base == "G":
        print("C")
    elif base == "T":
        print("A")
    else:
        print("Error")
        return

if __name__ == '__main__':
    main()