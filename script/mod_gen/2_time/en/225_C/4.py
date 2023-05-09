def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    a = [[i*7+j+1 for j in range(7)] for i in range(10**100)]
    for i in range(10**100-n+1):
        for j in range(7-m+1):
            if a[i:i+n][0][j:j+m] == b[0]:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()