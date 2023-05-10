def base(b):
    if b == "A":
        print("T")
    elif b == "T":
        print("A")
    elif b == "C":
        print("G")
    elif b == "G":
        print("C")
b = input()
base(b)

if __name__ == '__main__':
    base()