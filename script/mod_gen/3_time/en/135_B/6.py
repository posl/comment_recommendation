def main():
    N = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
        print('YES')
    else:
        if p[0] == 1 or p[-1] == N:
            print('YES')
        else:
            if p[0] == N and p[-1] == 1:
                print('YES')
            else:
                print('NO')

if __name__ == '__main__':
    main()