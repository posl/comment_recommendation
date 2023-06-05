def main():
    b = input()
    if b == "A":
        print("T")
    elif b == "T":
        print("A")
    elif b == "G":
        print("C")
    elif b == "C":
        print("G")
    else:
        print("输入的碱基不正确！")

if __name__ == '__main__':
    main()