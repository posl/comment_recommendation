def main():
    A1, A2, A3 = [int(i) for i in input().split()]
    if (A1+A2+A3) >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()