def main():
    n, m = map(int, input().split())
    a = [0 for _ in range(m)]
    b = [0 for _ in range(m)]
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    for i in range(m):
        if a[i] == 1:
            print('POSSIBLE')
            exit()
    for i in range(m):
        if b[i] == n:
            print('POSSIBLE')
            exit()
    print('IMPOSSIBLE')

if __name__ == '__main__':
    main()