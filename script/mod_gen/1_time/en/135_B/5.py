def main():
    N = int(input())
    p = list(map(int, input().split()))
    p.sort()
    if p == list(range(1, N+1)):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()