def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = dict()
    for a in A:
        r = a % 200
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()