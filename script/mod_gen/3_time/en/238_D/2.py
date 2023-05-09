def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        if a > s:
            print('No')
        elif a == s:
            if a == 0:
                print('Yes')
            else:
                print('No')
        else:
            if (s - a) % 2 == 0:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()