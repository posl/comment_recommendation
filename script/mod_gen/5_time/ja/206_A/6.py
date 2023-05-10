def main():
    price = int(input())
    price = int(price * 1.08)
    if price < 206:
        print("Yay!")
    elif price > 206:
        print(":(")
    else:
        print("so-so")

if __name__ == '__main__':
    main()