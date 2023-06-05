def main():
    # input
    n = int(input())
    # process
    price = int(n * 1.08)
    # output
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")

if __name__ == '__main__':
    main()