def main():
    n, s = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1 << n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            print('Yes')
            for j in range(n):
                if (i >> j) & 1:
                    print('H', end='')
                else:
                    print('T', end='')
            print()
            return
    print('No')

if __name__ == '__main__':
    main()