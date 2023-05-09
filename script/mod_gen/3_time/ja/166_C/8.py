def main():
    n,m = map(int, input().split())
    h = list(map(int, input().split()))
    a = []
    b = []
    for i in range(m):
        a_,b_ = map(int, input().split())
        a.append(a_-1)
        b.append(b_-1)
    good = [1]*n
    for i in range(m):
        if h[a[i]] == h[b[i]]:
            good[a[i]] = 0
            good[b[i]] = 0
        elif h[a[i]] > h[b[i]]:
            good[b[i]] = 0
        else:
            good[a[i]] = 0
    print(sum(good))

if __name__ == '__main__':
    main()