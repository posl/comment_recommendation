def main():
    n = int(input())
    price = int(1.08 * n)
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")

if __name__ == '__main__':
    main()