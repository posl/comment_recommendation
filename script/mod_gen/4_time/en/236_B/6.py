def main():
    n = int(input())
    cards = input().split()
    cards = [int(i) for i in cards]
    for i in range(1,n+1):
        if cards.count(i) == 4:
            continue
        else:
            print(i)
            break

if __name__ == '__main__':
    main()