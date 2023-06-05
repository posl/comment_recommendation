def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    count = 0
    while True:
        if all([x % 2 == 0 for x in a]):
            a = [x / 2 for x in a]
            count += 1
        elif all([x % 3 == 0 for x in a]):
            a = [x / 3 for x in a]
            count += 1
        else:
            break
    print(count if all([x == a[0] for x in a]) else -1)

if __name__ == '__main__':
    main()