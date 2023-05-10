def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        if a > s:
            print('No')
        else:
            if s % 2 == 1:
                if a % 2 == 1:
                    print('Yes')
                else:
                    print('No')
            else:
                if a % 2 == 0:
                    print('Yes')
                else:
                    print('No')

if __name__ == '__main__':
    main()