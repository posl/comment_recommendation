def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    ans = []
    for i in range(n):
        ans.append('Yes' if sum(p[i]) >= 300 * 3 - (n - k) else 'No')
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()