def main():
    cards = input().split()
    if cards[0] == cards[1] == cards[2]:
        if cards[3] == cards[4]:
            print("Yes")
        else:
            print("No")
    elif cards[0] == cards[1]:
        if cards[2] == cards[3] == cards[4]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()