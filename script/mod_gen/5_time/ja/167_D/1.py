def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k -= 1
    now = 0
    for i in range(60):
        if k & (1 << i):
            now = a[now]
        a = [a[a[j]] for j in range(n)]
    print(now + 1)

if __name__ == '__main__':
    main()