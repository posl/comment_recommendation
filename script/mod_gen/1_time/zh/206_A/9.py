def main():
    n = int(input())
    price = int(n * 1.08)
    if price < 206:
        print("Yay!")
    elif price > 206:
        print(":(")
    else:
        print("so-so")

if __name__ == '__main__':
    main()