def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [i for i in range(1, n+1)]
    if p == q:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()