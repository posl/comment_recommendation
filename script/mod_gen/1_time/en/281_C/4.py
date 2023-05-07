def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    u = t % s
    c = 0
    for i in range(n):
        c += a[i]
        if u <= c:
            print(i+1, u)
            break

if __name__ == '__main__':
    main()