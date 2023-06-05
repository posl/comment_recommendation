def main():
    n, m = map(int, input().split())
    ans = 0
    for _ in range(n):
        k, *a = map(int, input().split())
        ans += len(set(a) & set(range(1, m+1))) == m
    print(ans)

if __name__ == '__main__':
    main()