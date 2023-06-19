def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k -= 1
    now = 0
    for i in range(60, -1, -1):
        if k & (1 << i):
            now = a[now]
            for j in range(i):
                now = a[now]
    print(now + 1)

if __name__ == '__main__':
    main()