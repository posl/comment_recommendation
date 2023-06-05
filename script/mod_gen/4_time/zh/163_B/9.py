def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    if sum(a) <= n:
        print(0)
        return
    for i in range(m):
        if sum(a[:i]) <= n:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()