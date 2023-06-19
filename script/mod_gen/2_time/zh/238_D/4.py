def main():
    n = int(input())
    for i in range(n):
        a, s = map(int, input().split())
        if (s - a) % 2 == 0 and a <= s:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()