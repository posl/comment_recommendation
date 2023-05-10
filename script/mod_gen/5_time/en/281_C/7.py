def main():
    n,t = map(int, input().split())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n):
        total += a[i]
    c = t // total
    d = t % total
    e = 0
    for i in range(n):
        e += a[i]
        if e > d:
            print(i+1, d)
            break

if __name__ == '__main__':
    main()