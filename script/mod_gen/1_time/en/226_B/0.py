def main():
    N = int(input())
    d = {}
    for i in range(N):
        a = list(map(int, input().split()))
        if a[0] in d:
            d[a[0]].append(a[1:])
        else:
            d[a[0]] = [a[1:]]
    ans = 1
    for i in d:
        ans *= len(set(map(tuple, d[i])))
    print(ans % (10**9 + 7))

if __name__ == '__main__':
    main()