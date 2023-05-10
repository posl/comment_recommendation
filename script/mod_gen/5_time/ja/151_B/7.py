def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = max(0, m*n - sum(a))
    print(ans if ans <= k else -1)

if __name__ == '__main__':
    main()